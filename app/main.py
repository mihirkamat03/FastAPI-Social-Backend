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
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

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

