# Python Programming Problems & Solutions

Welcome to the Python Programming Lab collection located at:
`C:\nub\software-development\phython-programming`

This directory contains standalone Python solutions for all 8 assigned tasks, as well as a unified interactive runner.

---

## Directory Structure

```text
phython-programming/
├── problem_01_sum_diff_product.py   # Problem 1: Sum, Difference & Product
├── problem_02_even_odd.py           # Problem 2: Even or Odd Checker
├── problem_03_find_largest.py       # Problem 3: Function to Find Largest in List
├── problem_04_count_vowels.py       # Problem 4: Count Vowels in a Word
├── problem_05_highest_mark_student.py # Problem 5: Student with Highest Mark
├── problem_06_mini_calculator.py    # Problem 6: Mini Calculator (+, -, *, /, //, power, %)
├── problem_07_person_details.py     # Problem 7: Person Details Input & Display
├── problem_08_age_calculation.py    # Problem 8: Age Calculation
├── main.py                          # Interactive Menu Runner (Run any or all)
└── README.md                        # Documentation & Explanations
```

---

## How to Run

### Option 1: Interactive Menu (All Problems in One Place)
Run the central menu in your terminal:
```bash
python main.py
```
From the menu, enter numbers `1` through `8`, `A` to run all sequentially, or `0` to exit.

### Option 2: Run Individual Problem Files
You can run any specific problem directly:
```bash
python problem_01_sum_diff_product.py
python problem_02_even_odd.py
python problem_03_find_largest.py
python problem_04_count_vowels.py
python problem_05_highest_mark_student.py
python problem_06_mini_calculator.py
python problem_07_person_details.py
python problem_08_age_calculation.py
```

---

## Problem Summaries & Code Walkthrough

### Problem 1: Sum, Difference, and Product
- **File:** `problem_01_sum_diff_product.py`
- **Question:** Write a program that asks for two numbers and prints their sum, difference, and product.
- **Operations:**
  - Sum: `num1 + num2`
  - Difference: `num1 - num2`
  - Product: `num1 * num2`
- **Sample Run:**
  ```text
  Enter first number: 12
  Enter second number: 5

  --- Results ---
  First Number : 12.0
  Second Number: 5.0
  Sum          : 12.0 + 5.0 = 17.0
  Difference   : 12.0 - 5.0 = 7.0
  Product      : 12.0 * 5.0 = 60.0
  ```

---

### Problem 2: Even or Odd Checker
- **File:** `problem_02_even_odd.py`
- **Question:** Write a program that checks whether a number entered by the user is even or odd.
- **Logic:** Uses the modulo operator `number % 2 == 0` to check divisibility by 2.
- **Sample Run:**
  ```text
  Enter an integer: 17

  Result: The number 17 is ODD.
  ```

---

### Problem 3: Function to Return the Largest Number in a List
- **File:** `problem_03_find_largest.py`
- **Question:** Write a function that takes a list of numbers and returns the largest one.
- **Function Definition:**
  ```python
  def find_largest(numbers):
      if not numbers:
          return None
      largest = numbers[0]
      for num in numbers:
          if num > largest:
              largest = num
      return largest
  ```
- **Sample Run:**
  ```text
  Sample List   : [24, 67, 12, 89, 45, 99, 3]
  Largest Number: 99
  Enter numbers separated by spaces: 10 45 92 14
  Your List     : [10.0, 45.0, 92.0, 14.0]
  Largest Number: 92
  ```

---

### Problem 4: Count Vowels in a Word
- **File:** `problem_04_count_vowels.py`
- **Question:** Write a program that counts how many vowels are in a word entered by the user.
- **Logic:** Checks each character against vowels (`a`, `e`, `i`, `o`, `u`), case-insensitively.
- **Sample Run:**
  ```text
  Enter a word: Education

  --- Results ---
  Word entered        : "Education"
  Total vowels count  : 5
  Vowel breakdown     : E: 1, U: 1, A: 1, I: 1, O: 1
  ```

---

### Problem 5: Student with Highest Mark
- **File:** `problem_05_highest_mark_student.py`
- **Question:** Create a dictionary of three students and their marks, then print the name of the student with the highest mark.
- **Logic:** 
  ```python
  top_student = max(students_marks, key=students_marks.get)
  ```
- **Sample Run:**
  ```text
  --- Student Marks Records ---
   - Tamanna: 92
   - Rahim: 85
   - Karim: 96

  --- Result ---
  Top Student : Karim
  Highest Mark: 96

  The student with the highest mark is: Karim
  ```

---

### Problem 6: Mini Calculator
- **File:** `problem_06_mini_calculator.py`
- **Question:** Make a mini calculator which performs operations: `+`, `-`, `*`, `/`, `//`, `power`, `%`.
- **Supported Operations:**
  - `+` (Addition)
  - `-` (Subtraction)
  - `*` (Multiplication)
  - `/` (Division with zero-division safeguard)
  - `//` (Floor Division with zero-division safeguard)
  - `power` or `**` (Exponentiation)
  - `%` (Modulus with zero-division safeguard)
- **Sample Run:**
  ```text
  Enter first number: 10
  Enter operator (+, -, *, /, //, power, %): //
  Enter second number: 3

  Result: 10 // 3 = 3
  ```

---

### Problem 7: Person Details Input & Display
- **File:** `problem_07_person_details.py`
- **Question:** Print a person's details (name, id, cgpa, age) taking user input.
- **Sample Run:**
  ```text
  Enter Name : Tamanna
  Enter ID   : 231-015-001
  Enter CGPA : 3.85
  Enter Age  : 20

  =============================================
            PERSON PROFILE DETAILS
  =============================================
   Name : Tamanna
   ID   : 231-015-001
   CGPA : 3.85
   Age  : 20 years
  =============================================
  ```

---

### Problem 8: Age Calculation
- **File:** `problem_08_age_calculation.py`
- **Question:** 5 years ago your age was 5 years. Show your name with current age. Your output should show like: `Tamanna's current age is 10`.
- **Calculation:**
  - $\text{Current Age} = \text{Age 5 Years Ago} (5) + \text{Years Passed} (5) = 10$
- **Sample Run:**
  ```text
  Enter your name [press Enter for 'Tamanna']: Tamanna

  --- Output ---
  Tamanna's current age is 10
  ```
