def generate_fibonnaci(n):
    """
    Generate the first n numbers of the Fibonnaci sequence.
    Parameters:
        n (int): Number of terms to generate
    Returns:
        list: Fibonnaci sequence as a list
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    # Start with the first two numbers
    fib = [0, 1]
    
     # Generate the rest
    for i in range(2, n):
        next_num = fib[i-1] + fib[i-2]
        fib.append(next_num)
    return fib

def is_fibonnaci_number(num):
    """
    Check if a number belongs to the Fibonnaci sequence.
    Parameters:
        num (int): Number to check
    Returns:
        bool: True if number is in Fibonnaci sequence, False otherwise
    """
    if num < 0:
        return False
    
    # Generate Fibonnaci numbers until we reach or exceed the number
    a, b = 0, 1
    if num == 0 or num == 1:
        return True
    
    # Generate sequence until we reach or exceed number
    while b < num:
        a, b = b, a + b
    # If b equals num, it's a Fibonnaci number
    return b == num

def print_fibonnaci_sequence(seq):
    """Print the Fibonnaci sequence on one line."""
    if not seq:
        print("No numbers to display.")
    else:
        print("Fibonnaci sequence: " + " ".join(str(num) for num in seq))
        
if __name__ == "__main__":
    print("=" * 50)
    print("FIBONNACI SEQUENCE GENERATOR")
    print("=" * 50)
    
    # ======= PART A: Print First N Terms =======
    print("\n" + "=" * 30)
    print("PART A: PRINT FIRST N TERMS")
    print("=" * 30)
    
    n = int(input("How many terms? "))
    if n <= 0:
        print("Error: Number of terms must be positive.")
    else:
        fib_sequence = generate_fibonnaci(n)
        print_fibonnaci_sequence(fib_sequence)
    
    # ======= PART B: Check if Number is Fibonnaci =======
    print("\n" + "=" * 30)
    print("PART B: CHECK IF NUMBER IS FIBONNACI")
    print("=" * 30)
    
    num = int(input("Enter a number to check: "))
    if is_fibonnaci_number(num):
        print(f"{num} is a Fibonnaci number.")
    else:
        print(f"{num} is NOT a Fibonnaci number.")
    
    print("\n" + "=" * 50)
    print("All operations completed!")