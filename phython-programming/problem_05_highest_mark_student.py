# Problem 5: Student with Highest Mark
# Description: Create a dictionary of three students and their marks, 
#              then print the name of the student with the highest mark.

def main():
    print("=" * 45)
    print("  Problem 5: Highest Mark Among Students")
    print("=" * 45)

    choice = input("Do you want to enter custom data for 3 students? (y/n, default 'n'): ").strip().lower()

    if choice == 'y':
        students_marks = {}
        print("\nEnter details for 3 students:")
        for i in range(1, 4):
            while True:
                name = input(f"Enter name of student {i}: ").strip()
                if not name:
                    print("Name cannot be empty. Try again.")
                    continue
                try:
                    mark = float(input(f"Enter marks for {name}: "))
                    # Format as int if whole number
                    students_marks[name] = int(mark) if mark.is_integer() else mark
                    break
                except ValueError:
                    print("Please enter a valid numeric mark.")
    else:
        # Default dictionary with three students and their marks
        students_marks = {
            "Tamanna": 92,
            "Rahim": 85,
            "Karim": 96
        }

    print("\n--- Student Marks Records ---")
    for student, mark in students_marks.items():
        print(f" - {student}: {mark}")

    # Finding the student with the highest mark
    # max() using key=students_marks.get returns the key associated with the largest value
    top_student = max(students_marks, key=students_marks.get)
    highest_mark = students_marks[top_student]

    print("\n--- Result ---")
    print(f"Top Student : {top_student}")
    print(f"Highest Mark: {highest_mark}")
    print(f"\nThe student with the highest mark is: {top_student}")
    print("=" * 45)

if __name__ == "__main__":
    main()
