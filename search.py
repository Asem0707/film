from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .deps import get_db
from .models import Movie


router = APIRouter(prefix="/search")


@router.get('/')
def search(query: str = '', limit: int = 20, db: Session = Depends(get_db)):
    q = db.query(Movie).filter(Movie.title.ilike(f"%{query}%"))
    results = q.order_by(Movie.popularity.desc()).limit(limit).all()
    return {"results": results}