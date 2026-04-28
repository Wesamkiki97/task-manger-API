from pydantic import BaseModel #bring BaseModel from pydantic library for validate the FASTAPI values 

class TaskCreate(BaseModel): #this class to ensure the request of FASTAPI values JSON type
    title: str
    completed: bool =False

class TaskResponse(BaseModel): #this class to ensure the Response of FASTAPI values JSON type
    title: str
    id: int
    title: str
    completed: bool

    class Config: 
        from_attributes= True