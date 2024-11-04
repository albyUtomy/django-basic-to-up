# API Documentation

## Overview
This document provides the details of the API endpoints available for managing students, teachers, departments, and schools in the application.

---

## Summary of Endpoints

| S.No | Endpoint URL                                      | Method | Description                                                 |
|------|--------------------------------------------------|--------|-------------------------------------------------------------|
| 1    | `/app_students/students/`                        | GET    | Retrieve all students for a specific school.               |
| 2    | `/app_students/students/<roll_no>/`             | GET    | Retrieve details of a specific student.                    |
| 3    | `/app_students/students/`                        | POST   | Create a new student record.                               |
| 4    | `/app_students/students/<roll_no>/`             | PUT    | Update details for a specific student.                     |
| 5    | `/app_students/students/<roll_no>/`             | DELETE | Delete a specific student.                                 |
| 6    | `/app_students/statics/<str:filtration>/`       | GET    | Get student statistics based on filtration.                |
| 7    | `/app_teachers/`                                 | GET    | Retrieve all teachers.                                     |
| 8    | `/app_teachers/teacher/<int:teacher_id>/`       | GET    | Retrieve details of a specific teacher.                    |
| 9    | `/app_teachers/`                                 | POST   | Create a new teacher record.                               |
| 10   | `/app_teachers/teacher/<int:teacher_id>/`       | PUT    | Update details for a specific teacher.                     |
| 11   | `/app_teachers/teacher/<int:teacher_id>/`       | DELETE | Delete a specific teacher.                                 |
| 12   | `/app_departments/`                              | GET    | Retrieve all departments.                                   |
| 13   | `/app_departments/department/<int:department_id>/` | GET  | Retrieve details of a specific department.                 |
| 14   | `/app_departments/`                              | POST   | Create a new department record.                            |
| 15   | `/app_departments/department/<int:department_id>/` | PUT  | Update details for a specific department.                  |
| 16   | `/app_departments/department/<int:department_id>/` | DELETE | Delete a specific department.                               |
| 17   | `/app_schools/`                                  | GET    | Retrieve all schools.                                      |
| 18   | `/app_schools/school_details/<int:school_id>/`  | GET    | Retrieve details of a specific school.                     |
| 19   | `/app_schools/`                                  | POST   | Create a new school record.                                |
| 20   | `/app_schools/school_details/<int:school_id>/`  | PUT    | Update details for a specific school.                      |
| 21   | `/app_schools/school_details/<int:school_id>/`  | DELETE | Delete a specific school.                                  |

---

## Detailed API Endpoints

### 1. Retrieve All Students
- **URL**: `/app_students/students/`
- **Method**: `GET`
- **Description**: Retrieve all students for a specific school.
- **Query Parameters**: 
  - `school_id`: The ID of the school.
- **Response**:
  - **Status 200**: 
    ```json
    {
      "Students": [
        {
          "roll_no": 1,
          "name": "STUA",
          "percentage": 75,
          "gained_mark": 240,
          "out_off": 300
        }
      ]
    }
    ```
  - **Status 404**: 
    ```json
    {
      "message": "Students not found"
    }
    ```

### 2. Retrieve a Specific Student
- **URL**: `/app_students/students/<roll_no>/`
- **Method**: `GET`
- **Description**: Retrieve details of a specific student.
- **Response**:
  - **Status 200**: 
    ```json
    {
      "roll_no": 1,
      "name": "STUA",
      "percentage": 75,
      "gained_mark": 240,
      "out_off": 300
    }
    ```
  - **Status 404**: 
    ```json
    {
      "message": "Student not found"
    }
    ```

