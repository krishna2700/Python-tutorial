numbers = [1,3,5]

doubled = [x * 2 for x in numbers]

# for num in numbers:
#     doubled.append(num * 2)


# print(doubled)


friends = ["Sam", "Alex", "Jordan", "Taylor","Saura"]

starts_s=[friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)
print(friends)
print(starts_s)

print(friends is starts_s)  # False, they are different lists

print("friends", id(friends), "starts_s", id(starts_s))  # Different IDs, different lists