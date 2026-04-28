from app.database import SessionLocal,DATABASE_URL #bring the data base parmeter to here 
from app.models import Task #bring the FASTAPI datatype class JSON

#first time with decoretor 
def deco_start_close_DB(fun):
    def wrapper(*arg,**kwarg):
        session = SessionLocal()
        try:
            return fun(session,*arg,**kwarg)
        finally:
             session.close()
    return wrapper

#start the backend logic here 
@deco_start_close_DB
def create_task(session ,task):
    #session = SessionLocal() #start conecte with DB

    new_task = Task( #trans from JOS FASTAPI to DB 
        title = task.title,
        completed= task.completed
    )

    session.add(new_task) #add to db
    session.commit() #comit DB
    session.refresh(new_task) #refresh DB
    print("Saved task ID:", new_task.id)
    #print(DATABASE_URL)
    return new_task #return to endpoing as JSON


@deco_start_close_DB
def get_all_tasks(session):
    #session = SessionLocal() #start conecte with DB
    return session.query(Task).all() #return to endpoing as JSON


@deco_start_close_DB  
def get_task_by_id(session,task_id):
    #session = SessionLocal()#start conecte with DB
    return session.query(Task).filter(Task.id == task_id).first() #return to endpoing as JSON from the DB the first item has same ID Vule

@deco_start_close_DB    
def delete_task(session,task_id):
    #session = SessionLocal()#start conecte with DB
    task= session.query(Task).filter(Task.id == task_id).first()
    if not task: #check if there is task with this ID or no
     return False
    session.delete(task) # dekete from DB
    session.commit() #comit DB to save the change
    return True #return to HTTP endpoint bool

@deco_start_close_DB
def update_task(session,task_id, updated_task):
      #session = SessionLocal()#start conecte with DB
      task= session.query(Task).filter(Task.id == task_id).first()
      if not task:
       return False
      task.title= updated_task.title #update the value in DB parmter
      task.completed= updated_task.completed#update the value in DB parmter

      session.commit()#comit DB for save the change
      session.refresh(task) #refresh DB

      return task #return to HTTP endpoint