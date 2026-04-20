from src.utils.course_loader import extract_info

"""
Working Plan: Work on getting grade
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
            subject = list[0]
            number = list[1]
            
        instructor = input('What is your instructor\'s last name: ').strip().upper()

        features = extract_info(subject, number, instructor)
        if features == None:
            continue

        student_history.append(features)


        grade = input('What is your grade in that class in letter grade: ').strip.().upper()

        grade_to_gpa = {
            "A+": 4.0,
            "A": 4.0,
            "A-": 3.7,
            "B+": 3.3,
            "B": 3.0,
            "B-": 2.7,
            "C+": 2.3,
            "C": 2.0,
            "C-": 1.7,
            "D+": 1.3,
            "D": 1.0,
            "D-": 0.7,
            "F": 0.0
        }

        grade = grade_to_gpa.get(grade)

        space()

    print('Now we will ask for the courses you want to take')

    # Now ask for user targetted in
    while True:
        course = input('Enter the course you want to take: ').strip().upper()
        if course.lower() == 'done':
            break
        list = course.split(' ')
        if len(list) == 1:
            print("Need to have space between!")
            space()
            continue
        else:
            subject = list[0]
            number = list[1]

        instructor = input('What is the instructor\'s last name: ').upper()

        features = extract_info(subject, number, instructor)
        if features == None:
            continue

        student_history.append(features)
        space()


if __name__ == "__main__":
    main()