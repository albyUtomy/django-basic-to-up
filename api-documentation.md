# Project Management System API
## Overview
This API provides access to manage student progress, including their marks, assigned teachers, departments, and school details. Authentication is required for all endpoints.

## Base URL
```url
http://<your-domain>/
```

## End Points in this project
# API Endpoints
There are 24 endpoints in total for your project. Here’s the breakdown by section:

* **Department API Endpoints: 5**
* **School API Endpoints: 5**
* **Teacher API Endpoints: 7**
* **Student API Endpoints: 7**


### School API Endpoints

| Endpoint                                        | Method            | Description                                               |
|-------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/school/`                                  | GET, POST         | Retrieve all schools or create a new school record.       |
| `/api/school_details/<school_id>/`              | GET, PUT, DELETE  | Retrieve, update, or delete a school by ID.               |
| `/api/school/departments/<school_id>`           | GET               | List departments within a specific school.                |
| `/api/school/teachers/<school_id>`              | GET               | List teachers within a specific school.                   |
| `/api/school/students/<school_id>`              | GET               | List students within a specific school.                   |

---

### Department API Endpoints

| Endpoint                                       | Method            | Description                                   |
|------------------------------------------------|-------------------|-----------------------------------------------|
| `/api/department/`                             | GET, POST         | Retrieve all departments or create a new department. |
| `/api/department/<department_id>/`             | GET, PUT, DELETE  | Retrieve, update, or delete a department by ID. |
| `/api/department_filter/<department_id>/`      | GET               | Filter departments by department ID.               |
| `/api/department_teacher/<department_id>/`     | GET               | Retrieve teachers under a specific department by ID. |
| `/api/department_student/<department_id>/`     | GET               | Retrieve students under a specific department by ID. |

---


### Teacher API Endpoints

| Endpoint                                         | Method            | Description                                               |
|--------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/teacher/`                                  | GET, POST         | Retrieve all teachers or create a new teacher.            |
| `/api/teacher/<teacher_id>/`                     | GET, PUT, DELETE  | Retrieve, update, or delete a teacher by ID.              |
| `/api/teacher/sort_students/<teacher_name>/`     | GET               | Retrieve students taught by a specific teacher.           |
| `/api/teacher/teacher_sort_a_z/`                 | GET               | Retrieve a list of teachers sorted alphabetically.        |
| `/api/teacher/teacher_report/`                   | GET               | Generate a performance report for all teachers.           |
| `/api/teacher/teacher_report/<teacher_name>/`    | GET               | Generate a performance report for a specific teacher.     |
| `/api/teacher/best_teacher/`                     | GET               | Retrieve the best-performing teacher.                     |

---

### Student API Endpoints

| Endpoint                                         | Method            | Description                                               |
|--------------------------------------------------|-------------------|-----------------------------------------------------------|
| `/api/students/`                                 | GET, POST         | Retrieve all students or create a new student record.     |
| `/api/students/<student_id>/`                    | GET, PUT, DELETE  | Retrieve, update, or delete a student by ID.              |
| `/api/students/subject/<subject>/`               | GET               | Retrieve students sorted by marks in a specific subject.  |
| `/api/students/statics/<filtration>/`            | GET               | Retrieve statistics based on the specified filtration.    |





# In Detailed

## Student API Endpoints

| Endpoint                               | Method            | Description                                                                                                 |
|----------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------|
| `/app_students/students/`                       | GET, POST         | Retrieve a list of students or create a new student record.                                                 |
| `/app_students/students/<student_id>/`          | GET, PUT, DELETE  | Retrieve, update, or delete a specific student by their ID.                                                 |
| `/app_students/students/subject/<subject>/`     | GET               | Retrieve a list of students sorted by marks in a specific subject (e.g., chemistry, physics, or maths).     |
| `/app_students/students/statics/<filtration>/`  | GET               | Retrieve statistics based on the specified filtration (e.g., average marks, top 5 students, failed report). |

---
# Student APP
### 1. List All Students
* URL: ``` /app_students/students/```
* Method: GET
* Description: Retrieves a list of all students and their progress details.
* Response:
    - Status 200: List of students with details like name, roll number, marks, department, and school.
    - Status 404: No students found for the specified school_id.
