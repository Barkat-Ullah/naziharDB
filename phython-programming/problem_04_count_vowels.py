# Problem 4: Count Vowels in a Word
# Description: Write a program that counts how many vowels are in a word entered by the user.

def count_vowels(word):
    """
    Counts the total number of vowels (A, E, I, O, U) in a given word or text.
    Also returns a breakdown dictionary for each vowel.
    """
    vowels = "aeiou"
    word_lower = word.lower()
    
    total_count = 0
    vowel_breakdown = {v: 0 for v in vowels}
    
    for char in word_lower:
        if char in vowels:
            total_count += 1
            vowel_breakdown[char] += 1
            
    return total_count, vowel_breakdown


def main():
    print("=" * 45)
    print("  Problem 4: Vowel Counter")
    print("=" * 45)
    
    user_word = input("Enter a word: ").strip()
    
    if not user_word:
        print("[Notice] Empty input entered.")
        return

    total, breakdown = count_vowels(user_word)

    print("\n--- Results ---")
    print(f"Word entered        : \"{user_word}\"")
    print(f"Total vowels count  : {total}")
    print("Vowel breakdown     :", ", ".join([f"{v.upper()}: {count}" for v, count in breakdown.items() if count > 0]) or "None")
    print("=" * 45)

if __name__ == "__main__":
    main()
