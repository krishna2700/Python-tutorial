def divide(dividend, divisor):
    if divisor == 0:
       raise ZeroDivisionError("Devisor cannot be zero")  # Raise an exception if divisor is zero
    
    return dividend / divisor  # This function divides two numbers and returns the result.


students = [
    {"name": "John", "grades": [75, 90]},
    {"name": "Jane", "grades": [65,95]},
    {"name": "Doe", "grades": [80, 70]}
]



try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))  # This calculates the average of the grades.
        print(f"{name}'s average grade is: {average}")  # This prints the
except ZeroDivisionError as e:
    print(f"Error calculating average for {name}")
else:
    print("-- All averages calculated successfully --") 
finally:
    print("Thank you for using the average grade calculator!")      