* Sample Response:
```json
{
  "Students": [
    {
      "roll_no": 1,
      "name": "STUA",
      "percentage": 85.0,
      "gained_mark": 255.0,
      "out_off": 300,
      "class_teacher": "Mr. Smith",
      "school_details": "Central School",
      "department_details": "Science"
    }
  ]
}
```
### 2. Retrieve Student by ID
* URL: ```/app_students/students/<roll_no>/```
* Method: GET
* Description: Fetches details of a specific student by their roll number.
* Response:
    - Status 200: Student details.
    - Status 404: Student not found.
* Sample Response:
```json
{
  "roll_no": 1,
  "name": "STUA",
  "percentage": 85.0,
  "gained_mark": 255.0,
  "out_off": 300,
  "class_teacher": "Mr. Smith",
  "school_details": "Central School",
  "department_details": "Science"
}
```

### 3. Create a New Student Record
* URL: ```/app_students/students/```
* Method: POST
* Description: Creates a new student progress record.
* Request Body:
```json
{
  "name": "STUA",
  "chemistry_mark": 85.0,
  "physics_mark": 90.0,
  "maths_mark": 80.0,
  "class_teacher_id": 1,
  "school_id": 2,
  "department_id": 19
}
```
* Response:
    - Status 201: Created student record.
    - Status 400: Validation error or missing required fields.


### 4. Update a Student Record
* URL: ```/app_students/students/<roll_no>/```
* Method: PUT
* Description: Updates details for a specific student.
* Request Body:
```json
{
  "chemistry_mark": 90.0,
  "physics_mark": 85.0,
  "maths_mark": 88.0
}
```
* Response:
    - Status 200: Updated student data.
    - Status 404: Student not found.

### 5. Delete a Student Record
* URL: ```/app_students/students/<roll_no>/```
* Method: DELETE
* Description: Deletes a student progress record.
* Response:
    - Status 204: No content, successful deletion.
    - Status 404: Student not found.

### 6 Retrieve Students Sorted by Subject Marks
* URL: ```/app_students/subject/<subject>/```
* Method: GET

        This endpoint returns a list of students sorted by their marks in a specified subject (e.g., chemistry, physics, or maths). You pass the subject name as a parameter in the URL.

#### ** URL Parameters:**

* subject: The subject to sort by. Acceptable values are chemistry, physics, and maths.
Usage Example:

* ```/app_students/subject/chemistry/``` - Retrieves a list of students sorted by their chemistry marks.
* ```/app_students/subject/physics/``` - Retrieves a list of students sorted by their physics marks.
* ```/app_students/subject/maths/``` - Retrieves a list of students sorted by their maths marks.
* Response:
    - Status 200: Returns a list of students, sorted by the specified subject marks.
    - Status 404: If no students are found or the subject parameter is incorrect.

### 7. ```/app_students/statics/<str:filtration>/``` - Retrieve Student Mark Statistics
* URL: ```/app_students/statics/<filtration>/```
* Method: GET
        This endpoint provides various statistics on student marks, depending on the filter specified in the URL.
    ### **URL Parameters:**
    * **filtration** : The type of statistical data to retrieve. Acceptable values include:
    * **average-marks** : Returns the average marks across all students for each subject.
    * **report-failed** : Lists students who have failed (according to predefined pass criteria) in one or more subjects.
    * **top5** : Lists the top 5 students based on total gained marks or a specific criteria.

    ### Usage Example:
    * ```/app_students/statics/average-marks/``` - Retrieves the average marks of students in all subjects.
    * ```/app_students/statics/report-failed/``` - Retrieves a report of students who have failed.
    * ```/app_students/statics/top5/``` - Retrieves a list of the top 5 students based on marks.
    * Response:
        - Status 200: Returns the requested statistical data.
        - Status 404: If no data is found for the specified filtration or the filter is invalid.


Models
Student_Progress

| Field           | Type         | Description                                           |
|-----------------|--------------|-------------------------------------------------------|
| `roll_no`       | Integer      | Unique identifier for the student (auto-generated)    |
| `name`          | String       | Name of the student                                   |
| `chemistry_mark`| Float        | Marks in Chemistry (0-100)                            |
| `physics_mark`  | Float        | Marks in Physics (0-100)                              |
| `maths_mark`    | Float        | Marks in Mathematics (0-100)                          |
| `gained_mark`   | Float        | Total marks obtained, calculated from subject marks   |
| `percentage`    | Float        | Percentage score based on total marks                 |
| `out_off`       | Integer      | Default total marks (300)                             |
| `class_teacher` | Foreign Key  | The teacher assigned to the class                     |
| `school`        | Foreign Key  | School where the student is enrolled                  |
| `department`    | Foreign Key  | Department associated with the student                |
| `created_at`    | DateTime     | Timestamp of record creation                          |
| `updated_at`    | DateTime     | Timestamp of last update                              |


