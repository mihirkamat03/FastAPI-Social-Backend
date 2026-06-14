from .. import models, schemas, oauth2
from typing import List, Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router=APIRouter(prefix="/posts", tags=["Posts"])

my_posts=[{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "title of post 2", "content": "content of post 2", "id": 2}, {"title": "title of post 3", "content": "content of post 3", "id": 3}]

def find_post(id):
    for post in my_posts:
        if post["id"]==id:
            return post
        

def find_index(id):
    for i, p in enumerate(my_posts):
        if p["id"]==id:
            return i  


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session= Depends(get_db), limit: int = 10, skip: int= 0, search: Optional[str]= ""):
    # cursor.execute(""" SELECT * FROM posts """)
    # posts= cursor.fetchall()
    posts= db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post :schemas.PostCreate, db: Session= Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):    
    # cursor.execute(f"INSERT INTO (title, content, published) VALUES ({post.title}, {post.content}")
    # cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    # new_post=cursor.fetchone()
    # conn.commit()
    
    # new_post=models.Post(title= post.title, content= post.content, published=post.published)
                        #  OR
    new_post= models.Post(user_id= current_user.id, **post.dict()) # It will go to models.py and get the db contents from class Post in a dictionary form
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return post  


# USING RESPONSE

# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
#     post = find_post(id)
#     if not post:
#         response.status_code=status.HTTP_404_NOT_FOUND
#         return{"message": f"post with id: {id} not found!!"}
#     return{"post": post}



# USING HTTP EXCEPTION
# MOST PEREFERED AS IT IS SHORT
@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session=Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s RETURNING *""", [id])   #HERE U CAN JUST PUT [id] OR USE TUPLE str((id),)
    # sing_post = cursor.fetchone()
    
    sing_post=db.query(models.Post).filter(models.Post.id==id).first()
    
    if not sing_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found!!")
        
    return sing_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session=Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    # index=find_index(id)
    # cursor.execute(""" DELETE FROM posts WHERE id= %s RETURNING *""", [id])
    # deleted_post=cursor.fetchone()
    # conn.commit()
    
    deleted_post_query=db.query(models.Post).filter(models.Post.id==id)
    
    deleted_post=deleted_post_query.first()
    
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found!!")
    
    if deleted_post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform this action!!")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()
    
    #my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT), {"post deleted"}



@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int ,post:schemas.PostCreate,  db: Session=Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE posts SET title= %s, content= %s, published=%s WHERE id= %s """, (post.title), (post.content), (post.published), [id])
    # updated_post= cursor.fetchone()
    # conn.commit() 
    # index=find_index(id)
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    updated_post = post_query.first()
    
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found!!")
    
    if updated_post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform this action!!")
    
    post_query.update(post.dict(), synchronize_session=False)
    
    db.commit()    
    db.refresh(updated_post)
    
    # post_dict=post.dict()
    # post_dict["id"]=id
    # my_posts[index]=post_dict
    # return{"data": post_dict}
    return updated_post