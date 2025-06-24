def multiply(*args):
    print("Arguments received:", args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1,2,3))  # This will print the tuple of arguments received


def add(x,y):
    return x + y

nums = [3,5]

add(*nums)  # This will unpack the list nums and pass its elements as arguments to add
print(add(*nums))  # This will print the sum of the elements in nums

print(add(x=10, y=20))  # This will print 30, passing arguments by keyword

nums = {"x": 10, "y": 20}
print(add(**nums))  # This will unpack the dictionary nums and pass its elements as keyword arguments to add


def multiply(*args):
    print("Arguments received:", args)
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == "*":
        return multiply(*args) # This will unpack the args and pass them to multiply
    elif operator == "+":
        return sum(args) # This will return the sum of the args
    else:
        return "Unsupported operator"
    
print(apply(1, 2, 3, operator="*"))  # This will print the product of the arguments
print(apply(1, 2, 3, operator="+"))  # This will print the sum of the arguments
print(apply(1, 2, 3, operator="-"))  # This will print "Unsupported operator" since "-" is not supported