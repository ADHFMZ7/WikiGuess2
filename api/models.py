from sqlmodel import SQLModel
from pydantic import BaseModel

class User(SQLModel, table=True):
  identifier: str
  score: int
  highscore: int

class ArticleDB(SQLModel, table=True):
  gen_article: str
  wiki_article: str
  currect_article: bool

class ArticleRequest(BaseModel):
  article1: str
  article2: str
