#from pydantic import BaseModel
from sqlalchemy import Column,Integer,String,Boolean #we bring this datatypes from sqlalchemy library 
from sqlalchemy.orm import declarative_base #bring declarative_base from sqlalchemy 

Base= declarative_base() #declare this parameter and set declarative_base function 
#Task model (data shape)

# !here was locale  list instead DB
# class Task(BaseModel):
#     title: str
#     completed: bool =False


class Task(Base): #create this class datatype to prepare sql parameter 
    __tablename__="tasks" 
    id= Column(Integer,primary_key=True,index=True) 
    title= Column(String)
    completed= Column(Boolean,default=True) 