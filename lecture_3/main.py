def add_student(s_name, studs):
    for student in studs:
        if student["name"] == s_name:
            print(f'Student {s_name} already exists')
            return False
    studs.append({
        "name":s_name,
        "grades": []
    })
    print('Student succesfully added!')

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

while command != 5:
    if command == 1:
        name = input('Enter student name: ').capitalize()
        add_student(name, students)
        

    






    command = 0
    print(menu_txt, end = '')
    while command == 0:
        try:
            command = int(input())
        except ValueError:
            print("Enter a number: ", end = '')

