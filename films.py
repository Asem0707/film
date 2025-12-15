from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import Film

router = APIRouter(
    prefix="/films",
    tags=["Films"]
)

@router.get("/")
def get_films(db: Session = Depends(get_db)):
    return db.query(Film).all()
