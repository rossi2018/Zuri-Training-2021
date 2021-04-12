# String formating allow us to decide how the string is printed out
name = 'Mike'  # string -s
age = 55  # Digits - d

print('His name is %s and he is %d years old' % (name, age))

# You can also used the string formating to print out items in list
sampleList = ['Mike', 'Love', 'Dove', 55]

print('some text %s' % sampleList)

# You can still select items from the sampleList like this
print('Lists %s ' % sampleList)

# To no the length of string use len
string = 'I am a string'
string2 = 'Mike b'
string3 = 'UPPERCASE STRING'

print(len(string))
print(len(string2))

# To get the position of a particular letter in a string use index() function
print(string2.index('k'))

# To get the count of a letter in a string use count() function
print(string2.count('e'))
print(string.count('a'))
print(string2.count('Mike'))
print(string2.count('o'))  # o doesnt exist so it returns 0
print(string2.count(' '))  # It returns 1 which is the space i string2

# To print sub string
print(string[1:8])

# To convert string to upper case
print(string.upper())

# You can also convert string to lower
print(string3.lower())

# You might revers a string like this
print(string3[::-1])

# You can check if a string start with a particular term like this
print(string.startswith('I'))  # True
print(string.startswith('p'))  # False

# And also check if a string ends with a particuar letter like this
print(string.endswith('string'))  # True
print(string.endswith('shifrtr'))  # False

print('f-Strings: A New and Improved Way to Format Strings in Python.....................................')
# f-string:Also called “formatted string literals,” f-strings are string literals that have an f at the
# beginning and curly braces containing expressions that will be replaced with their values.

# The expressions are evaluated at runtime and then formatted using the __format__ protocol.
name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")

# It would also be valid to use a capital letter F:
print(F"Hello, {name}. You are {age}.")

print('Arbitrary Expressions----------------------------------------------------------------------------')
# Because f-strings are evaluated at runtime, you can put any and all valid Python expressions in them.
# This allows you to do some nifty things.
# You could do something pretty straightforward, like this:
print(f"{2 * 37}")

print('You could also call functions--------------------------------------------------------------------')


def to_lowercase(input):
    return input.lower()


name = 'Eric Idle'
print(f'{to_lowercase(name)} is funny')

print('Calling a method directly=======================================================================')
# You also have the option of calling a method directly:

print(f'{name.lower()} is funny.')

print('You could even use objects created from classes with f-strings----------------------------------')
# You could even use objects created from classes with f-strings. Imagine you had the following class:


class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


# You’d be able to do this:
new_comedian = Comedian("Eric", "Idle", "74")
print(f'{new_comedian}')

# The __str__() and __repr__() methods deal with how objects are presented as strings, so you’ll need
# to make sure you include at least one of those methods in your class definition. If you have to pick
# one, go with __repr__() because it can be used in place of __str__().

# The string returned by __str__() is the informal string representation of an object and should be readable.
#  The string returned by __repr__() is the official representation and should be unambiguous. Calling str()
#  and repr() is preferable to using __str__() and __repr__() directly.

# By default, f-strings will use __str__(), but you can make sure they use __repr__() if you include the
# conversion flag !r:
print(f"{new_comedian}")

print(f"{new_comedian!r}")

print('Multiline f-Strings----------------------------------------------------------------------------------')
name2 = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name2}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
    # But remember that you need to place an f in front of each line of a multiline string.
)
print(message)

print('The f in f-strings may as well stand for “fast.”-----------------------------------------------------')
# f-strings are faster than both %-formatting and str.format(). As you already saw, f-strings are expressions
#  evaluated at runtime rather than constant values. Here’s an excerpt from the docs:

# “F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should
#  be noted that an f-string is really an expression evaluated at run time, not a constant value. In Python
# source code, an f-string is a literal string, prefixed with f, which contains expressions inside braces.
# The expressions are replaced with their values.” (Source)

# At runtime, the expression inside the curly braces is evaluated in its own scope and then put together with
# the string literal part of the f-string. The resulting string is then returned. That’s all it takes.

# Here’s a speed comparison:
