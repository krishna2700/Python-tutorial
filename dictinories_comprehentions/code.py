users = [
    (0,"Krishna", "password123"),
    (1,"Ravi", "password456"),
    (2,"Sita", "password789"),
    (3,"Gita", "password1011"),
]

username_mapping = {user[1]: user for user in users}
# print(username_mapping)

username_input = input("Enter your username: ")
username_password = input("Enter your password: ")

_,username, password = username_mapping[username_input]

if username_password == password:
    print(f"Welcome {username}!")
else:
    print("Invalid username or password. Please try again.")


