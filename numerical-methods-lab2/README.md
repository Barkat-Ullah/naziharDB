# Numerical Methods (Lab 2) - Python Solutions

This directory contains clean, robust Python implementations for all tasks in **Numerical Methods (Lab 2)**.

**Location:** `C:\nub\software-development\numerical-methods-lab2`

---

## Directory Structure

```text
numerical-methods-lab2/
├── problem_01_grading_system.py         # Problem 1: Marks to Grade converter
├── problem_02_star_pattern_ascending.py  # Problem 2: Ascending star pattern (input = 5)
├── problem_03_star_pattern_descending.py # Problem 3: Descending star pattern (input = 5)
├── problem_04_bisection_method.py        # Problem 4: Bisection Method root-finding
├── main.py                               # Interactive menu runner for all tasks
├── run.bat                               # Windows 1-click batch runner
└── README.md                             # Documentation & walk-through
```

---

## Problem Explanations & Solutions

### Problem 1: Grading System based on Table
- **Question:** Write a python code to print the output based on the following table:

  | Marks | Grade |
  | :--- | :--- |
  | `90>=` | `A` |
  | `80 to <90` | `B` |
  | `70 to <80` | `C` |
  | `60 to <70` | `D` |
  | `Below 60` | `Fail` |
  | `otherwise` | `Invalid marks given` |

- **Logic:**
  - Marks must be in valid percentage range $[0, 100]$.
  - If `marks < 0` or `marks > 100`: return `"Invalid marks given"`
  - If `marks >= 90`: `"A"`
  - If `marks >= 80`: `"B"`
  - If `marks >= 70`: `"C"`
  - If `marks >= 60`: `"D"`
  - If `0 <= marks < 60`: `"Fail"`
- **File:** `problem_01_grading_system.py`

---

### Problem 2: Ascending Star Pattern
- **Question:** Print the following pattern where taking input from the user:
  ```text
  *
  * *
  * * *
  * * * *
  * * * * *       input = 5
  ```
- **Logic:**
  - Outer loop runs from `i = 1` to `n`.
  - Inner loop prints `i` asterisks separated by spaces.
- **File:** `problem_02_star_pattern_ascending.py`

---

### Problem 3: Descending Star Pattern
- **Question:** Print the following pattern where taking input from the user:
  ```text
  * * * * *
  * * * *
  * * *
  * *
  *               input = 5
  ```
- **Logic:**
  - Outer loop runs downwards from `i = n` down to `1`.
  - Inner loop prints `i` asterisks separated by spaces.
- **File:** `problem_03_star_pattern_descending.py`

---

### Problem 4: Bisection Method in Python
- **Question:** Implement the bisection method in python.
- **Mathematical Theory:**
  - Root-finding algorithm based on Bolzano's Intermediate Value Theorem: If $f(x)$ is continuous on $[a, b]$ and $f(a) \cdot f(b) < 0$, then there exists at least one root $c \in (a, b)$ such that $f(c) = 0$.
  - Midpoint: $c = \frac{a + b}{2}$
  - Interval reduction:
    - If $f(a) \cdot f(c) < 0$, new interval is $[a, c]$ ($b = c$).
    - Else, new interval is $[c, b]$ ($a = c$).
  - Stopping condition: $|f(c)| < \text{tol}$ or $\frac{|b - a|}{2} < \text{tol}$.
- **Features Included:**
  - Iteration table with formatted columns: `Iter`, `a`, `b`, `c`, `f(c)`, `Error`.
  - Includes standard textbook equations:
    - $f(x) = x^3 - x - 2 = 0$ on $[1, 2]$
    - $f(x) = x^3 - 4x - 9 = 0$ on $[2, 3]$
    - $f(x) = x^2 - 4 = 0$ on $[0, 3]$
    - $f(x) = \cos(x) - x = 0$ on $[0, 1]$
    - Custom equation input support
- **File:** `problem_04_bisection_method.py`

---

## How to Run

### Option 1: Interactive Menu
Run the central menu:
```bash
cd C:\nub\software-development\numerical-methods-lab2
python main.py
```
Or double-click `run.bat` on Windows.

### Option 2: Run Individual Files
```bash
python problem_01_grading_system.py
python problem_02_star_pattern_ascending.py
python problem_03_star_pattern_descending.py
python problem_04_bisection_method.py
```
