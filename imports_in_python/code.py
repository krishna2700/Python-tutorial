from mymodule import divide # from mymodule import divide as div
import mymodule # import mymodule as mm
import sys


print(divide(10, 2))  # This will print 5.0
print(__name__)  # This will print "__main__" if this script is run directly, or "mymodule" if imported

print(sys.modules)  # This will print the module object of mymodule
print(mymodule.__name__)  # This will print "mymodule"


