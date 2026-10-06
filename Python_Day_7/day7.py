# Exercises: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Nvidia','Infosys','Tata','Wipro'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

# What is the difference between remove and discard

# ANSWER: remove gives an error if the item is not in the set whereas discard doesn't give any errors in case if the item is not found.

# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
result = A.union(B)
print(result)

# Find A intersection B
A.intersection(B)
print(A)

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
A.update(B); print(A)
B.update(A); print(B)

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B

# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
length_list_age = len(age)
length_set_age = len(set_age)
print(set_age)
print(length_list_age > length_set_age)

# Explain the difference between the following data types: string, list, tuple and set

#ANSWER: Strings are ordered and not mutable, modifying them creates a new string instead, any data type written within ' ' or " " or ''' ''' or """ """ is a string.
#        Lists are mutable, modifiable and written within '[ ]' brackets.
#        Tuple are not mutable, not modifiable directly, ordered and written within '( )' brackets.
#        Set is unordered and un-indexed and it contains unique elements. a set itself is mutable but the elements inside a set must be immutable.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = 'I am a teacher and I love to inspire and teach people'
split_sentence = sentence.split(' ')
print(split_sentence)
set_unique = set(split_sentence)
print('Number of unique element in the sentence is:', len(set_unique))
