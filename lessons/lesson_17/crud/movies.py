from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Movie
from schemas import MovieRequest

async def get_all_movies(db: AsyncSession) -> list[Movie]:
    result = await db.execute(select(Movie)) # SELECT * FROM movies
    movies = list(result.scalars().all())
    return movies

async def get_movie_by_id(movie_id: str, db:AsyncSession) -> Movie | None:
    result = await db.execute(select(Movie).where(Movie.id == movie_id))
    movie = result.scalar_one_or_none()
    return movie

async def create_movie(movie: MovieRequest, db: AsyncSession) -> Movie:
    new_movie = Movie(**movie.model_dump())
    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)

    return new_movie


async def update_movie_by_id(existing_movie: Movie, movie_update: MovieRequest, db: AsyncSession) -> Movie:
    for key, value in movie_update.model_dump(exclude_unset=True).items():
        setattr(existing_movie, key, value)

    db.add(existing_movie)
    await db.commit()
    await db.refresh(existing_movie)

    return existing_movie


async def delete_movie_by_id(movie: Movie, db: AsyncSession) -> Movie:
    await db.delete(movie)
    await db.commit()

    return movie