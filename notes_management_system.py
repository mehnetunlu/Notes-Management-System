import json

student_info = {
    "username": "mehmet",
    "password": "12345"
}

def load_grades():
    try:
        with open('grades.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_grades(grades):
    with open('grades.json', 'w') as f:
        json.dump(grades, f)

def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == student_info["username"] and password == student_info["password"]:
            print("Successful login.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect credentials. {attempts} attempts remaining.")
    print("Too many failed login attempts. Exiting...")
    return False

def add_notes(grades):
    course_name = input("Enter the course name: ")
    course_notes = []
    while True:
        try:
            grade = int(input(f"Enter a grade for {course_name} (or type -1 to stop): "))
            if grade == -1:
                break
            course_notes.append(grade)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if course_name in grades:
        grades[course_name].extend(course_notes)
    else:
        grades[course_name] = course_notes
    save_grades(grades)
    print(f"Grades added for {course_name}!")

def calculate_average(grades):
    if not grades:
        print("No grades entered yet.")
        return
    
    overall_total = 0
    overall_count = 0
    for course, course_grades in grades.items():
        course_average = sum(course_grades) / len(course_grades)
        print(f"Average for {course}: {course_average:.2f}")
        overall_total += sum(course_grades)
        overall_count += len(course_grades)
    
    overall_average = overall_total / overall_count
    print(f"Overall average: {overall_average:.2f}")
    
    if overall_average < 50:
        print("You didn't pass the overall courses.")
    else:
        print("You passed the overall courses.")

def view_notes(grades):
    if not grades:
        print("No grades entered yet.")
    else:
        print("Here are your grades:")
        for course, course_grades in grades.items():
            print(f"{course}: {course_grades}")

def main():
    grades = load_grades()
    if not login():
        return
    
    while True:
        print("\nSelect the action you want to perform:")
        print("1. Add notes")
        print("2. Calculate and display average")
        print("3. View notes")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            add_notes(grades)
        elif choice == "2":
            calculate_average(grades)
        elif choice == "3":
            view_notes(grades)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()