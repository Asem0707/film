from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.database import Base, engine
from app.auth import router as auth_router
from app.search import router as search_router
from app.recommendations import router as rec_router
from app.films import router as films_router

# создаём приложение
app = FastAPI(title="Movie Recommendation API")

# создаём таблицы
Base.metadata.create_all(bind=engine)

# подключаем роутеры
app.include_router(auth_router)
app.include_router(search_router)
app.include_router(rec_router)
app.include_router(films_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}
