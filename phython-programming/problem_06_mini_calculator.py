# Problem 6: Mini Calculator
# Description: Make a mini calculator which performs the following operations:
#              +, -, *, /, //, power (**), %

def calculate(num1, operator, num2):
    """
    Performs arithmetic calculation based on the specified operator.
    Supports: +, -, *, /, //, power (or **), %
    """
    op = operator.strip().lower()
    
    if op == '+':
        return num1 + num2, None
    elif op == '-':
        return num1 - num2, None
    elif op == '*':
        return num1 * num2, None
    elif op == '/':
        if num2 == 0:
            return None, "Error: Division by zero is undefined."
        return num1 / num2, None
    elif op == '//':
        if num2 == 0:
            return None, "Error: Floor division by zero is undefined."
        return num1 // num2, None
    elif op in ('power', '**', '^'):
        return num1 ** num2, None
    elif op == '%':
        if num2 == 0:
            return None, "Error: Modulo by zero is undefined."
        return num1 % num2, None
    else:
        return None, f"Error: Unsupported operator '{operator}'."


def format_number(val):
    """Formats floats without trailing .0 if integer."""
    if isinstance(val, float) and val.is_integer():
        return int(val)
    return val


def main():
    print("=" * 50)
    print("           Mini Calculator")
    print("=" * 50)
    print("Supported Operations:")
    print("  [+]  Addition")
    print("  [-]  Subtraction")
    print("  [*]  Multiplication")
    print("  [/]  Standard Division")
    print("  [//] Floor Division")
    print("  [**] or [power] Exponentiation (Power)")
    print("  [%]  Modulo (Remainder)")
    print("=" * 50)

    while True:
        try:
            raw1 = input("\nEnter first number (or 'q' to quit): ").strip()
            if raw1.lower() == 'q':
                print("Exiting calculator. Goodbye!")
                break
            num1 = float(raw1)

            operator = input("Enter operator (+, -, *, /, //, power, %): ").strip()
            
            raw2 = input("Enter second number: ").strip()
            num2 = float(raw2)

            result, error = calculate(num1, operator, num2)

            if error:
                print(f"[Calculation Failed] {error}")
            else:
                n1_fmt = format_number(num1)
                n2_fmt = format_number(num2)
                res_fmt = format_number(result)
                print(f"\nResult: {n1_fmt} {operator} {n2_fmt} = {res_fmt}")

        except ValueError:
            print("[Error] Please enter valid numbers.")

        again = input("\nDo you want to perform another calculation? (y/n, default 'y'): ").strip().lower()
        if again == 'n':
            print("Thank you for using the Mini Calculator!")
            break

if __name__ == "__main__":
    main()