# TEACHER APP
## Teacher API Endpoints

| Endpoint                                     | Method            | Description                                                                                                  |
|----------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------|
| `/api/teacher/`                              | GET, POST         | Retrieve a list of teachers or create a new teacher record.                                                  |
| `/api/teacher/<teacher_id>/`                 | GET, PUT, DELETE  | Retrieve, update, or delete a specific teacher by their ID.                                                  |
| `/api/teacher/sort_students/<teacher_name>/` | GET               | Retrieve details of students taught by a specific teacher.                                                   |
| `/api/teacher/teacher_sort_a_z/`             | GET               | Retrieve a list of teachers sorted alphabetically by name.                                                   |
| `/api/teacher/teacher_report/`               | GET               | Generate a report of performance for all teachers.                                                           |
| `/api/teacher/teacher_report/<teacher_name>/`| GET               | Retrieve a performance report for a specific teacher by name.                                                |
| `/api/teacher/best_teacher/`                 | GET               | Retrieve details of the best-performing teacher based on student performance metrics.                        |

---
### 1. / - List and Create Teachers
* URL: ```/app_teachers/```
* Method: GET, POST
        This endpoint allows for listing all teachers or creating a new teacher.
### Usage:
* GET ```/app_teachers/``` - Retrieves a list of all teachers.
* POST ```/app_teachers/``` - Creates a new teacher with the data provided in the request body.
* Response:
    - Status 200 (GET): Returns a list of all teachers.
    - Status 201 (POST): Returns the created teacher object upon successful creation.
    - Status 400: If the provided data for creation is invalid.
    - 
### 2. ```teacher/<int:teacher_id>/``` - Retrieve, Update, or Delete a Specific Teacher
* URL: ```/app_teachers/teacher/<teacher_id>/```
* Method: GET, PUT, DELETE
        This endpoint allows retrieval, updating, or deletion of a specific teacher by their teacher_id.
* URL Parameters:
    - ```teacher_id```: The unique ID of the teacher to retrieve, update, or delete.
### Usage:
* GET ```/app_teachers/teacher/<teacher_id>/``` - Retrieves details of a specific teacher.
* PUT ```/app_teachers/teacher/<teacher_id>/``` - Updates the teacher’s details with the data provided in the request body.
* DELETE```/app_teachers/teacher/<teacher_id>/```- Deletes the specified teacher.
* Response:
    - Status 200 (GET): Returns the teacher’s details.
    - Status 204 (DELETE): No content upon successful deletion.
    - Status 400 or 404: If the teacher is not found or if invalid data is provided for update.


### 3. sort_students/<str:teacher_name>/ - Retrieve Students Managed by a Specific Teacher
* URL: ```/app_teachers/sort_students/<teacher_name>/```
* Method: GET
        This endpoint retrieves all students associated with a specific teacher, identified by their teacher_name.
* URL Parameters:
    - ```teacher_name```: The name of the teacher for whom to retrieve student details.
### Usage:
* GET ```/app_teachers/sort_students/<teacher_name>/``` - Retrieves a list of students under the specified teacher.
* Response:
    - Status 200: Returns a list of students managed by the specified teacher.
    - Status 404: If no students are found under the specified teacher.


### 4. teacher_sort_a_z/ - Retrieve Students Sorted by Teacher Names (A-Z)
* URL: ```/app_teachers/teacher_sort_a_z/```
* Method: GET
        This endpoint returns a list of students sorted alphabetically by their teachers' names.
### Usage:
* GET ```/app_teachers/teacher_sort_a_z/``` - Retrieves a sorted list of students by teacher names.
* Response:
    - Status 200: Returns a list of students sorted by teacher names.
    - Status 404: If no students are found.

### 5. teacher_report/ - Retrieve Overall Teacher Performance Report
* URL: ```/app_teachers/teacher_report/```
* Method: GET
        This endpoint provides an overall performance report for all teachers, based on metrics like student performance.
### Usage:
* GET ```/app_teachers/teacher_report/``` - Retrieves the performance report for all teachers.
* Response:
    - Status 200: Returns the report with details on each teacher’s performance.
    - Status 404: If no data is available for the report.

