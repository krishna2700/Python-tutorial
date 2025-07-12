def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return dividend / divisor
    

def calculator(*values,operator): # This function takes a variable number of values and an operator function to perform calculations.
    return operator(*values)    
  

result = calculator(20,4,operator=divide)   # This calls the calculator function with 20 and 4 as values and the divide function as the operator.
print(f"Result of division: {result}")  # This prints the result of the division operation.