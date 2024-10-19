
# function to return the percentage of given parameter
def get_percentage(*args, **kwargs):
    if args:
        total_marks = sum(args)
        total_possible = kwargs.get('total_possible', 100)
        return (total_marks/total_possible) * 100
    else:
        return 0
    
def get_average(numbers:list)->float:
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)