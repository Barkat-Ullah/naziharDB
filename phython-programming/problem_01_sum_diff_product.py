# Problem 1: Two Numbers Operations
# Description: Write a program that asks for two numbers and prints their sum, difference, and product.

def main():
    print("=" * 45)
    print("  Problem 1: Sum, Difference, and Product")
    print("=" * 45)
    
    try:
        # Taking input from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Performing calculations
        total_sum = num1 + num2
        difference = num1 - num2
        product = num1 * num2

        # Displaying results
        print("\n--- Results ---")
        print(f"First Number : {num1}")
        print(f"Second Number: {num2}")
        print(f"Sum          : {num1} + {num2} = {total_sum}")
        print(f"Difference   : {num1} - {num2} = {difference}")
        print(f"Product      : {num1} * {num2} = {product}")
        print("=" * 45)
    except ValueError:
        print("\n[Error] Please enter valid numeric values!")

if __name__ == "__main__":
    main()
