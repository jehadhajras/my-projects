import numpy as np

# Function for addition
def add(a, b):
    return np.add(a, b)

# Function for subtraction
def subtract(a, b):
    return np.subtract(a, b)

# Function for multiplication
def multiply(a, b):
    return np.multiply(a, b)

# Function for division
def divide(a, b):
    # Check if denominator is zero
    if b == 0:
        return "Cannot divide by zero!"
    return np.divide(a, b)

# Function for square root
def square_root(a):
    # Check if number is not negative
    if a < 0:
        return "Square root of negative number is not defined!"
    return np.sqrt(a)

# Function for natural logarithm
def natural_log(a):
    # Check if number is greater than zero
    if a <= 0:
        return "Natural log of non-positive number is not defined!"
    return np.log(a)

# Function to show available operations
def show_operations():
    print("Available operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square root (√)")
    print("6. Natural logarithm (ln)")

# Main function
def main():
    print("Welcome to the Scientific Calculator using Numpy!")
    
    # Show available operations to the user
    show_operations()
    
    while True:
        # Get user's choice
        choice = input("Choose an operation (Enter the number): ")
        
        if choice in ['1', '2', '3', '4']:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            
            if choice == '1':
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif choice == '2':
                result = subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            elif choice == '3':
                result = multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
            elif choice == '4':
                result = divide(a, b)
                print(f"Result: {a} / {b} = {result}")
        
        elif choice == '5':
            a = float(input("Enter the number to find the square root: "))
            result = square_root(a)
            print(f"Result: Square root of {a} = {result}")
        
        elif choice == '6':
            a = float(input("Enter the number to find the natural log: "))
            result = natural_log(a)
            print(f"Result: Natural log of {a} = {result}")
        
        else:
            print("Invalid choice! Please try again.")
        
        # Ask if the user wants to do another calculation
        continue_choice = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
