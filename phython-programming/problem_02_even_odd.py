# Problem 2: Even or Odd Checker
# Description: Write a program that checks whether a number entered by the user is even or odd.

def main():
    print("=" * 45)
    print("  Problem 2: Even or Odd Checker")
    print("=" * 45)
    
    try:
        # Taking integer input from the user
        number = int(input("Enter an integer: "))

        # Checking if the number is even or odd using modulo operator (%)
        if number % 2 == 0:
            print(f"\nResult: The number {number} is EVEN.")
        else:
            print(f"\nResult: The number {number} is ODD.")
            
        print("=" * 45)
    except ValueError:
        print("\n[Error] Invalid input! Please enter a whole number (integer).")

if __name__ == "__main__":
    main()
