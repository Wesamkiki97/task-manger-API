from fastapi import FastAPI #bring the FASTAPI to this project
from app.routes import tasks #bring the EndPoints(routers) HTTP
app = FastAPI()   #Make this variable FASTAPI 

app.include_router(tasks.router) #Call the EndPoints(routers) HTTP

@app.get("/") #HTTP req handling (endpoint)
def home(): #the home Function that will run when req this endpoint
    return{"message":"Task Manger API is ruining"}








