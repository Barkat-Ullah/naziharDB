"""
Python Programming Lab Exercises
Location: C:\\nub\\software-development\\phython-programming
All 8 Problems Interactive Runner
"""

import sys

# Import functions from each problem script
from problem_01_sum_diff_product import main as run_p1
from problem_02_even_odd import main as run_p2
from problem_03_find_largest import main as run_p3
from problem_04_count_vowels import main as run_p4
from problem_05_highest_mark_student import main as run_p5
from problem_06_mini_calculator import main as run_p6
from problem_07_person_details import main as run_p7
from problem_08_age_calculation import main as run_p8

PROBLEMS = {
    "1": ("Two Numbers: Sum, Difference & Product", run_p1),
    "2": ("Check Even or Odd Number", run_p2),
    "3": ("Function: Largest Number in a List", run_p3),
    "4": ("Count Vowels in a Word", run_p4),
    "5": ("Student with Highest Mark (Dictionary)", run_p5),
    "6": ("Mini Calculator (+, -, *, /, //, power, %)", run_p6),
    "7": ("Person Details (Name, ID, CGPA, Age)", run_p7),
    "8": ("Age Calculation (Past age to Current age)", run_p8),
}

def print_menu():
    print("\n" + "=" * 60)
    print("      PYTHON PROGRAMMING ASSIGNMENT / LAB RUNNER")
    print("=" * 60)
    for key, (title, _) in PROBLEMS.items():
        print(f" [{key}] {title}")
    print(" [A] Run All Problems Sequentially")
    print(" [0] Exit")
    print("=" * 60)

def main():
    while True:
        print_menu()
        choice = input("Enter choice (0-8 or A): ").strip().upper()

        if choice == "0":
            print("\nExiting program. Happy coding!")
            break
        elif choice == "A":
            for key in sorted(PROBLEMS.keys()):
                title, func = PROBLEMS[key]
                print("\n" + "#" * 60)
                print(f"  EXECUTING PROBLEM {key}: {title}")
                print("#" * 60)
                try:
                    func()
                except Exception as e:
                    print(f"Error running Problem {key}: {e}")
                input("\nPress Enter to continue to the next problem...")
        elif choice in PROBLEMS:
            title, func = PROBLEMS[choice]
            print("\n" + "-" * 60)
            try:
                func()
            except Exception as e:
                print(f"Error running Problem {choice}: {e}")
        else:
            print("[Warning] Invalid choice. Please select from 0 to 8 or A.")

if __name__ == "__main__":
    main()
