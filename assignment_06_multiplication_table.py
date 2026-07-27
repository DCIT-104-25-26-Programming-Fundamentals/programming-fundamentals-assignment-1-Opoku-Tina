# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(number):
    """
    Part A: Print the multiplication table for a single number from 1 to 12.
    Parameters:
        number (int): The number to generate the table for
    """
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:2}  =  {number * i:3}")

def print_tables_up_to(n):
    """
    Part B: Print multiplication tables for all numbers from 1 to N.
    Parameters:
        n (int): The maximum number to generate tables for
    """
    for num in range(1, n + 1):
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 13):
            print(f"{num}  x  {i:2}  =  {num * i:3}")
        print("-" * 30)  # Separator between tables

if __name__ == "__main__":
    print("=" * 50)
    print("MULTIPLICATION TABLE GENERATOR")
    print("=" * 50)
    
    # ======= PART A: Single Table =======
    print("\n" + "=" * 30)
    print("PART A: SINGLE TABLE")
    print("=" * 30)
    
    num = int(input("Enter a number: "))
    print_single_table(num)
    
    # ======= PART B: Tables 1 to N =======
    print("\n" + "=" * 30)
    print("PART B: TABLES 1 TO N")
    print("=" * 30)
    
    n = int(input("Enter a number N: "))
    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to(n)
    
    print("\n" + "=" * 50)
    print("All operations completed!")