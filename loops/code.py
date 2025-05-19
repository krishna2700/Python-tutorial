
# number = 7 
# while True:
#     user_input = input("would you like to play? (y/n): ").lower()
#     if user_input == "n":
#         break
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed it right!")
#     # elif number - user_number in (1, -1):
#     elif abs(number - user_number) == 1:    
#         print("You were off by one!")
#     else:
#         print("Wrong guess, try again!")


# friends = ["Alice", "Bob", "Charlie", "David",]

# for friend in friends:
#     print(f"Hello, {friend}!")

grades = [85, 90, 78, 92, 88]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total/amount)    



       