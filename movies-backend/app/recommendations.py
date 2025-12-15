from fastapi import APIRouter, Depends
from .deps import get_db
from .models import Rating, Movie
from sqlalchemy.orm import Session
import numpy as np
import joblib
import os


router = APIRouter(prefix="/recommendations")


ARTIFACTS = os.getenv('ML_ARTIFACTS_PATH','./ml/artifacts')
ITEM_SIM_PATH = os.path.join(ARTIFACTS,'item_sim.npy')
ID_INDEX_PATH = os.path.join(ARTIFACTS,'movie_id_index.pkl')


ITEM_SIM = None
ID_INDEX = None
INDEX_ID = None


if os.path.exists(ITEM_SIM_PATH) and os.path.exists(ID_INDEX_PATH):
    ITEM_SIM = np.load(ITEM_SIM_PATH)
    ID_INDEX = joblib.load(ID_INDEX_PATH)
    INDEX_ID = {v:k for k,v in ID_INDEX.items()}


@router.get('/')
def get_recommendations(user_id: int = 1, db: Session = Depends(get_db), limit: int = 10):
    if ITEM_SIM is None or ID_INDEX is None:
# fallback popular
       movies = db.query(Movie).order_by(Movie.popularity.desc()).limit(limit).all()
       return {"recommendations": movies}


    ratings = db.query(Rating).filter(Rating.user_id==user_id).all()
    if not ratings:
        movies = db.query(Movie).order_by(Movie.popularity.desc()).limit(limit).all()
        return {"recommendations": movies}


    scores = np.zeros(ITEM_SIM.shape[0])
    for r in ratings:
        idx = ID_INDEX.get(r.movie_id)
        if idx is not None:
            scores += ITEM_SIM[idx] * (r.rating - 3)


    top_idx = np.argsort(-scores)[:limit]
    ids = [INDEX_ID[i] for i in top_idx if i in INDEX_ID]
    movies = db.query(Movie).filter(Movie.id.in_(ids)).all()
    return {"recommendations": movies}
