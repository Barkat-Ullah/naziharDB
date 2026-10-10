from typing import Callable, Tuple, List, Optional

def bisection_method(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-5,
    max_iter: int = 100,
    verbose: bool = True
) -> Tuple[Optional[float], int, List[dict]]:
 
    fa = f(a)
    fb = f(b)

    # Check if a or b is already an exact root
    if abs(fa) < 1e-12:
        return a, 0, []
    if abs(fb) < 1e-12:
        return b, 0, []

    # Check sign condition
    if fa * fb > 0:
        if verbose:
            print(f"[Error] f(a) and f(b) must have opposite signs!")
            print(f"        f({a}) = {fa:.6f}, f({b}) = {fb:.6f}")
            print(f"        f(a) * f(b) = {fa * fb:.6f} > 0. Root is not bracketed.")
        return None, 0, []

    history = []
    
    if verbose:
        print("\n" + "=" * 80)
        print(f"{'Iter':<6}{'a':<14}{'b':<14}{'c (Midpoint)':<16}{'f(c)':<16}{'Error (|b-a|/2)':<16}")
        print("=" * 80)

    c = a
    for iteration in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)
        error = abs(b - a) / 2.0

        history.append({
            "iter": iteration,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "error": error
        })

        if verbose:
            print(f"{iteration:<6}{a:<14.6f}{b:<14.6f}{c:<16.6f}{fc:<16.6e}{error:<16.6e}")

        # Check stopping criteria
        if abs(fc) < tol or error < tol:
            if verbose:
                print("=" * 80)
                print(f"[Success] Converged in {iteration} iterations.")
            return c, iteration, history

        # Update interval
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    if verbose:
        print("=" * 80)
        print(f"[Warning] Maximum iterations ({max_iter}) reached without meeting exact tolerance.")
    
    return c, max_iter, history


def default_equations():
    """Returns a dictionary of standard example equations for demonstration."""
    return {
        "1": {
            "name": "f(x) = x^3 - x - 2 = 0",
            "func": lambda x: x**3 - x - 2,
            "default_a": 1.0,
            "default_b": 2.0
        },
        "2": {
            "name": "f(x) = x^3 - 4x - 9 = 0",
            "func": lambda x: x**3 - 4*x - 9,
            "default_a": 2.0,
            "default_b": 3.0
        },
        "3": {
            "name": "f(x) = x^2 - 4 = 0",
            "func": lambda x: x**2 - 4,
            "default_a": 0.0,
            "default_b": 3.0
        },
        "4": {
            "name": "f(x) = cos(x) - x = 0",
            "func": lambda x: __import__("math").cos(x) - x,
            "default_a": 0.0,
            "default_b": 1.0
        }
    }


def main():
    print("=" * 60)
    print("      PROBLEM 4: BISECTION METHOD ROOT FINDER")
    print("=" * 60)

    eqs = default_equations()
    print("Select an equation to solve:")
    for key, item in eqs.items():
        print(f"  [{key}] {item['name']} (Recommended interval: [{item['default_a']}, {item['default_b']}])")
    print("  [5] Custom Python equation (e.g., x**3 - 2*x - 5)")

    choice = input("\nEnter choice (1-5, default 1): ").strip() or "1"

    if choice in eqs:
        selected = eqs[choice]
        f = selected["func"]
        eq_name = selected["name"]
        default_a = selected["default_a"]
        default_b = selected["default_b"]
    elif choice == "5":
        expr = input("Enter function in terms of x (e.g., x**3 - x - 2): ").strip()
        eq_name = f"f(x) = {expr}"
        # Safe math evaluation
        import math
        allowed_names = {
            "x": 0, "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "exp": math.exp, "log": math.log, "sqrt": math.sqrt, "pi": math.pi, "e": math.e
        }
        def custom_f(val):
            allowed_names["x"] = val
            return eval(expr, {"__builtins__": {}}, allowed_names)
        f = custom_f
        default_a = 1.0
        default_b = 2.0
    else:
        print("Invalid choice, using default: f(x) = x^3 - x - 2 = 0")
        selected = eqs["1"]
        f = selected["func"]
        eq_name = selected["name"]
        default_a = selected["default_a"]
        default_b = selected["default_b"]

    print(f"\nSolving: {eq_name}")
    
    # Input interval [a, b]
    try:
        a_in = input(f"Enter interval start 'a' (default {default_a}): ").strip()
        a = float(a_in) if a_in else default_a

        b_in = input(f"Enter interval end 'b' (default {default_b}): ").strip()
        b = float(b_in) if b_in else default_b

        tol_in = input("Enter tolerance (default 0.0001): ").strip()
        tol = float(tol_in) if tol_in else 0.0001

        max_in = input("Enter maximum iterations (default 50): ").strip()
        max_iter = int(max_in) if max_in else 50
    except ValueError:
        print("[Error] Invalid numerical inputs. Running with defaults.")
        a, b, tol, max_iter = default_a, default_b, 0.0001, 50

    root, iters, _ = bisection_method(f, a, b, tol=tol, max_iter=max_iter, verbose=True)

    if root is not None:
        print("\n--- Final Results ---")
        print(f"Function       : {eq_name}")
        print(f"Interval       : [{a}, {b}]")
        print(f"Approximate Root: {root:.6f}")
        print(f"f(root)        : {f(root):.6e}")
        print(f"Iterations     : {iters}")
        print(f"Tolerance      : {tol}")


if __name__ == "__main__":
    main()
