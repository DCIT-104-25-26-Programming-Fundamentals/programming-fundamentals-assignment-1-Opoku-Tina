# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 35)
    print("   STUDENT RECORD SYSTEM MENU")
    print("=" * 35)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    print("=" * 35)

def add_student(students):
    """Add a new student to the records."""
    name = input("Student name: ")    
    # Validate ID
    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Invalid ID! Please enter a number.")
        return
    
    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print(f"Student with ID {student_id} already exists!")
            return
    
    # Get scores
    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Number of scores must be positive!")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    scores = []
    for i in range(num_scores):
        try:
            score = float(input(f"Enter score {i+1}: "))
            scores.append(score)
        except ValueError:
            print("Invalid score! Please enter a number.")
            return
    
    # Create student record
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')

def calculate_average(scores):
    """Calculate the average of a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def display_all_students(students):
    """Display all students in a formatted table."""
    if not students:
        print("\nNo students have been added yet.")
        return
    
    print("\n" + "-" * 55)
    print(f"{'Name':<15} {'ID':<12} {'Scores':<20} {'Average':>8}")
    print("-" * 55)
    
    for student in students:
        name = student["name"][:14]  # Truncate long names
        student_id = student["id"]
        scores = student["scores"]
        avg = calculate_average(scores)
                
        # Format scores as comma-separated string
        scores_str = ", ".join(str(s) for s in scores)
        if len(scores_str) > 19:
            scores_str = scores_str[:17] + "..."
        print(f"{name:<15} {student_id:<12} {scores_str:<20} {avg:>8.2f}")
    print("-" * 55)

def calculate_student_average(students):
    """Calculate and display the average score for a specific student."""
    if not students:
        print("\nNo students have been added yet.")
        return
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid ID! Please enter a number.")
        return
    
    # Find the student
    for student in students:
        if student["id"] == student_id:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg:.2f}")
            return
    print(f"Student with ID {student_id} not found.")

if __name__ == "__main__":
    # Initialize empty student records list
    student_records = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")        
        if choice == "1":
            add_student(student_records)
        elif choice == "2":
            display_all_students(student_records)
        elif choice == "3":
            calculate_student_average(student_records)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")