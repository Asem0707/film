from pydantic import BaseModel
from typing import Optional, List


class MovieBase(BaseModel):
    title: str
    description: Optional[str]
    poster: Optional[str]
    year: Optional[int]
    genres: Optional[List[str]]
    rating: Optional[float]


class MovieOut(MovieBase):
    id: int
    class Config:
        orm_mode = True


class UserCreate( BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
