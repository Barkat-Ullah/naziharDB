
def print_descending_pattern(n: int):
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    print(f"\nPattern for input = {n}:")
    for i in range(n, 0, -1):
        # Method 1: Using nested loops
        for j in range(i):
            print("*", end=" " if j < i - 1 else "")
        print()


def main():
    print("=" * 50)
    print("      PROBLEM 3: DESCENDING STAR PATTERN")
    print("=" * 50)
    
    try:
        user_input = input("Enter number of rows (e.g., 5): ").strip()
        n = int(user_input)
        print_descending_pattern(n)
    except ValueError:
        print("[Error] Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
