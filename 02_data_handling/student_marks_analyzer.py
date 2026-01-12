def collect_student_data():
    students = {}

    while True:
        name = input("Enter the name of student or done for exit : ").strip()

        if name.lower() == "done":
            break
        if name.lower() in students:
            print("Student Already Present!")
            continue
        
        try:
            marks = float(input(f"Enter Marks for {name} : "))
            students[name] = marks
        except ValueError:
            print("Invalid input!")
    return students

def display_report(students):
    if not students:
        print("No students data!")
        return
    marks = list(students.values())
    max_marks = max(marks)
    min_marks = min(marks)
    average_marks = sum(marks)/len(marks)
    topper = [name for name, score in students.items() if score == max_marks]
    bottomer = [name for name, score in students.items() if score == min_marks]
    
    print("-"*30)
    print("\nStudents Marks Report 📅")
    print(f"Total Students : {len(students)}")
    print(f"Average Marks for students : {average_marks:.2f}")
    print(f"Highest Marks : {max_marks} by {', '.join(topper)}")
    print(f"Lowest Marks : {min_marks} by {', '.join(bottomer)}")
    print("-"*30)
    print("Detailed Marks 📘")
    for name, score in students.items():
        print(f" - {name}: {score}")

data = collect_student_data()
display_report(data)