### 3. Create a New Student
- **URL**: `/app_students/students/`
- **Method**: `POST`
- **Description**: Create a new student record.
- **Request Body**:
  ```json
  {
    "name": "STUA",
    "chemistry_mark": 85,
    "physics_mark": 90,
    "maths_mark": 80,
    "class_teacher_id": 1,
    "school_id": 1,
    "department_id": 1
  }

Response:
Status 201:
json
Copy code
{
  "message": "Student created successfully"
}
Status 400:
json
Copy code
{
  "error": "Invalid data"
}
4. Update a Student Record
URL: /app_students/students/<roll_no>/
Method: PUT
Description: Updates details for a specific student.
Request Body:
json
Copy code
{
  "chemistry_mark": 90.0,
  "physics_mark": 85.0,
  "maths_mark": 88.0
}
Response:
Status 200:
json
Copy code
{
  "message": "Student updated successfully"
}
Status 404:
json
Copy code
{
  "message": "Student not found"
}
5. Delete a Specific Student
URL: /app_students/students/<roll_no>/
Method: DELETE
Description: Delete a specific student.
Response:
Status 204:
json
Copy code
{
  "message": "Student deleted successfully"
}
Status 404:
json
Copy code
{
  "message": "Student not found"
}
6. Get Student Statistics
URL: /app_students/statics/<str:filtration>/
Method: GET
Description: Get student statistics based on filtration (e.g., average marks, top 5 students).
Response:
Status 200:
json
Copy code
{
  "average": 80,
  "top_5": [
    { "name": "STUA", "percentage": 90 }
  ],
  "failed": [
    { "name": "FAIL", "percentage": 40 }
  ]
}
Status 400:
json
Copy code
{
  "message": "Invalid filtration type"
}
7. Retrieve All Teachers
URL: /app_teachers/
Method: GET
Description: Retrieve all teachers.
Response:
Status 200:
json
Copy code
{
  "teachers": [
    {
      "id": 1,
      "name": "John Doe",
      "performance_rate": 8
    }
  ]
}
Status 404:
json
Copy code
{
  "message": "No teachers found"
}
8. Retrieve a Specific Teacher
URL: /app_teachers/teacher/<int:teacher_id>/
Method: GET
Description: Retrieve details of a specific teacher.
Response:
Status 200:
json
Copy code
{
  "id": 1,
  "name": "John Doe",
  "performance_rate": 8
}
Status 404:
json
Copy code
{
  "message": "Teacher not found"
}
9. Create a New Teacher
URL: /app_teachers/
Method: POST
Description: Create a new teacher record.
Request Body:
json
Copy code
{
  "name": "Jane Smith",
  "department_id": 1
}
Response:
Status 201:
json
Copy code
{
  "message": "Teacher created successfully"
}
Status 400:
json
Copy code
{
  "error": "Invalid data"
}
10. Update a Teacher Record
URL: /app_teachers/teacher/<int:teacher_id>/
Method: PUT
Description: Update details for a specific teacher.
Request Body:
json
Copy code
{
  "name": "Jane Doe"
}
Response:
Status 200:
json
Copy code
{
  "message": "Teacher updated successfully"
}
Status 404:
json
Copy code
{
  "message": "Teacher not found"
}
11. Delete a Specific Teacher
URL: /app_teachers/teacher/<int:teacher_id>/
Method: DELETE
Description: Delete a specific teacher.
Response:
Status 204:
json
Copy code
{
  "message": "Teacher deleted successfully"
}
Status 404:
json
Copy code
{
  "message": "Teacher not found"
}
12. Retrieve All Departments
URL: /app_departments/
Method: GET
Description: Retrieve all departments.
Response:
Status 200:
json
Copy code
{
  "departments": [
    {
      "department_id": 1,
      "name": "Science"
    }
  ]
}
Status 404:
json
Copy code
{
  "message": "No departments found"
}
13. Retrieve a Specific Department
URL: /app_departments/department/<int:department_id>/
Method: GET
Description: Retrieve details of a specific department.
Response:
Status 200:
json
Copy code
{
  "department_id": 1,
  "name": "Science"
}
Status 404:
json
Copy code
{
  "message": "Department not found"
}
14. Create a New Department
URL: /app_departments/
Method: POST
Description: Create a new department record.
Request Body:
json
Copy code
{
  "name": "Arts"
}
Response:
Status 201:
json
Copy code
{
  "message": "Department created successfully"
}
Status 400:
json
Copy code
{
  "error": "Invalid data"
}
15. Update a Department Record
URL: /app_departments/department/<int:department_id>/
Method: PUT
Description: Update details for a specific department.
Request Body:
json
Copy code
{
  "name": "Arts and Humanities"
}
Response:
Status 200:
json
Copy code
{
  "message": "Department updated successfully"
}
Status 404:
json
Copy code
{
  "message": "Department not found"
}
16. Delete a Specific Department
URL: /app_departments/department/<int:department_id>/
Method: DELETE
Description: Delete a specific department.
Response:
Status 204:
json
Copy code
{
  "message": "Department deleted successfully"
}
Status 404:
json
Copy code
{
  "message": "Department not found"
}
17. Retrieve All Schools
URL: /app_schools/
Method: GET
Description: Retrieve all schools.
Response:
Status 200:
json
Copy code
{
  "schools": [
    {
      "school_id": 1,
      "name": "ABC High School",
      "address": "123 Main St",
      "created": "2023-01-01T00:00:00Z",
      "updated": "2023-01-01T00:00:00Z"
    }
  ]
}
Status 404:
json
Copy code
{
  "message": "No schools found"
}
18. Retrieve a Specific School
URL: /app_schools/school_details/<int:school_id>/
Method: GET
Description: Retrieve details of a specific school.
Response:
Status 200:
json
Copy code
{
  "school_id": 1,
  "name": "ABC High School",
  "address": "123 Main St",
  "created": "2023-01-01T00:00:00Z",
  "updated": "2023-01-01T00:00:00Z"
}
Status 404:
json
Copy code
{
  "message": "School not found"
}
19. Create a New School
URL: /app_schools/
Method: POST
Description: Create a new school record.
Request Body:
json
Copy code
{
  "name": "XYZ High School",
  "address": "456 Elm St"
}
Response:
Status 201:
json
Copy code
{
  "message": "School created successfully"
}
Status 400:
json
Copy code
{
  "error": "Invalid data"
}
20. Update a School Record
URL: /app_schools/school_details/<int:school_id>/
Method: PUT
Description: Update details for a specific school.
Request Body:
json
Copy code
{
  "name": "XYZ High School Updated",
  "address": "789 Oak St"
}
Response:
Status 200:
json
Copy code
{
  "message": "School updated successfully"
}
Status 404:
json
Copy code
{
  "message": "School not found"
}
21. Delete a Specific School
URL: /app_schools/school_details/<int:school_id>/
Method: DELETE
Description: Delete a specific school.
Response:
Status 204:
json
Copy code
{
  "message": "School deleted successfully"
}
Status 404:
json
Copy code
{
  "message": "School not found"
}