### 6. teacher_report/<str:teacher_name>/ - Retrieve Report for a Specific Teacher
* URL: ```/app_teachers/teacher_report/<teacher_name>/```
* Method: GET
* Description: This endpoint provides a performance report for a specific teacher, identified by their teacher_name.
* URL Parameters:
    - teacher_name: The name of the teacher to retrieve the performance report for.
### Usage:
* GET ```/app_teachers/teacher_report/<teacher_name>/``` - Retrieves the performance report for the specified teacher.
* Response:
    - Status 200: Returns the report with details on the teacher’s performance.
    - Status 404: If no data is available for the specified teacher.

### 7. best_teacher/ - Retrieve the Best Performing Teacher
* URL: ```/app_teachers/best_teacher/```
* Method: GET
* Description: This endpoint identifies and returns the best performing teacher based on metrics such as student success rates and scores.
### Usage:
* GET ```/app_teachers/best_teacher/``` - Retrieves details of the best performing teacher.
* Response:
    - Status 200: Returns the teacher identified as the best performer.
    - Status 404: If no data is available to determine the best teacher.

## Teacher Model
| Field           | Type         | Description                                                   |
|-----------------|--------------|---------------------------------------------------------------|
| teacher_id      | Integer      | Unique identifier for the teacher (auto-generated)            |
| name            | String       | Name of the teacher                                           |
| department      | Foreign Key  | Department associated with the teacher                        |
| school          | Foreign Key  | School where the teacher is employed                          |
| performance_rate| Float        | Performance rating of the teacher based on student success    |
| created_at      | DateTime     | Timestamp of record creation                                  |
| updated_at      | DateTime     | Timestamp of last update                                      |


# Department APP

## Department API Endpoints

| Endpoint                                    | Method | Description                                                                                         |
|---------------------------------------------|--------|-----------------------------------------------------------------------------------------------------|
| `/app_departments/departments/`                         | GET, POST  | Retrieve all departments or create a new department.                                                |
| `/app_departments/department/<department_id>/`          | GET, PUT, DELETE | Retrieve, update, or delete a specific department by its ID.                                  |
| `/app_departments/department_filter/<department_id>/`   | GET    | Retrieve sorted or filtered department details based on specific criteria.                          |
| `/app_departments/department_teacher/<department_id>/`  | GET    | Retrieve teachers associated with a specific department.                                            |
| `/app_departments/department_student/<department_id>/`  | GET    | Retrieve students associated with a specific department.                                            |

---

## Endpoint Details

### 1. /departments/
- **Method**: `GET`, `POST`
- **Description**: List all departments or create a new department.
- **Usage**:
  - `GET /app_departments/departments/` - Lists all departments.
  - `POST /app_departments/departments/` - Creates a new department with data provided in the request.
- **Response**:
  - **Status 200** (GET): Returns a list of all departments.
  - **Status 201** (POST): Returns the created department object.
  - **Status 400**: Invalid data for department creation.

### 2. department/<department_id>/
- **Method**: `GET`, `PUT`, `DELETE`
- **Description**: Retrieve, update, or delete a specific department by its `department_id`.
- **Parameters**:
  - `department_id`: ID of the department to retrieve, update, or delete.
- **Usage**:
  - `GET /app_departments/department/<department_id>/` - Retrieve details of a specific department.
  - `PUT /app_departments/department/<department_id>/` - Update department details.
  - `DELETE /app_departments/department/<department_id>/` - Delete the specified department.
- **Response**:
  - **Status 200** (GET): Returns department details.
  - **Status 204** (DELETE): Successfully deleted.
  - **Status 400** or **404**: If the department is not found or if update data is invalid.

### 3. /department_filter/<department_id>/
- **Method**: `GET`
- **Description**: Retrieve filtered or sorted details of a department.
- **Parameters**:
  - `department_id`: ID of the department to filter or sort.
- **Usage**:
  - `GET /app_departments/department_filter/<department_id>/` - Retrieve filtered details for a department.
- **Response**:
  - **Status 200**: Returns filtered department data.
  - **Status 404**: If the department is not found.

### 4. department_teacher/<department_id>/
- **Method**: `GET`
- **Description**: Retrieve all teachers associated with a specific department.
- **Parameters**:
  - `department_id`: ID of the department to retrieve associated teachers.
- **Usage**:
  - `GET /app_departments/department_teacher/<department_id>/` - List all teachers in the department.
