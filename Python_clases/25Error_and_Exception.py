#What is Exception?
#An exception is an event, which occurs during the execution of a program that disrupts the normal flow of
#  the program's instructions. In general, when a Python script encounters a situation that it cannot cope
#  with, it raises an exception. An exception is a Python object that represents an error.

#When a Python script raises an exception, it must either handle the exception immediately otherwise it 
# terminates and quits.

# Handling Exceptions
#It is possible to write programs that handle selected exceptions. Look at the following example, which asks
#  the user for input until a valid integer has been entered, but allows the user to interrupt the program 
# (using Control-C or whatever the operating system supports); note that a user-generated interruption is 
# signalled by raising the KeyboardInterrupt exception.

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

#The try statement works as follows.
#1. First, the try clause (the statement(s) between the try and except keywords) is executed.

#2. If no exception occurs, the except clause is skipped and execution of the try statement is finished.

#3. If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if 
#its type matches the exception named after the except keyword, the except clause is executed, and then 
#execution continues after the try statement.

#4. If an exception occurs which does not match the exception named in the except clause, it is passed on to 
# outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message 
# as shown above.


print('Raising an exception ================================================================================')
# If you want to throw an error when a certain condition occurs using raise, you could go about it like this:
#The raise statement allows the programmer to force a specified exception to occur. For example:

#Example 1 
""" y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed")  """ #To comment press ALT+SHIFT+A 

#Example 2
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
