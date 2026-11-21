from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from crud.movies import (
    create_movie,
    delete_movie_by_id,
    get_all_movies,
    get_movie_by_id,
    update_movie_by_id
)
from models import Movie
from schemas import MovieRequest

async def list_movies_service(db: AsyncSession) -> list[Movie]:
    return await get_all_movies(db)

async def create_movie_service(movie: MovieRequest, db: AsyncSession) -> Movie:
    return await create_movie(movie, db)

async def get_movie_service(movie_id: str, db: AsyncSession) -> Movie:
    movie = await get_movie_by_id(movie_id, db)

    if movie is None:
        raise HTTPException(status_code=404, detail=f"Movie id {movie_id} not found")

    return movie


async def update_movie_service(movie_id: str, movie_update: MovieRequest,
                               db:AsyncSession) -> Movie:

    movie = await get_movie_service(movie_id, db)
    return await update_movie_by_id(movie, movie_update, db)

async def delete_movie_service(movie_id: str, db:AsyncSession) -> Movie:
    movie = await get_movie_service(movie_id, db)

    return await delete_movie_by_id(movie, db)