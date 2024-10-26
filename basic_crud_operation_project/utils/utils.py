from django.db.models import Count, Q


# function to return the percentage of given parameter
def get_percentage(*args, **kwargs):
    if args:
        total_marks = sum(args)
        total_possible = kwargs.get('total_possible', 100)
        return (total_marks/total_possible) * 100
    else:
        return 0
    
# find the average parameter is list
def get_average(numbers:list)->float:
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)



def teacher_analysis(student_data, top_10):
    """function to return the performance statics of each teacher.
    This function takes a database object and a list of top 10 gained marks as parameters.
    To find the best teacher, the criteria are:
        - Most number of passed students.
        - Most number of students in the top 10 list.
        - Top 10 ratio.
        - Performance rate is calculated out of 10 using the formula:
            (success_score_out_of_10 + top10_score_out_of_10)/2.
    """
    
    # Define the passing criteria
    total_student = student_data.count()
    passing_criteria = Q(chemistry_mark__gte=40) & Q(physics_mark__gte=40) & Q(maths_mark__gte=40)
    passed_students = student_data.filter(passing_criteria).count()
    failed_students = total_student - passed_students

    # Calculate success rate and score
    success_rate = (passed_students / total_student * 100) if total_student > 0 else 0
    success_score_out_of_10 = (success_rate / 100) * 10

    # Get the first student safely to avoid NoneType errors
    first_student = student_data.first()

    if first_student:
        no_top10 = sum(1 for student in top_10 if student.class_teacher_id == first_student.class_teacher_id)
        teacher_name = first_student.class_teacher_id.name
    else:
        no_top10 = 0
        teacher_name = "Unknown"  # Fallback in case no students are found

    # Calculate top 10 ratio and score
    top10_ratio = (no_top10 / total_student) if total_student > 0 else 0
    top10_score_out_of_10 = top10_ratio * 10
    
    # Calculate performance points
    performance_points = (success_score_out_of_10 + top10_score_out_of_10) / 2

    # Prepare the analysis report
    analysis = {
        'teacher_name': teacher_name,
        'total_students': total_student,
        'passed_students': passed_students,
        'failed_students': failed_students,
        'number_top_10': no_top10,
        'performance_rate_out_of_10': performance_points,
    }

    return analysis

def get_best_value(model):
    highest = model.objects.order_by('-performance_rate').first()
    print(highest)
    return highest

def assign_hod_name(department_instance_in, teacher_instance):
    """
    Sets the highest-performing teacher as the head of department (`hod_name`).
    Clears conflicting `hod_name` assignments from other departments.
    """
    
    # Find the best-performing teacher in the department
    best_teacher = teacher_instance.__class__.objects.filter(
        department_id=department_instance_in
    ).order_by('-performance_rate').first()

    if best_teacher:
        # Clear conflicting `hod_name` assignments from other departments
        conflicting_departments = department_instance_in.__class__.objects.filter(
            hod_name=best_teacher
        ).exclude(pk=department_instance_in.pk)
        
        for conflict in conflicting_departments:
            conflict.hod_name = None
            conflict.save()

        # Set the `hod_name` if it’s different from the current one
        if department_instance_in.hod_name != best_teacher:
            department_instance_in.hod_name = best_teacher
            department_instance_in.save()  # Ensure the change is saved