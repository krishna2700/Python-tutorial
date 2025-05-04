vegetables = {"carrot", "tomato", "potato",} 
fruits = {"apple", "banana","tomato"}

local_food = fruits.difference(vegetables) 
# local_food = vegetables.difference(fruits) 
# print(local_food)

food = vegetables.union(fruits)
# print(food)


art = {"Bob", "Alice", "Charlie", "John"}
science = {"Bob", "Alice", "David","Eve"}

both = art.intersection(science)
print(both)