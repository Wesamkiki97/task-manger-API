#from pydantic import BaseModel
from sqlalchemy import Column,Integer,String,Boolean #we bring this datatypes from sqlalchy librerry 
from sqlalchemy.orm import declarative_base #bring declarative_base from sqlalchemy 

Base= declarative_base() #declear this parmeter and set declaative_base function 
#Task model (data shape)

#here was locle  list instad DB
# class Task(BaseModel):
#     title: str
#     completed: bool =False


class Task(Base): #creat this class datatype to prapre sql parmeter 
    __tablename__="tasks" 
    id= Column(Integer,primary_key=True,index=True) 
    title= Column(String)
    completed= Column(Boolean,default=True) 