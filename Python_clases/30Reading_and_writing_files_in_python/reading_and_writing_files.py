#Reading and Writing Files in Python

#----------------------------------What Is a File?----------------------------------------------
#At its core, a file is a contiguous set of bytes used to store data. This data is organized in a 
# specific format and can be anything as simple as a text file or as complicated as a program executable. 
# In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

#File path
#When you access a file on an operating system, a file path is required. The file path is a string that 
# represents the location of a file. 

#==================================Opening and Closing a File in Python==========================
#When you want to work with a file, the first thing to do is to open it. This is done by invoking the open() 
# built-in function. open() has a single required argument that is the path to the file. open() has a single 
# return, the file object:

""" file = open('dog_breeds.txt') """

#After you open a file, the next thing to learn is how to close it.
#It’s important to remember that it’s your responsibility to close the file. In most cases, upon termination
#  of an application or script, a file will be closed eventually. However, there is no guarantee when exactly 
# that will happen. This can lead to unwanted behavior including resource leaks. It’s also a best practice 
# within Python (Pythonic) to make sure that your code behaves in a way that is well defined and reduces 
# any unwanted behavior.

#When you’re manipulating a file, there are two ways that you can use to ensure that a file is closed properly,
#  even when encountering an error. The first way to close a file is to use the try-finally block:

    """ reader = open('dog_breeds.txt')
        try:
            # Further file processing goes here
        finally:
           reader.close() """

#-------------------The second way to close a file is to use the with statement:-------------------------------

    """ with open('dog_breeds.txt') as reader:
            # Further file processing goes here """

#The with statement automatically takes care of closing the file once it leaves the with block, even in cases 
# of error. I highly recommend that you use the with statement as much as possible, as it allows for cleaner 
# code and makes handling any unexpected errors easier for you.

#Most likely, you’ll also want to use the second positional argument, mode. This argument is a string that 
# contains multiple characters to represent how you want to open the file. The default and most common is 'r', 
# which represents opening the file in read-only mode as a text file:

    """ with open('dog_breeds.txt', 'r') as reader:
            # Further file processing goes here """

# Other options for modes are fully documented online, but the most commonly used ones are the following:

# Character	        Meaning
# 'r'	            Open for reading (default)
# 'w'	            Open for writing, truncating (overwriting) the file first
# 'rb' or 'wb'  	Open in binary mode (read/write using byte data)

