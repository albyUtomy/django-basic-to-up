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



def teacher_analysis(db):
    """function to return the performance statics of each teacher 
        and best among them.
        this function take database as parameter.
        to find the best teacher the criterions are:
            most number of passed student
            most number of students in the top 10 list
    """

    # Define the passing criteria
    passing_criteria = Q(chemistry_mark__gte=40) & Q(physics_mark__gte=40) & Q(maths_mark__gte=40)
    
    
    # Group by teacher and annotate with counts of passed and failed students
    teacher_stats = (
        db.objects
        .values('class_teacher')
        .annotate(
            passed_count=Count('roll_no', filter=passing_criteria),
            failed_count=Count('roll_no') - Count('roll_no', filter=passing_criteria)
        )
    )
    
    # Report
    report = []
    for teacher in teacher_stats:
        total_students = teacher['passed_count'] + teacher['failed_count']
        success_rate = (teacher['passed_count'] / total_students * 100) if total_students > 0 else 0
        
        report.append({
            'teacher_name': teacher['class_teacher'],
            'total_student':teacher['passed_count']+teacher['failed_count'],
            'passed_students': teacher['passed_count'],
            'failed_students': teacher['failed_count'],
            'success_rate': round(success_rate, 2)
        })
    
    # Counting number of passed students
    passed_students = db.objects.filter(passing_criteria)
    
    # Calculate top 10 students per teacher based on gained marks
    top_students = passed_students.order_by('-gained_mark')[:10]
    top_students_counts = top_students.values('class_teacher').annotate(
        top_count=Count('roll_no')
    )
    
    # Combine stats into a single dictionary for best teacher
    teacher_scores = {}
    for teacher in teacher_stats:
        teacher_scores[teacher['class_teacher']] = {
            'passed_count': teacher['passed_count'],
            'top_count': 0
        }

    for top_student in top_students_counts:
        if top_student['class_teacher'] in teacher_scores:
            teacher_scores[top_student['class_teacher']]['top_count'] += top_student['top_count']
    
    # Find the best teacher based on the criteria
    best_teacher = max(teacher_scores.items(), key=lambda x: (x[1]['passed_count'], x[1]['top_count']))
    
    return {
        'best_teacher': {
            'teacher_name': best_teacher[0],
            'passed_count': best_teacher[1]['passed_count'],
            'top_10_count': best_teacher[1]['top_count']
        },
        'teacher_reports': report
    }

