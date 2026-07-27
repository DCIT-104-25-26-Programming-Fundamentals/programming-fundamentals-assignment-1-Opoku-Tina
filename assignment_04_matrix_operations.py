# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, columns, name):
    matrix = []
    print(f"\nEnter {name} matrix ( {rows}) * {columns}):")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        while len(row) < columns:
            row.append(0)
        matrix.append(row[:columns]) #Take only the first 'columns'numbers
    return matrix

def print_matrix(matrix, name=""):
    if name:
        print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{num:4}" for num in row))
            
def transpose(matrix):
    rows = len(matrix) 
    columns = len(matrix[0])    
    transposed =[[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            transposed[j][i] = matrix[i][j]   
    return transposed
    
def add_matrices(matrix_a, matrix_b):
    rows =   len(matrix_a) 
    columns = len(matrix_a[0])    
    result =[[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]  
    return result
    
def multiply_matrices(matrix_a, matrix_b):
    rows_a =   len(matrix_a) 
    columns_a = len(matrix_a[0]) 
    rows_b =   len(matrix_b) 
    columns_b = len(matrix_b[0]) 
    #Check if multiplication is possible 
    if columns_a != rows_b:
        return None 
    #Create result matrix (rows_a * columns_b)
    result = [[0 for _ in range(columns_b)] for _ in range(rows_a)]
    #Matrix multiplication
    for i in range(rows_a):
        for j in range(columns_b):
            total = 0
            for k in range(columns_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total 
    return result 

#MAIN PROGRAM
if __name__ == "__main__":
    print("=" * 50)   
    print("MATRIX OPERATIONS")  
    print("=" * 50)
    
    # =======PART A: Transpose =======
    print("\n" + "=" * 30)
    print("Part A: TRANSPOSE MATRIX")
    print("=" * 30)
    
    rows = int (input("Enter number of rows: "))
    columns = int (input("Enter number of columns: "))
    
    matrix_a = read_matrix(rows, columns , "Original")
    print_matrix(matrix_a, "Original Matrix")
    
    transposed = transpose(matrix_a)
    print_matrix(transposed, "Transposed Matrix")
    
    # ======= PART B: Add Two Matrices =======
    print("\n" + "=" * 30)
    print("PART B: ADD TWO MATRICES")
    print("=" * 30)
    
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    matrix_b = read_matrix(rows, columns, "first")
    matrix_c = read_matrix(rows, columns, "second")
    
    print_matrix(matrix_b, "Matrix A")
    print_matrix(matrix_c, "Matrix B")
    
    sum_matrix = add_matrices(matrix_b, matrix_c)
    print_matrix(sum_matrix, "Sum (A + B)")
    
    # ======= PART C: Multiply Two Matrices =======
    print("\n" + "=" * 30)
    print("PART C: MULTIPLY TWO MATRICES")
    print("=" * 30)
    
    rows_m = int(input("Enter rows for matrix A: "))
    columns_m = int(input("Enter columns for matrix A (and rows for matrix B): "))
    columns_p = int(input("Enter columns for matrix B: "))
    
    matrix_m = read_matrix(rows_m, columns_m, "A")
    matrix_n = read_matrix(columns_m, columns_p, "B")
    
    print_matrix(matrix_m, "Matrix A")
    print_matrix(matrix_n, "Matrix B")
    
    product = multiply_matrices(matrix_m, matrix_n)
    if product is None:
        print("\nERROR: Cannot multiply matrices! Columns of A must equal rows of B.")
    else:
        print_matrix(product, "Product (A * B)")  
        
    print("\n" + "=" * 50)   
    print("All operations completed!")   