class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def __repr__(self): 
        return f"Person(name={self.name!r}, age={self.age!r})" 

bob = Person("Krishna", 24)
print(bob) 