- **Response**:
  - **Status 200**: Returns a list of teachers in the specified department.
  - **Status 404**: If no teachers are found in the department.

### 5. department_student/<department_id>/
- **Method**: `GET`
- **Description**: Retrieve all students associated with a specific department.
- **Parameters**:
  - `department_id`: ID of the department to retrieve associated students.
- **Usage**:
  - `GET /app_departments/department_student/<department_id>/` - List all students in the department.
- **Response**:
  - **Status 200**: Returns a list of students in the specified department.
  - **Status 404**: If no students are found in the department.

## Department Model
| Field           | Type         | Description                                         |
|-----------------|--------------|-----------------------------------------------------|
| department_id   | Integer      | Unique identifier for the department (primary key)  |
| department_name            | String       | Name of the department                              |
| hod_name        | String       | Name of the Head of Department (HOD) (unique)       |
| school          | Foreign Key  | Reference to the school the department belongs to   |
| created_at      | DateTime     | Timestamp of record creation                        |
| updated_at      | DateTime     | Timestamp of last update                            |

# School APP
## School API Endpoints

| Endpoint                                     | Method | Description                                                                                             |
|----------------------------------------------|--------|---------------------------------------------------------------------------------------------------------|
| `/app_schools/school/`                               | GET, POST  | Retrieve a list of schools or create a new school record.                                                |
| `/api/school_details/<school_id>/`           | GET, PUT, DELETE | Retrieve, update, or delete a specific school by its ID.                                       |
| `/app_schools/school/departments/<school_id>/`       | GET    | Retrieve all departments associated with a specific school.                                              |
| `/app_schools/school/teachers/<school_id>/`          | GET    | Retrieve all teachers associated with a specific school.                                                 |
| `/app_schools/school/students/<school_id>/`          | GET    | Retrieve all students associated with a specific school.                                                 |

---

## Endpoint Details

### 1. `/app_schools/school/`
- **Method**: `GET`, `POST`
- **Description**: List all schools or create a new school.
- **Usage**:
  - `GET /app_schools/school/` - Retrieve a list of all schools.
  - `POST /app_schools/school/` - Create a new school record with the provided data.
- **Response**:
  - **Status 200** (GET): Returns a list of all school records.
  - **Status 201** (POST): Returns the created school object.
  - **Status 400**: Invalid data for school creation.

### 2. `/app_schools/school_details/<school_id>/`
- **Method**: `GET`, `PUT`, `DELETE`
- **Description**: Retrieve, update, or delete a specific school by its `school_id`.
- **Parameters**:
  - `school_id`: ID of the school to retrieve, update, or delete.
- **Usage**:
  - `GET /app_schools/school_details/<school_id>/` - Retrieve details of a specific school.
  - `PUT /app_schools/school_details/<school_id>/` - Update the details of the specified school.
  - `DELETE /app_schools/school_details/<school_id>/` - Delete the specified school.
- **Response**:
  - **Status 200** (GET): Returns school details.
  - **Status 204** (DELETE): Successfully deleted.
  - **Status 400** or **404**: If the school is not found or if update data is invalid.

### 3. `/app_schools/school/departments/<school_id>/`
- **Method**: `GET`
- **Description**: Retrieve all departments associated with a specific school.
- **Parameters**:
  - `school_id`: ID of the school to retrieve associated departments.
- **Usage**:
  - `GET /app_schools/school/departments/<school_id>/` - List all departments for the specified school.
- **Response**:
  - **Status 200**: Returns a list of departments for the school.
  - **Status 404**: If no departments are found for the school.

### 4. `/app_schools/school/teachers/<school_id>/`
- **Method**: `GET`
- **Description**: Retrieve all teachers associated with a specific school.
- **Parameters**:
  - `school_id`: ID of the school to retrieve associated teachers.
- **Usage**:
  - `GET /app_schools/school/teachers/<school_id>/` - List all teachers for the specified school.
- **Response**:
  - **Status 200**: Returns a list of teachers for the school.
  - **Status 404**: If no teachers are found for the school.

### 5. `/app_schools/school/students/<school_id>/`
- **Method**: `GET`
- **Description**: Retrieve all students associated with a specific school.
- **Parameters**:
  - `school_id`: ID of the school to retrieve associated students.
- **Usage**:
  - `GET /app_schools/school/students/<school_id>/` - List all students for the specified school.
- **Response**:
  - **Status 200**: Returns a list of students for the school.
  - **Status 404**: If no students are found for the school.
