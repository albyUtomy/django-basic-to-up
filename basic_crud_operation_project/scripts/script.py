from app_progress_student.models import *
# from utils.utils import teacher_analysis
from app_progress_student.models import Teacher
from app_department.models import Department
import random


def run():
    students = [
        {
            "name": "Aarav Nair",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 85,
            "physics_mark": 90,
            "maths_mark": 88
        },
        {
            "name": "Veer Malhotra",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 78,
            "physics_mark": 82,
            "maths_mark": 80
        },
        {
            "name": "Aanya Nair",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 92,
            "physics_mark": 94,
            "maths_mark": 89
        },
        {
            "name": "Reyansh Kumar",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 70,
            "physics_mark": 72,
            "maths_mark": 75
        },
        {
            "name": "Aditya Sharma",
            "class_teacher": "Johnson",
            "chemistry_mark": 88,
            "physics_mark": 85,
            "maths_mark": 90
        },
        {
            "name": "Dhruv Iyer",
            "class_teacher": "Johnson",
            "chemistry_mark": 95,
            "physics_mark": 93,
            "maths_mark": 96
        },
        {
            "name": "Kavya Singh",
            "class_teacher": "Johnson",
            "chemistry_mark": 79,
            "physics_mark": 76,
            "maths_mark": 77
        },
        {
            "name": "Arjun Verma",
            "class_teacher": "Johnson",
            "chemistry_mark": 38, 
            "physics_mark": 40,
            "maths_mark": 35
        },
        {
            "name": "Vanya Das",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 90,
            "physics_mark": 92,
            "maths_mark": 95
        },
        {
            "name": "Riya Singh",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 86,
            "physics_mark": 88,
            "maths_mark": 84
        },
        {
            "name": "Maanvi Gupta",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 82,
            "physics_mark": 81,
            "maths_mark": 85
        },
        {
            "name": "Pranav Reddy",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 55,  
            "physics_mark": 58,
            "maths_mark": 57
        },
        {
            "name": "Anaya Rathi",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 75,
            "physics_mark": 78,
            "maths_mark": 76
        },
        {
            "name": "Shivansh Roy",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 80,
            "physics_mark": 84,
            "maths_mark": 82
        },
        {
            "name": "Shanaya Desai",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 70,
            "physics_mark": 72,
            "maths_mark": 68
        },
        {
            "name": "Rohit Kaur",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 41,  
            "physics_mark": 43,
            "maths_mark": 39
        },
        {
            "name": "Divyansh Patil",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 88,
            "physics_mark": 92,
            "maths_mark": 89
        },
        {
            "name": "Kriti Mehta",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 83,
            "physics_mark": 87,
            "maths_mark": 85
        },
        {
            "name": "Kabir Anand",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 95,
            "physics_mark": 91,
            "maths_mark": 93
        },
        {
            "name": "Nikhil Sen",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 44,  
            "physics_mark": 47,
            "maths_mark": 43
        },
        {
            "name": "Siddharth Khanna",
            "class_teacher": "Johnson",
            "chemistry_mark": 92,
            "physics_mark": 90,
            "maths_mark": 94
        },
        {
            "name": "Tanvi Kapoor",
            "class_teacher": "Johnson",
            "chemistry_mark": 79,
            "physics_mark": 78,
            "maths_mark": 80
        },
        {
            "name": "Arnav Bansal",
            "class_teacher": "Johnson",
            "chemistry_mark": 70,
            "physics_mark": 68,
            "maths_mark": 72
        },
        {
            "name": "Karan Joshi",
            "class_teacher": "Johnson",
            "chemistry_mark": 33,  
            "physics_mark": 36,
            "maths_mark": 30
        },
        {
            "name": "Gaurav Yadav",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 87,
            "physics_mark": 85,
            "maths_mark": 88
        },
        {
            "name": "Reema Sharma",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 84,
            "physics_mark": 86,
            "maths_mark": 90
        },
        {
            "name": "Manish Chaudhary",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 72,
            "physics_mark": 70,
            "maths_mark": 75
        },
        {
            "name": "Anil Agarwal",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 39,  
            "physics_mark": 40,
            "maths_mark": 37
        },
        {
            "name": "Diya Menon",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 91,
            "physics_mark": 89,
            "maths_mark": 94
        },
        {
            "name": "Krishna Rao",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 81,
            "physics_mark": 80,
            "maths_mark": 82
        },
        {
            "name": "Raghav Gupta",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 73,
            "physics_mark": 75,
            "maths_mark": 70
        },
        {
            "name": "Niranjan Bhat",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 42,  
            "physics_mark": 39,
            "maths_mark": 40
        },
        {
            "name": "Aditi Singh",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 88,
            "physics_mark": 90,
            "maths_mark": 92
        },
        {
            "name": "Bharat Desai",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 75,
            "physics_mark": 70,
            "maths_mark": 72
        },
        {
            "name": "Sunil Patil",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 81,
            "physics_mark": 85,
            "maths_mark": 78
        },
        {
            "name": "Shivani Kumar",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 34,  
            "physics_mark": 37,
            "maths_mark": 36
        },
        {
            "name": "Deepak Mishra",
            "class_teacher": "Johnson",
            "chemistry_mark": 90,
            "physics_mark": 92,
            "maths_mark": 88
        },
        {
            "name": "Gaurav Agarwal",
            "class_teacher": "Johnson",
            "chemistry_mark": 82,
            "physics_mark": 85,
            "maths_mark": 80
        },
        {
            "name": "Ritesh Singh",
            "class_teacher": "Johnson",
            "chemistry_mark": 88,
            "physics_mark": 87,
            "maths_mark": 84
        },
        {
            "name": "Priya Iyer",
            "class_teacher": "Johnson",
            "chemistry_mark": 30,  
            "physics_mark": 32,
            "maths_mark": 28
        },
        {
            "name": "Anushka Verma",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 85,
            "physics_mark": 90,
            "maths_mark": 87
        },
        {
            "name": "Ravi Saini",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 91,
            "physics_mark": 85,
            "maths_mark": 90
        },
        {
            "name": "Sonam Bhatt",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 88,
            "physics_mark": 84,
            "maths_mark": 89
        },
        {
            "name": "Ajay Rawat",
            "class_teacher": "Rupkumar",
            "chemistry_mark": 41,  
            "physics_mark": 43,
            "maths_mark": 38
        },
        {
            "name": "Neha Rathi",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 86,
            "physics_mark": 84,
            "maths_mark": 88
        },
        {
            "name": "Karan Kumar",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 79,
            "physics_mark": 76,
            "maths_mark": 80
        },
        {
            "name": "Mohit Sethi",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 93,
            "physics_mark": 91,
            "maths_mark": 95
        },
        {
            "name": "Nisha Yadav",
            "class_teacher": "Rupeesh",
            "chemistry_mark": 36,  
            "physics_mark": 32,
            "maths_mark": 35
        },
        {
            "name": "Rajesh Sharma",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 87,
            "physics_mark": 88,
            "maths_mark": 90
        },
        {
            "name": "Tanmay Saini",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 81,
            "physics_mark": 85,
            "maths_mark": 83
        },
        {
            "name": "Sakshi Singh",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 93,
            "physics_mark": 89,
            "maths_mark": 91
        },
        {
            "name": "Kriti Malhotra",
            "class_teacher": "Radhakrishnan",
            "chemistry_mark": 42,  
            "physics_mark": 40,
            "maths_mark": 38
        },
        {
            "name": "Riya Iyer",
            "class_teacher": "Johnson",
            "chemistry_mark": 89,
            "physics_mark": 91,
            "maths_mark": 87
        },
        {
            "name": "Neel Patel",
            "class_teacher": "Johnson",
            "chemistry_mark": 80,
            "physics_mark": 85,
            "maths_mark": 82
        },
        {
            "name": "Deepika Roy",
            "class_teacher": "Johnson",
            "chemistry_mark": 92,
            "physics_mark": 90,
            "maths_mark": 94
        },
        {
            "name": "Manish Gupta",
            "class_teacher": "Johnson",
            "chemistry_mark": 39,  
            "physics_mark": 38,
            "maths_mark": 36
        }]

# Define possible values for class_teacher_id, school_id, department_id
    class_teacher_ids = [100, 101, 102, 103]
    school_ids = [1, 2]
    department_ids = [10, 20, 30, 40, 50]

    # Function to randomly assign class_teacher_id, school_id, department_id
    def assign_random_ids(student):
        student["class_teacher_id"] = random.choice(class_teacher_ids)
        student["school_id"] = random.choice(school_ids)
        student["department_id"] = random.choice(department_ids)
        return student

# Update each student record
    students_with_ids = [assign_random_ids(student) for student in students]

    # Print updated dataset
    for student in students_with_ids:
        print(student)