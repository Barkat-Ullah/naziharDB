# Problem 8: Age Calculation
# Description: 5 years ago your age was 5 years. Show your name with current age.
#              Output should show like: Tamanna's current age is 10

def main():
    print("=" * 50)
    print("  Problem 8: Current Age Calculation")
    print("=" * 50)

    # Given condition:
    # 5 years ago, the age was 5 years.
    years_ago = 5
    age_5_years_ago = 5

    # Calculating current age:
    current_age = age_5_years_ago + years_ago  # 5 + 5 = 10

    # User enters their name (defaults to "Tamanna" if pressed Enter directly)
    user_name = input("Enter your name [press Enter for 'Tamanna']: ").strip()
    if not user_name:
        user_name = "Tamanna"

    # Displaying the exact required output format
    print("\n--- Output ---")
    print(f"{user_name}'s current age is {current_age}")
    print("=" * 50)

if __name__ == "__main__":
    main()
