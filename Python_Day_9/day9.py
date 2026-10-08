# Get user input using input(“Enter your age: ”). If user is 18 or older,
# give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.
from traceback import print_tb

age = int(input('Enter your age: '))
if age > 18:
    print('You are old enough to drive')
else:
    print(f'You need to wait {18-age} more years to learn to drive')

# Compare the values of my_age and your_age using if … else.
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

your_age = int(input('Enter your age: '))
my_age = 20

if your_age >= my_age:
    if your_age == (my_age + 1):
        print(f'You are {your_age-my_age} year older than me')
    elif your_age==my_age:
        print(f'We are of same age')
    else:
        print(f'You are {your_age-my_age} years older than me')
else:
    if my_age == (your_age+1):
        print(f'I am {my_age-your_age} year older than you')
    else:
        print(f'I am {my_age-your_age} years older than you')

# Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if a==b:
    print (f'{a} and {b} are equal')
else:
    print( f'{a} is greater than {b}' if(a>b) else f'{a} is smaller than {b}')

# Write a code which gives grade to students according to theirs scores:

# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F

score = int(input('Enter your score: '))

if score > 100 or score < 0:
    print('Invalid score')
elif score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('F')

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring.
# June, July or August, the season is Summer.

month = input('Enter a month: ').title()

if month not in ['January','February','March','April','May','June','July','August','September','October','November','December']:
    print('Invalid: month doesn\'t exist')
elif month in ['December','January','February']:
    print('Winter season')
elif month in ['March','April','May']:
    print('Spring season')
elif month in ['June','July','August']:
    print('Summer season')
else:
    print('Autumn season')

# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the given list, add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruit = input('Enter your favourite fruit: ').lower()
fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('Fruit already exists in the given list')

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end developer'),
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title')
# - for more accurate results more conditions can be nested!
# *If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland.He is married.

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
    if 'Python' in person['skills']:
        print('The person knows Python')

user_skills  = set(person['skills'])

if {'JavaScript','React'} == user_skills:
    print ('He is a front end developer')
elif {'React','Node','MongoDB'}.issubset(user_skills):
    print('He is a fullstack developer')
elif {'Node','Python','MongoDB'}.issubset(user_skills):
    print('He is a backend developer')
else:
    print('Unknown-title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in Finland. He is Married' )

