def divide(dividend,divisor):
    return dividend / divisor

print("mymodule.py", __name__) # This will print "mymodule" if this script is imported, or "__main__" if run directly

import libs.mylibs  # import libs as lb