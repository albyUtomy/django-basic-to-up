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
    """function to return the performance statics of each teacher
        this function take database object, and list of top_10 gained_mark as parameter.
        to find the best teacher the criterions are:
            most number of passed student
            most number of students in the top 10 list
            top10 ratio
            performance_rate is calculated out-off 10
            by using this formula :
                (success_score_out_of_10 + top10_score_out_of_10)/2
    """

    # Define the passing criteria
    total_student = student_data.count()
    passing_criteria = Q(chemistry_mark__gte=40) & Q(physics_mark__gte=40) & Q(maths_mark__gte=40)
    passed_students = student_data.filter(passing_criteria).count()
    failed_student = total_student - passed_students


    success_rate = (passed_students / total_student * 100) if total_student > 0 else 0
    success_score_out_of_10 = (success_rate / 100) * 10

    no_top10 = sum(1 for student in top_10 if student.class_teacher_id == student_data.first().class_teacher_id)

    top10_ratio = (no_top10 / total_student) if total_student > 0 else 0
    top10_score_out_of_10 = (top10_ratio) * 10
    
    performance_points = (success_score_out_of_10 + top10_score_out_of_10) / 2

    
    analysis = {
        'teacher_name': student_data.first().class_teacher_id.name,
        'total_students' : total_student,
        'passed_students' : passed_students,
        'failed_students' : failed_student,
        'number_top_10' : no_top10,
        'performance_rate_out_of_10':performance_points
    }

    return analysis
    
    