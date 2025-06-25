def named(**kwargs):
    print("Named arguments:", kwargs) 

named(name="Alice", age=30, city="New York")  # This will print the dictionary of named arguments


# def named(name,age): 
def named(**kwargs):       
    print(kwargs) 
    # print(f"Name: {name}, Age: {age}") 

details={"name": "Bob", "age": 24} 
named(**details)     # This will unpack the dictionary details and pass its elements as keyword arguments to named

def named(name, age):
    print(f"Name: {name}, Age: {age}")

details = {"name": "Charlie", "age": 28}
named(**details)  # This will unpack the dictionary details and pass its elements as keyword arguments    


def named(**kwargs):       
    print(kwargs) 


def named(**kwargs):       
    print("Named arguments:", kwargs)

def print_nicely(**kwargs):
    named(**kwargs)  # This will unpack the dictionary kwargs and pass its elements as keyword arguments to named
    for arg,value in kwargs.items(): # Iterate through the items in kwargs
        print(f"{arg}: {value}")

print_nicely(name="Alice", age=30, city="New York")  # This will print the named arguments and their values        


def both(*args, **kwargs):
    print("Positional arguments:", args)
    print("Named arguments:", kwargs)

both(1, 2, 3, name="Alice", age=30)  # This will print both positional and named arguments