from Python_Day_10.data import data
from Python_Day_10.countries import countries

# Iterate 0 to 10 using for loop, do the same using while loop.

for number in (range(11)):
    print(number)

num = 0
while num <=  10:
    print(num)
    num += 1

# Iterate 10 to 0 using for loop, do the same using while loop.

lst = [0,1,2,3,4,5,6,7,8,9,10]
lst.sort(reverse=True)
for number in lst:
    print(number)

num = 10
while num>=0:
    print(num)
    num -= 1


# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#
##
###
####
#####
######
#######

for i in range(1,8):
    for j in range(i):
        print('#', end="")
    print()

# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(1,9):
    for j in range(1,9):
        print('# ', end="")
    print()

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(1,11):
    print(f'{i} x {i} = {i*i}')

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)

# Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(0,101,2):
    print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(1,101,2):
    print(i)

# Exercises: Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

sum = 0
for i in range(0,101):
    sum += i
print(sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

even_sum , odd_sum = 0,0
for i in range(0,101):
    if i%2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f'The sum of even numbers is {even_sum} and the sum of odd numbers is {odd_sum}')

# Go to the data folder and use the data.py file. Loop through the countries and extract all the countries containing the word land.

for country in countries:
    if 'land' in country:
        print(country, end = ", ")

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']

for reversed_fruits in fruits[::-1]:
    print(reversed_fruits)

# Go to the data folder and use the countries_data.py file.

# What are the total number of languages in the data

total_languages = set()
for country in data:
    for language in country['languages']:
        total_languages.add(language)
print('total number of languages in the data is',len(total_languages))

# Find the ten most spoken languages from the data

language = dict()
for country in data:
    for most_spoken in country['languages']:
        language[most_spoken] = language.get(most_spoken,0)+1

lst = []
for key, values in language.items():
    lst.append((values,key))

lst.sort(reverse=True)

ten_languages = lst[:10]

for count,lang in ten_languages:
    print(f'{lang} is spoken in {count} countries')

# Find the 10 most populated countries in the world

lst = []
for country in data:
    lst.append((country['population'],country['name']))

lst.sort(reverse = True)

top_ten = lst[:10]

for population,country in top_ten:
    print(f'{country} has population {population}')