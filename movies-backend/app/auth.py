from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from .deps import get_db
from .models import User
from .schemas import UserCreate, Token


router = APIRouter(prefix="/auth")
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET = "supersecret"
ALGO = "HS256"


@router.post('/register')
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username==user.username).first()
    if existing:
        raise HTTPException(400, "User exists")
    hashed = pwd.hash(user.password)
    u = User(username=user.username, hashed_password=hashed)
    db.add(u); db.commit()
    return {"status":"ok"}


@router.post('/login', response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    dbu = db.query(User).filter(User.username==user.username).first()
    if not dbu or not pwd.verify(user.password, dbu.hashed_password):
        raise HTTPException(400, "Invalid credentials")
    token = jwt.encode({"sub": dbu.username, "uid": dbu.id, "exp": datetime.utcnow() + timedelta(days=1)}, SECRET, algorithm=ALGO)

    return {"access_token": token}
