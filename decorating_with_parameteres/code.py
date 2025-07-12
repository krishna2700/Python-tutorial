import functools  # This is a built-in module that provides higher-order functions for functional programming.
user = {"username": "jose", "access_level": "guest"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)  # This decorator preserves the metadata of the original function.
        def secure_get_admin(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)  # Call the original function with any arguments and keyword arguments.
            else:
                return f"Access denied: {user['username']} does not have {access_level} privileges."
                # raise PermissionError("You do not have permission to access this resource.")

        return secure_get_admin

    return decorator


@make_secure("admin") # This decorator wraps the get_password function with security checks.
def get_password():  # This function retrieves the password for a given panel.
    return "admin: 1234"

@make_secure("user") # This decorator wraps the get_password function with security checks.
def get_dashboard_password():
    return "user: user_password"

print(get_password())  # This prints the admin password, which is "admin: 1234"
print(get_dashboard_password())  # This prints the dashboard password, which is "user: user

user = {"username": "anne", "access_level": "admin"}

print(get_password())  # This prints the admin password, which is "admin: 1234"
print(get_dashboard_password())  # This prints the dashboard password, which is "user: user_password"
