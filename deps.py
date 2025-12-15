from .database import SessionLocal
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from .models import User
from sqlalchemy.orm import Session
import os


SECRET = os.getenv('SECRET_KEY', 'supersecret')
ALGO = 'HS256'


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(lambda: None), db: Session = Depends(get_db)):
# placeholder: in production use OAuth2PasswordBearer; here frontend will send user_id param or token
# For simplicity, allow user_id query param when developing
    raise HTTPException(status_code=400, detail="Not implemented: use query user_id for dev")