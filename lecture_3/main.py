def add_student(s_name, studs):
    '''Adding new students
    
    This function adding new students to the base 
    and creates poles with grades for them'''
    for student in studs:
        if student["name"] == s_name:
            print(f'Student {s_name} already exists')
            return False
    studs.append({
        "name":s_name,
        "grades": []
    })
    print('Student succesfully added!\n')


def add_grade(s_name, studs):
    '''Adding grades
    
    This function adding grades for students
    that already exists in the base and telling user
    if they are not'''
    for student in studs:
        
        if student["name"] == s_name:
            grade = input('Enter a grade, or "done" to finish: ')

            while grade != 'done':
                correct = False
                while correct == False:
                    try: 
                        grade = int(grade)
                        correct = True
                    except ValueError:
                        grade = int(input("Invalid input. Please enter a number: "))
                
                if 0<=grade<=100:
                    student["grades"].append(grade)
                    grade = input('Enter a grade, or "done" to finish: ')
                else: grade = input("Grade out of range. Input grade from 0 to 100: ")
            return False  
        
    print("The student isn't in the base yet\n")
    return False

  
def count_avg(studs):
    '''This function counts average grades for students
    
    Function counting max average, min average and globak average 
    grades if the student has grades in the base'''
    avg_grades = []
    counter = 0
    if len(studs) == 0:
        print("There's no students in the base\n")
        return False
    for student in studs:
        try:
            avg_grade = sum(student["grades"])/len(student["grades"])
            print(f"{student["name"]}'s average grade is {format(avg_grade, '.1f')}")
            avg_grades.append(avg_grade)
        except ZeroDivisionError:
            print(f"{student["name"]}'s average grade is N/A")
    print("--------------------------------")
    print(f"Max Average: {format(max(avg_grades), '.1f')}\nMin Average: {format(min(avg_grades), '.1f')}\nAverall Average: {format(sum(avg_grades)/len(avg_grades), '.1f')}\n")

def searching_max_avg(studs):
    '''Function searchs for max average frade
    
    Search for the max average grade between all students that has grades,
    using lambda to do it'''
    highest_grade = 0
    avg_grades = []
    counter = 0
    if len(studs) == 0:
        print("There's no students in the base\n")
        return False
    
    for student in studs:
        try:
            avg_grade = lambda student: sum(student["grades"])/len(student["grades"])

            if avg_grade(student) > highest_grade:
                highest_grade = avg_grade(student)
                max_grade_student = student["name"]

        except ZeroDivisionError:
            pass

    print(f"The student with highest average is {max_grade_student} with a grade of {format(highest_grade, '.1f')}\n")

            
students = []
menu_txt = '''--- Student Grade Analyzer ---
1. Add a new student
2. Add grades for a student
3. Generate a full report
4. Find top performer
5. Exit
Enter your choise: '''

command = 0
print(menu_txt, end = '')
while command == 0:
    try:
        command = int(input())
    except ValueError:
        print("Enter a number: ", end = '')
# Menu
while command != 5:
    if command == 1:
        name = input('Enter student name: ').capitalize()
        add_student(name, students)
    if command == 2:
        assessed = input('Enter student name, to add his grades: ').capitalize()
        add_grade(assessed, students)
    if command == 3:
        print("--- Student Report ---")
        count_avg(students)
    if command == 4:
        searching_max_avg(students)

    command = 0
    print(menu_txt, end = '')
    while command == 0:
        try:
            command = int(input())
        except ValueError:
            print("Enter a number: ", end = '')

