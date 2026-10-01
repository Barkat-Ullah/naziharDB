# Problem 3: Function to Find the Largest Number in a List
# Description: Write a function that takes a list of numbers and returns the largest one.

def find_largest(numbers):
    """
    Takes a list of numbers and returns the largest one.
    Returns None if the list is empty.
    """
    if not numbers:
        return None
    
    # Initialize largest with the first element
    largest = numbers[0]
    
    # Iterate through list elements to find the maximum
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest


def main():
    print("=" * 45)
    print("  Problem 3: Find Largest Number in a List")
    print("=" * 45)

    # Example 1: Predefined test demonstration
    sample_list = [24, 67, 12, 89, 45, 99, 3]
    result = find_largest(sample_list)
    print(f"Sample List   : {sample_list}")
    print(f"Largest Number: {result}")
    print("-" * 45)

    # Example 2: Interactive user input
    user_input = input("Enter numbers separated by spaces (e.g. 10 55 32 88): ").strip()
    if user_input:
        try:
            user_list = [float(x) for x in user_input.split()]
            largest_user_num = find_largest(user_list)
            # Display cleanly as int if it has no fractional part
            formatted_largest = int(largest_user_num) if largest_user_num.is_integer() else largest_user_num
            print(f"Your List     : {user_list}")
            print(f"Largest Number: {formatted_largest}")
        except ValueError:
            print("[Error] Invalid input! Please enter only numbers separated by spaces.")
    else:
        print("No input provided. Using sample demonstration above.")
        
    print("=" * 45)

if __name__ == "__main__":
    main()
