import functools # This is a built-in module that provides higher-order functions for functional programming.

user ={"username":"jose","access_level":"guest"}


# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"
    

# print(secure_get_admin())  # This will not print anything since user is a guest.    

def make_secure(func):
    @functools.wraps(func)  # This decorator preserves the metadata of the original function.
    def secure_get_admin(*args, **kwargs):  # This function checks the user's access level before allowing access to the admin password.
        if user["access_level"] == "admin":
            return func(*args, **kwargs)  # Call the original function with any arguments and keyword arguments.
        else:
            return f"Access denied: {user['username']} does not have admin privileges."
            # raise PermissionError("You do not have permission to access this resource.")
        
    return secure_get_admin
   
@make_secure # This decorator wraps the get_admin_password function with security checks.
def get_password(panel): # This function retrieves the password for a given panel.
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"  
# get_password = make_secure(get_password)      


print(get_password.__name__)  # This prints the name of the function, which is "get_password" due to the @functools.wraps decorator.
print(get_password("billing"))  # This prints the password, which is "1234"