from pydantic import  BaseModel, EmailStr,conint, Field
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str = Field(..., title="Title of the Post", description="Must be at least 3 characters long", min_length=3)
    content: str = Field(..., description="The main body of the post")
    published: bool = Field(True, description="Set to false to save as a draft")

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes=True
        

class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserOut
    
    class Config:
        from_attributes=True
        
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str
        
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int]
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)