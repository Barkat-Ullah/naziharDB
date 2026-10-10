def determine_grade(marks: float) -> str:

    if marks < 0 or marks > 100:
        return "Invalid marks given"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:  # Below 60 (0 <= marks < 60)
        return "Fail"


def main():
    print("=" * 50)
    print("      PROBLEM 1: GRADE CALCULATION SYSTEM")
    print("=" * 50)
    
    try:
        user_input = input("Enter marks (0 - 100): ").strip()
        marks = float(user_input)
        grade = determine_grade(marks)
        
        print("\n--- Output ---")
        print(f"Marks Entered: {marks}")
        print(f"Grade/Result : {grade}")
    except ValueError:
        print("\n--- Output ---")
        print("Grade/Result : Invalid marks given")


if __name__ == "__main__":
    main()
