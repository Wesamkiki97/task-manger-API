from sqlalchemy import create_engine #bring create_engine from sqlalchemy
from sqlalchemy.orm import sessionmaker #bring sessionmaker from sqlalchemy.orm 

DATABASE_URL="postgresql://postgres:password@localhost:5432/task_db" #the path of the DB and information 
engine = create_engine(DATABASE_URL) 
SessionLocal = sessionmaker(bind=engine)
