# def add(x,y):
#     return x + y

# print(add(10,20))  # This will print the sum of 10 and 20

add = lambda x,y: x + y
print((lambda x,y: x + y)(5,7) ) # This will return 12
# This is a lambda function that takes two arguments x and y and returns their sum

# print(add(10,20))  # This will print the sum of 10 and 20

def double(x):
    return x * 2

sequence = [1, 2, 3, 4, 5]
doubled = [double(x) for x in sequence]
# doubled = map(double, sequence)  # Using map to apply double to each element in sequence

# print(doubled)


sequence = [1, 2, 3, 4, 5]
# doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled =list( map(lambda x: x * 2, sequence))  # Using map with a lambda function to double each element in sequence

print(doubled)