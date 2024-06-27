from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import create_db_and_tables, get_session, get_randon_articles
from sqlmodel import Session
from models import ArticleDB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_db_and_tables()

# @app.get('/session')
# def open_session():
#
#   # create random uuid
#   uuid = 
#
#   # create user profile 
#
#   return uuid   

@app.get("/articles")
def get_articles(session: Session = Depends(get_session)):
  
  articles = get_random_articles(session)
  
  if not articles:
    raise HTTPException(status_code=404, detail="failed to fetch articles")

  return articles
