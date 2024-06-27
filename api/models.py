from sqlmodel import Field, SQLModel
from pydantic import BaseModel

# class User(SQLModel, table=True):
#   id: str = Field(default=)
#   name: str
#   score: int
#   highscore: int

# class ArticleRequest(BaseModel):
#   article1: str
#   article2: str

class ArticleDB(SQLModel, table=True):
  id: str
  gen_article: str
  wiki_article: str

