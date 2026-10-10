"""
Numerical Methods (Lab 2) - Unified Interactive Runner
Location: C:\\nub\\software-development\\numerical-methods-lab2
"""

import sys
from problem_01_grading_system import main as run_p1
from problem_02_star_pattern_ascending import main as run_p2
from problem_03_star_pattern_descending import main as run_p3
from problem_04_bisection_method import main as run_p4

PROBLEMS = {
    "1": ("Grade Calculation based on Table", run_p1),
    "2": ("Ascending Star Pattern (Pyramid)", run_p2),
    "3": ("Descending Star Pattern (Inverted Pyramid)", run_p3),
    "4": ("Bisection Method Root Finder", run_p4),
}


def print_menu():
    print("\n" + "=" * 65)
    print("          NUMERICAL METHODS (LAB 2) - PYTHON SOLUTIONS")
    print("=" * 65)
    for key, (title, _) in PROBLEMS.items():
        print(f" [{key}] Problem {key}: {title}")
    print(" [A] Run All Problems Sequentially")
    print(" [0] Exit")
    print("=" * 65)


def main():
    while True:
        print_menu()
        choice = input("Enter choice (0-4 or A): ").strip().upper()

        if choice == "0":
            print("\nExiting Numerical Methods Lab 2 runner. Goodbye!")
            break
        elif choice == "A":
            for key in sorted(PROBLEMS.keys()):
                title, func = PROBLEMS[key]
                print("\n" + "#" * 65)
                print(f"  EXECUTING PROBLEM {key}: {title}")
                print("#" * 65)
                try:
                    func()
                except Exception as e:
                    print(f"Error running Problem {key}: {e}")
                input("\nPress Enter to continue to the next problem...")
        elif choice in PROBLEMS:
            title, func = PROBLEMS[choice]
            print("\n" + "-" * 65)
            try:
                func()
            except Exception as e:
                print(f"Error running Problem {choice}: {e}")
        else:
            print("[Warning] Invalid choice! Please select 1, 2, 3, 4, A, or 0.")


if __name__ == "__main__":
    main()
