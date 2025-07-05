# from libs.operations import operator # Assuming 'operator' is a function defined in libs/operations.py

from .operations import operator  # Relative import of the operator module

print("mylibs.py", __name__)  # This will print "mylibs" if this script is imported, or "__main__" if run directly