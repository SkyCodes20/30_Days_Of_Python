# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

a,b,c,d = 'Thirty ','Days ','Of ','Python '
Concatenated_string = a + b + c + d
print(Concatenated_string)

# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# Cut(slice) out the first word of Coding For All string.
# Check if Coding For All string contains a word Coding using the method index, find or other methods
# Replace the word coding in the string 'Coding For All' to Python.
# Split the string 'Coding For All' using space as the separator (split()) .
# What is the last index of the string Coding For All.
# What character is at index 10 in "Coding For All" string.
# Use index to determine the position of the first occurrence of C in Coding For All.

company ='Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find('Coding'))
print(company.replace('Coding','Python'))
print(company.split())
print(len(company)-1)
print(company[10])
print(company.index('C'))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_name = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_name.split(','))

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
text = "Python For Everyone"

first_letter = text[0]  # Grab the first letter, then find the letters right after each space
second_letter = text[text.find(" ") + 1]
third_letter = text[text.rfind(" ") + 1]

acronym = (first_letter + second_letter + third_letter)

print(acronym)  # Output: PFE


# Create an acronym or an abbreviation for the name 'Coding For All'.
text = "Coding For All"

first = text[0]
second = text[text.find(" ") + 1]
third = text[text.rfind(" ") + 1]

acronym = (first + second + third)
print(acronym)

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
s = '       Coding for All      '
print(s.strip())

# Which one of the following variables return True when we use the method isidentifier():
#  1. 30DaysOfPython
#  2. thirty_days_of_python
# My Answer - thirty_days_of_python will return True because isidentifier() method checks whether a string is a valid variable name or not.

# The following list contains the names of some of Python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
Python_library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(Python_library))

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2
print('The area of the circle with radius {} is {:.0f} meters square'.format(radius,area))

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

x,y = 8,6
print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} / {y} = {x/y:.2f}')
print(f'{x} % {y} = {x%y}')
print(f'{x} // {y} = {x//y}')
print(f'{x} ** {y} = {x**y}')
