#-------------------------Django Environment Variables and Django Templating-----------------------------------
# An environment variable is a value that can affect the way running process will behave on a computer.
#  They are part of the environment in which a process runs. These variables are set outside the program 
#through functionalities built into the operating system, microservcie, or web framework.

#Environment variable are made up of name value pairs, for instance 
# SECRET_KEY="F1209051SKDlgsfgfgref", where the name is " SECRET_KEY" and value is "F1209051SKDlgsfgfgref".
#Environment variable were introduces in their modern form in 1979 with version 7 unix, so are included in 
#all Unix operating system flavors and variant from that point onward including linux and macOS.

# -------------Why environment variables?-----------------------------------------------------
#Environment variables help secure our apps by keeping sensitive bits of code like API keys and passwords 
# away from prying eyes and hackers on the internet, storing passwords or other sensitive information in your
#version control system, like Git, is never a good idea.
# So instead of setting the password directly in the configuration files in your codebase, you can use a 
# reference to your .gitignore file so that Git knows to exclude this particular file on your next commit

#READ UP BEST SRCURITY PRATICES IN DJANGO DOCUMENTATION 
#HERE https://docs.djangoproject.com/en/3.2/topics/security/  

#-----------Demostrate how to keep your environment variable safe in Django using virtual environment ---------

#But first, What Is a Virtual Environment?
#At its core, the main purpose of Python virtual environments is to create an isolated environment for Python 
# projects. This means that each project can have its own dependencies, regardless of what dependencies every 
# other project has.
#A virtual environment  also is a Python environment such that the Python interpreter, libraries and scripts 
# installed into it are isolated from those installed in other virtual environments, and (by default) any 
# libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.

#In our little example above, we’d just need to create a separate virtual environment for both ProjectA and 
# ProjectB, and we’d be good to go. Each environment, in turn, would be able to depend on whatever version of 
# ProjectC they choose, independent of the other.
#The great thing about this is that there are no limits to the number of environments you can have since 
# they’re just directories containing a few scripts. Plus, they’re easily created using the virtualenv or 
# pyenv command line tools.


#---------------Using Virtual Environments-----------------------------------------------
#To get started, if you’re not using Python 3, you’ll want to install the virtualenv tool with in ubuntu---->
#pip3 install virtualenv


#Start by making a new directory to work with:------->
#$ mkdir python-virtual-environments && cd python-virtual-environments

# Create a new virtual environment inside the directory:---------->
# Python 3
# $ python3 -m venv <name the file>

#venv — Creation of virtual environments
#The venv module provides support for creating lightweight “virtual environments” with their own site 
# directories, optionally isolated from system site directories. Each virtual environment has its own Python 
# binary (which matches the version of the binary that was used to create this environment) and can have its 
# own independent set of installed Python packages in its site directories.

#In the above command using venv, this command creates a directory , which contains a directory files which are
# bin: files that interact with the virtual environment
# include: C headers that compile the Python packages
# lib: a copy of the Python version along with a site-packages folder where each dependency is installed

#More interesting are the activate scripts in the bin directory. These scripts are used to set up your shell 
# to use the environment’s Python executable and its site-packages by default.
#In order to use this environment’s packages/resources in isolation, you need to “activate” it. 