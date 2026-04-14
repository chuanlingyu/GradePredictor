from src.utils.course_loader import extract_info

"""
Current plan: Using the College to predict, assuming the instructor exists
Future plan: If have specific course, use the specific course to predict
    Add the option of not having the instructor.
"""

def space():
    print('--' * 10)
    print()

def main():
    print("""
We will first ask the courses you want to take NEXT semester.
Then we will ask your grade from PAST courses.
We will ask the course, your grade (for past courses), and your instructor.
When inputing your courses, please follow the format of:
    'course abbreviation' 'Course number'
    Ex: 'CS 173' 'MATH 241'
    
Input AS MUCH past grades from previous courses as you can as that 
we can predict better.
    """)

    # STUDENT INPUT DATA

    # List with dictionary inside, each map to course name, subject, subject number, instructor last name, and grade.
    # Ex: {"Course": "CS 124", "Subject": "CS", "Number": "124", "instructor": "Challen", "Grade": "A"},
    student_history = [] 

    # List with dictionary inside, each map to course name, subject, subject number, and instructor last name
    # Ex: {"Course": "CS 128", "Subject": "CS", "Number": "128", "Instructor"}
    target_courses = []


    print("We will begin with your past courses:\n")
    space()

    while True:
        # Ask for course and break up
        course = input('Enter your past course: ').strip().upper()
        if course.lower() == 'done':
            break;
        list = course.split(' ')
        if len(list) == 1:
            print("Need to have space between!")
            space()
            continue
        else:
            subject = list[0].upper()
            number = list[1]
        instructor = input('What is your instructor\'s last name: ').upper()

        features = extract_info(subject, number, instructor)
        if features == None:
            continue

        student_history.append(features)

    # Now ask for user targetted in
    # while True:


if __name__ == "__main__":
    main()