# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 30)
    print("        SIMPLE CALCULATOR")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
    print("=" * 30)

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers, rounded to 2 decimal places."""
    if b == 0:
        return None
    return round(a / b, 2)

def modulus(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        return None
    return a % b

def exponentiate(a, b):
    """Return a raised to the power of b."""
    return a ** b

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def perform_calculation():
    """Perform a single calculation based on user choice."""
    display_menu()
    choice = input("Select an operation (1-7): ")
    if choice == "7":
        return False
    
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice! Please select 1-7.")
        return True
    # Get two numbers
    print()
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    
    # Perform calculation
    if choice == "1":
        result = add(num1, num2)
        operator = "+"
        symbol = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operator = "-"
        symbol = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        operator = "*"
        symbol = "*"
    elif choice == "4":
        result = divide(num1, num2)
        operator = "/"
        symbol = "/"
        if result is None:
            print("\nError: Cannot divide by zero.")
            return True
    elif choice == "5":
        result = modulus(num1, num2)
        operator = "%"
        symbol = "%"
        if result is None:
            print("\nError: Cannot perform modulus with zero.")
            return True
    elif choice == "6":
        result = exponentiate(num1, num2)
        operator = "**"
        symbol = "^"
    
    # Display result
    if choice in ["1", "2", "3", "4", "5", "6"]:
        # Format numbers to show integers without decimal if they are whole
        if num1.is_integer():
            num1_display = int(num1)
        else:
            num1_display = num1
            
        if num2.is_integer():
            num2_display = int(num2)
        else:
            num2_display = num2
            
        if isinstance(result, float) and result.is_integer():
            result_display = int(result)
        else:
            result_display = result
        
        print(f"\nResult: {num1_display} {symbol} {num2_display} = {result_display}")
    return True

if __name__ == "__main__":
    print("=" * 30)
    print("    WELCOME TO THE CALCULATOR")
    print("=" * 30)
    
    running = True
    while running:
        running = perform_calculation()
    
    print("\nGoodbye!")