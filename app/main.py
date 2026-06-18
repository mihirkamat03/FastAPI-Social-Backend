from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utilis
from .database import engine, get_db 
from sqlalchemy.orm import Session
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

origins=["https://www.google.com"]

app = FastAPI()
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def test():
    return{"Hello world"}

# def get_db():
#     db=SessionLocal
#     try:
#         yield db
#     finally:
#         db.close

 

# class Post(BaseModel):              #Now we are commenting this as we have put all the specs in schemas.py
#     title: str
#     content: str
#     published: bool= True
# rating: Optional[int]= None         #as it is not in models.py
    
    
    
# DATABASE CONNECTION

# while True:
#     try:
#         conn= psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Broker$123', cursor_factory=RealDictCursor)
#         cursor= conn.cursor()
#         print("success")
#         break
    
#     except Exception as error:
#         print(error)
#         time.sleep(10)

    
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
