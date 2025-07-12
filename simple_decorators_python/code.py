user ={"username":"jose","access_level":"guest"}

def get_admin_password():
    return "1234"

# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"
    

# print(secure_get_admin())  # This will not print anything since user is a guest.    

def make_secure(func):
    def secure_get_admin():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"Access denied: {user['username']} does not have admin privileges."
            # raise PermissionError("You do not have permission to access this resource.")
        
    return secure_get_admin
   
    
get_admin_password = make_secure(get_admin_password)  # This wraps the get_admin_password function with security checks.    


print(get_admin_password())  # This prints the admin password, which is "1234".