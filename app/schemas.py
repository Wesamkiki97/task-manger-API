from pydantic import BaseModel #bring BaseModel from pydantic librerry for validet the FASTAPI values 

class TaskCreate(BaseModel): #this calss to ensure the requset of FASTAPI values JSON type
    title: str
    completed: bool =False

class TaskResponse(BaseModel): #this calss to ensure the Response of FASTAPI values JSON type
    title: str
    id: int
    title: str
    completed: bool

    class Config: 
        from_attributes= True