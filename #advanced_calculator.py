# advanced_calculator.py
import math

def add(x, y):
  """This function adds two numbers"""
  return x + y

def subtract(x, y):
  """This function subtracts two numbers"""
  return x - y

def multiply(x, y):
  """This function multiplies two numbers"""
  return x * y

def divide(x, y):
  """This function divides two numbers"""
  # Handle division by zero error
  if y == 0:
    return "Error! Division by zero."
  else:
    return x / y

#Advanced Functions
def power(x, y):
  """This function raises x to the power of y"""
  return x ** y

def square_root(x):
  """This function calculates the square root of x"""
  # Handle negative input for square root
  if x < 0:
    return "Error! Cannot calculate square root of a negative number."
  else:
    return math.sqrt(x)

def sine(x):
  """This function calculates the sine of x (in radians)"""
  return math.sin(x)

def cosine(x):
  """This function calculates the cosine of x (in radians)"""
  return math.cos(x)

def tangent(x):
  """This function calculates the tangent of x (in radians)"""
  # Optional: Handle cases where tangent is undefined (e.g., pi/2 + n*pi)
  if math.cos(x) == 0:
      return "Error! Tangent is undefined for this angle."
  return math.tan(x)

if __name__ == "__main__":
  print("---------------------------")
  print(" Advanced Python Calculator")
  print("---------------------------")

  while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Sine (sin(x)) - x in radians")
    print("8. Cosine (cos(x)) - x in radians")
    print("9. Tangent (tan(x)) - x in radians")
    print("Enter 'quit' to exit.")
    
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/quit): ")

    if choice.lower() == 'quit':
        print("Exiting calculator.")
        break


    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number (x): "))
            num2 = float(input("Enter second number (y): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
    elif choice in ('6', '7', '8', '9'):
        try:
            num1 = float(input("Enter the number (x): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    else:
        print("Invalid Input for operation choice.")
        continue


    result = None
    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")
    elif choice == '5':
        result = power(num1, num2)
        print(f"Result: {num1} ^ {num2} = {result}")
    elif choice == '6':
        result = square_root(num1)
        print(f"Result: √{num1} = {result}")
    elif choice == '7':
        result = sine(num1)
        print(f"Result: sin({num1}) = {result}")
    elif choice == '8':
        result = cosine(num1)
        print(f"Result: cos({num1}) = {result}")
    elif choice == '9':
        result = tangent(num1)
        print(f"Result: tan({num1}) = {result}")

    print("-" * 20) # Separator for clarity

