a=[]
# b=a
b=[]  # This creates a new list 'b' that is initially empty.

a.append(35)
print(a)  # This will print the list 'a' which contains the element 35
print(b)  # This will also print the same list 'a', since 'b'

print(id(a))  # This will print the memory address of the list 'a'
print(id(b))  # This will print the same memory address as 'a', since 'b' is a reference to 'a'