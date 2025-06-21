def add(x,y):
    # print(x + y)  # This prints the sum but does not return it
    return x + y

# add(10,20)
result = add(10,20)
print(result)  # This will print None since add does not return a value


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "Cannot divide by zero"
    
result= divide(10, 2)
# result= divide(10, 0)
print(result)  # This will print the result of the division