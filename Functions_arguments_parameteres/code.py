# def add(x,y):
#     result = x + y
#     print(f"The sum of {x} and {y} is {result}")

# add(5,3)


# def say_hello(name , surname):
#     print("Hello" + " " + name + " " + surname + "!")

# say_hello("Krishna", "Ruparelia")
# say_hello(surname="Krishna", name="Ruparelia")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("Error: Division by zero is not allowed.")

divide(15,5)         
divide(15,0)
divide(divisor=15,dividend=0)