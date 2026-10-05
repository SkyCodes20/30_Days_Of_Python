# Create an empty tuple
empty_tuple = ()    # or empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('sam','vam','gamma','alpha','beta','sigma')
sisters = ('vena','mena','gena','lena','dena')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
print('Total siblings',len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
father, mother = 'him', 'her'
family_members = siblings + [father,mother]
family_members = tuple(family_members)
print(family_members)

# Unpack siblings and parents from family_members
*siblings,father,mother = family_members
print(siblings)
print(father,mother)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana','apple','mango')
vegetables = ('potato','tomato')
animal_products = ('milk','egg')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid_element = food_stuff_tp[:(len(food_stuff_tp)-1)//2] + food_stuff_tp[len(food_stuff_tp)//2+1:]
print(mid_element)


# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[3:-3])

# Delete the food_stuff_tp tuple completely
del food_stuff_tp
print(food_stuff_tp)  #NameError