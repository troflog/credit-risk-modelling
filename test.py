def my_function():
   """
   This is a reST style.

   :param param1: this is a first param
   :param param2: this is a second param
   :returns: this is a description of what is returned
   :raises keyError: raises an exception
   """
   return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)
