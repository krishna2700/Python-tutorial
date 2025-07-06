def divide(dividend, divisor):
    if divisor == 0:
        print("Cannot divide by zero")
        return

    return dividend / divisor   # This function divides two numbers and returns the result.

divide(10, 0)  # This will print "Cannot divide by zero" and return None


# grades = [90, 80, 70, 60, 50]  # This is a list of grades.
grades =[] # Initialize an empty list to store grades.
print("Welcome to the average grade calculator!")  # This prints a welcome message.

if len(grades) == 0:  # This checks if the grades list is empty.
    print("No grades available to calculate average.")  # This prints a message if there are no grades.

average = divide(sum(grades), len(grades))  # This calculates the average of the grades.

print(f"The average grade is: {average}")  # This prints the average grade.