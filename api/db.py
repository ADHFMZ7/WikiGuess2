from sqlmodel import Session, SQLModel, create_engine, select
from models import ArticleDB

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
# engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
  """
  returns a database session
  """
  ...

def get_random_articles(session: Session) -> ArticleDB:
  """
  Fetches a random pair of articles from the databse
  """
  ... 

# def create_user(session: Session, user: User) -> int | None:
#     session.add(user)  
#     session.commit()
#     return user.id
#
# def get_user_by_id(session: Session, user_id: str) -> User | None:
#     """
#     fetch the user identified by user_id from the database
#
#     parameters:
#         session: Session - the active database session
#         user_id: int - primary key identifying the user
#
#     returns:
#         Optional[User] - User object if found, None otherwise
#     """
#     ...
#     statement = select(User).where(User.id == user_id)
#     result = session.exec(statement)
#
#     return result.first()
#
