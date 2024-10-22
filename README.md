# Student Progress Management System

This project is a Django-based web application designed to manage student progress, including CRUD operations, sorting by teacher, and generating statistics on student marks.

## Table of Contents
- [Student Progress Management System](#student-progress-management-system)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)

## Features

- **CRUD Operations**: 
  - Add new students, retrieve the list of students, update existing student information, and delete student records.
  
- **Filter Students by Subject Marks**: 
  - Retrieve students sorted by their marks in specific subjects like chemistry, physics, and maths.
  
- **Sort Students by Class Teacher**: 
  - View students assigned to a specific class teacher.
  
- **Student Statistics**: 
  - Generate various reports:
    - Average marks of students.
    - List of students who have failed.
    - Top 5 students based on marks.
    - Analyze student performance by teacher.
    
- **Admin Panel**:
  - Manage student records and related data through the Django admin interface.

## Technologies Used
- Python
- Django
- SQLite (or your choice of database)
- Django REST Framework (if applicable)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/albyUtomy/django-basic-to-up.git
    ```
2. Navigate to the project directory:
    ```bash
    cd basic_crud_operation_project
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:'
   * On Windows :
        ```bash
        venv\Scripts\activate
        ```
   * On macOS/Linux
        ```bash
        source venv/bin/activate
        ```
5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
6. Run database migrations:

    ```bash
    python manage.py migrate
    ```
7. Start the development server:

    ```bash
    python manage.py runserver
    ```
## Usage
Once the server is running, you can access the application at http://127.0.0.1:8000/. You can perform various operations such as adding students, modifying their records, and retrieving statistics.

## API Endpoints

| Method | Endpoint                             | Description                                                       |
|--------|--------------------------------------|-------------------------------------------------------------------|
| GET, POST, DELETE | `/`                                  | List all students, add a new student, or delete students          |
| GET, PUT, DELETE  | `/student/<int:roll_no>/`             | Retrieve, update, or delete a single student by roll number        |
| GET    | `/subject/<str:subject>/`              | Get students sorted by subject marks (chemistry, physics, maths)   |
| GET    | `/class_teacher/<str:teacher_name>/`  | Retrieve students taught by a specific class teacher               |
| GET    | `/statics/<str:filtration>/`          | Retrieve statistics (average-marks, report-failed, top 5, teacher-analysis) |

