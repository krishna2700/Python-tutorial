import functools # This is a built-in module that provides higher-order functions for functional programming.

user ={"username":"jose","access_level":"guest"}


# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"
    

# print(secure_get_admin())  # This will not print anything since user is a guest.    

def make_secure(func):
    @functools.wraps(func)  # This decorator preserves the metadata of the original function.
    def secure_get_admin():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"Access denied: {user['username']} does not have admin privileges."
            # raise PermissionError("You do not have permission to access this resource.")
        
    return secure_get_admin
   
@make_secure # This decorator wraps the get_admin_password function with security checks.
def get_admin_password():
    return "1234"    
# get_admin_password = make_secure(get_admin_password)      


print(get_admin_password.__name__)  # This prints the name of the function, which is "get_admin_password" due to the @functools.wraps decorator.
print(get_admin_password())  # This prints the admin password, which is "1234"