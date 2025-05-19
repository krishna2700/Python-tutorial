movies_watched = ["Inception", "The Matrix", "Interstellar"]
# user_movies = input("Enter something you like: ")

# if user_movies in movies_watched:
#     print(f"I have watched {user_movies} too!")
# else:
#     print(f"I haven't watched {user_movies} yet.")

number = 7 
user_input = input("Enter 'y' if you wanna play: ")
if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed it right!")
    elif number - user_number in (1, -1):
    # elif abs(number - user_number) == 1:    
        print("You were off by one!")
    else:
        print("Wrong guess, try again!")