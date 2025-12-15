from app.database import SessionLocal
from app.models import Film

films_data = [
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014},
    {"title": "The Matrix", "genre": "Sci-Fi", "year": 1999},
    {"title": "The Dark Knight", "genre": "Action", "year": 2008},
    {"title": "Forrest Gump", "genre": "Drama", "year": 1994},
    {"title": "Gladiator", "genre": "Action", "year": 2000},
    {"title": "Titanic", "genre": "Romance", "year": 1997},
    {"title": "Avatar", "genre": "Sci-Fi", "year": 2009},
    {"title": "The Shawshank Redemption", "genre": "Drama", "year": 1994},
    {"title": "The Godfather", "genre": "Crime", "year": 1972},
    {"title": "Pulp Fiction", "genre": "Crime", "year": 1994},
    {"title": "Fight Club", "genre": "Drama", "year": 1999},
    {"title": "Se7en", "genre": "Thriller", "year": 1995},
    {"title": "The Silence of the Lambs", "genre": "Thriller", "year": 1991},
    {"title": "The Green Mile", "genre": "Drama", "year": 1999},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "genre": "Fantasy", "year": 2001},
    {"title": "The Lord of the Rings: The Two Towers", "genre": "Fantasy", "year": 2002},
    {"title": "The Lord of the Rings: The Return of the King", "genre": "Fantasy", "year": 2003},
    {"title": "Harry Potter and the Philosopher's Stone", "genre": "Fantasy", "year": 2001},
    {"title": "Harry Potter and the Chamber of Secrets", "genre": "Fantasy", "year": 2002},
    {"title": "Harry Potter and the Prisoner of Azkaban", "genre": "Fantasy", "year": 2004},
    {"title": "Star Wars: A New Hope", "genre": "Sci-Fi", "year": 1977},
    {"title": "Star Wars: The Empire Strikes Back", "genre": "Sci-Fi", "year": 1980},
    {"title": "Star Wars: Return of the Jedi", "genre": "Sci-Fi", "year": 1983},
    {"title": "Joker", "genre": "Drama", "year": 2019},
    {"title": "Parasite", "genre": "Thriller", "year": 2019},
    {"title": "Whiplash", "genre": "Drama", "year": 2014},
    {"title": "La La Land", "genre": "Romance", "year": 2016},
    {"title": "The Avengers", "genre": "Action", "year": 2012},
    {"title": "Avengers: Infinity War", "genre": "Action", "year": 2018},
    {"title": "Avengers: Endgame", "genre": "Action", "year": 2019},
    {"title": "Pirates of the Caribbean: The Curse of the Black Pearl", "genre": "Adventure", "year": 2003},
    {"title": "Jurassic Park", "genre": "Adventure", "year": 1993},
    {"title": "The Lion King", "genre": "Animation", "year": 1994},
    {"title": "Toy Story", "genre": "Animation", "year": 1995},
]

def seed():
    db = SessionLocal()

    
    db.query(Film).delete()

    for film in films_data:
        db.add(Film(**film))

    db.commit()
    db.close()
    print("✅ Фильмы добавлены")

if __name__ == "__main__":
    seed()

