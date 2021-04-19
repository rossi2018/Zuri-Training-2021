#-----------------OS model----------------------------
#The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s 
# standard utility modules. This module provides a portable way of using operating system-dependent 
# functionality. The *os* and *os.path* modules include many functions to interact with the file system.

#-------------------Handling the Current Working Directory-----------------------------------
#Consider Current Working Directory(CWD) as a folder, where the Python is operating. Whenever the files are 
# called only by their name, Python assumes that it starts in the CWD which means that name-only reference will
#  be successful only if the file is in the Python’s CWD.
#Note: The folder where the Python script is running is known as the Current Directory. This is not the path 
# where the Python script is located.

#--------------Getting the Current working directory------------------------------------------
#To get the location of the current working directory os.getcwd() is used.

# Python program to explain os.getcwd() method 
          
# importing os module 
import os

# Get the current working 
# directory (CWD) 
cwd = os.getcwd() 
      
# Print the current working 
# directory (CWD) 
print("Current working directory:", cwd) 

print('Changing the Current working directory------------------------------------------------')
#----------------Changing the Current working directory-----------------------------------------
#To change the current working directory(CWD) os.chdir() method is used. This method changes the CWD to a 
# specified path. It only takes a single argument as a new directory path.

#Note: The current working directory is the folder in which the Python script is operating.



# Python program to change the current working directory 
    
import os


# Function to Get the current  
# working directory 
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
    
    
# Driver's code 
# Printing CWD before 
current_path() 
    
# Changing the CWD 
""" os.chdir('../')  """  #can uncomment later to see how it works for real 
    
# Printing CWD after 
current_path() 

print('Listing out Files and Directories with Python---------------------------------------------------')

#os.listdir() method in Python is used to get the list of all files and directories in the specified directory.
#  If we don’t specify any directory, then list of files and directories in the current working directory will
#  be returned.

# Python program to explain os.listdir() method 
      
# importing os module 
import os 
  
# Get the list of all files and directories 
# in the root directory 
path = "/"
dir_list = os.listdir(path) 
  
print("Files and directories in '", path, "' :") 
  
# print the list 
print(dir_list) 