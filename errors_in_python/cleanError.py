def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Devisor cannot be zero")  # Raise an exception if divisor is zero
    return dividend / divisor  # This function divides two numbers and returns the result.


grades =[]  # Initialize an empty list to store grades.
print("Welcome to the average grade calculator!")  # This prints a welcome message.

try:
    average = divide(sum(grades), len(grades))  # This calculates the average of the grades.
except ZeroDivisionError as e: # This catches the ZeroDivisionError if the grades list is empty.
    # print(e) # This will print the error message if there are no grades.    
    print("No grades available to calculate average.") # This prints a message if there are no grades.
else:
        print(f"The average grade is: {average}")  # This prints the average grade.
finally:
    print("Thank you for using the average grade calculator!")        
    


