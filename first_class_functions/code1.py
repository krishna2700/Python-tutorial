from operator import itemgetter

def search(sequence,expected,finder): # finder is a function
    for item in sequence: # item is an element of sequence
        if finder(item) == expected: # if finder(item) is equal to expected 
            return item # return the item


friends = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 27}
]

def find_by_name(friend):
    return friend['name']  # This function returns the name of the friend


print(search(friends, 'Charlie', find_by_name))  # This searches for the friend with the name 'Alice' using the find_by_name function.
print(search(friends, 25, lambda friend: friend['age']))  # This searches for the friend with the age 25 using a lambda function.
print(search(friends, 30, lambda friend: friend['age']))  # This searches for the friend with the age 30 using a lambda function.
print(search(friends, 'Alice', lambda friend: friend['name']))  # This searches for the friend with the name 'Alice' using a lambda function.
print(search(friends, 'sssz', lambda friend: friend['name']))  # This searches for the friend with the name 'sssz' using a lambda function, which will return None since no such friend exists.
print(search(friends, 'Alice', itemgetter('name')))  # This searches for the friend with the name 'Alice' using the itemgetter function from the operator module.
print(search(friends, 30, itemgetter('age')))  # This searches for the