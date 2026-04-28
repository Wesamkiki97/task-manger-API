# Task Manager API

A simple backend REST API for managing tasks, built with FastAPI and PostgreSQL.


## Features

- Create new tasks
- Get all tasks
- Get task by ID
- Update tasks
- Delete tasks
- Structured project architecture (routes, services, schemas)


## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn


## Project Structure

task-manager-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
|   ├── init_db.py
│   ├── routes/
│   │   └── tasks.py
│   └── services/
│       └── task_service.py


## Installation

pip install -r requirements.txt


## Run the Server

uvicorn app.main:app --reload


## API Endpoints

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| POST   | /tasks      | Create task     |
| GET    | /tasks      | Get all tasks   |
| GET    | /tasks/{id} | Get single task |
| PUT    | /tasks/{id} | Update task     |
| DELETE | /tasks/{id} | Delete task     |


## Future Improvements

User authentication
Task priority levels
Due dates
Docker support
Unit testing
Author


## Author

Wesam Kiki