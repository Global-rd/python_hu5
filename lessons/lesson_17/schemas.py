from pydantic import BaseModel, Field

#pydantic model

class MovieRequest(BaseModel):

    title: str = Field(..., min_length=1)
    genre: str
    year: int
    length_in_mins: int

    rating: int = 0

class MovieResponse(MovieRequest):

    id: str


