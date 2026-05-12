from fastapi import APIRouter, HTTPException #bring API Router,and this HTTP Exception 
from app.schemas import TaskCreate, TaskResponse #from schemas.py bring the Request and Response that trans the data to Json
from app.services import task_service #from services.py bring task_service the functions backend of the req/res
router = APIRouter() #make this variable APIRouter 


@router.post("/tasks",response_model=TaskResponse) #Http URL endpoint ( response_model=TaskResponse before display the value we send it to pydantic library for validate)
def create_task(task:TaskCreate): #function of this endpoint task attribute with TaskCreate type Json
    return task_service.create_task(task) #call the create_task endpoint from task_service from service.py with task parameter 


#get by ID
@router.get("/tasks/{task_id}",response_model=TaskResponse) #Http URL with parameter endpoint ( response_model=TaskResponse before display the value we send it to pydantic library for validate)
def get_task_by_ID(task_id:int):#Function calling
    task = task_service.get_task_by_id(task_id) #call get_task_by_ID function from task_service from service.py
    if not task:#this endpoint will return value if has the value of task_id parameter or no
        raise HTTPException(status_code=404, detail="Task Not Found")#massage if not has and handle this exception
    return task #return the task if has this ID

#get by completed of not completed
@router.get("/tasks",response_model=list[TaskResponse]) #Http URL with parameter endpoint ( response_model=TaskResponse before display the value we send it to pydantic library for validate)
def get_task_by_complete(completed:bool | None = None):#Function calling
    task = task_service.get_tasks_by_completed(completed) #call get_task_by_ID function from task_service from service.py
    if not task:#this endpoint will return value if has the value of task_id parameter or no
        raise HTTPException(status_code=404, detail="Task Not Found")#massage if not has and handle this exception
    return task #return the task if has this ID

@router.delete("/tasks/{task_id}") #Http URL with parameter endpoint ( response_model=TaskResponse before display the value we send it to pydantic library for validate)
def delete_task(task_id:int):#Function calling
    success = task_service.delete_task(task_id)#call delete_task function from task_service from service.py
    if not success:#this endpoint will return value if has the value of task_id parameter or no
        raise HTTPException(status_code=404, detail="Task Not Found")#massage if not has and handle this exception
    return{"message": "Task deleted"} #return this massage if has  ID after function done


@router.put("/tasks/{task_id}",response_model=TaskResponse) #Http URL endpoint ( response_model=TaskResponse before display the value we send it to pydantic library for validate)
def update_task(task_id:int , new_task: TaskCreate): #Function calling 
    task=task_service.update_task(task_id, new_task) #call update_task function from task_service from service.py
    if not task: #this endpoint will return value if has the value of task_id parameter or no
      raise HTTPException(status_code=404, detail="Task Not Found")#massage if not has and handle this exception
    return task #return this massage if has  ID after function done

