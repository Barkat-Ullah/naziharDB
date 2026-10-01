# Problem 7: Person Details Input & Display
# Description: Print a person's details (name, id, cgpa, age) taking user input.

def main():
    print("=" * 45)
    print("  Problem 7: Person Details")
    print("=" * 45)

    # Taking inputs from user
    name = input("Enter Name : ").strip()
    person_id = input("Enter ID   : ").strip()

    # CGPA with validation
    while True:
        try:
            cgpa_input = input("Enter CGPA : ").strip()
            cgpa = float(cgpa_input)
            break
        except ValueError:
            print("[Error] Invalid CGPA! Please enter a valid number (e.g., 3.75).")

    # Age with validation
    while True:
        try:
            age_input = input("Enter Age  : ").strip()
            age = int(age_input)
            break
        except ValueError:
            print("[Error] Invalid Age! Please enter a valid integer (e.g., 21).")

    # Printing formatted details
    print("\n" + "=" * 45)
    print("          PERSON PROFILE DETAILS")
    print("=" * 45)
    print(f" Name : {name}")
    print(f" ID   : {person_id}")
    print(f" CGPA : {cgpa:.2f}")
    print(f" Age  : {age} years")
    print("=" * 45)

if __name__ == "__main__":
    main()
