# Declare an empty list
lst = list()
print(lst)

# Declare a list with more than 5 items
# Find the length of your list
# Get the first item, the middle item and the last item of the list

fruits = ['apple', 'banana', 'orange', 'mango', 'papaya']
print(len(fruits))
print(fruits[0::2])

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# Print the list using print()
# Print the number of companies in the list
# Print the first, middle and last company
# Print the list after modifying one of the companies
# Add an IT company to it_companies
# Insert an IT company in the middle of the companies list
# Change one of the it_companies names to uppercase (IBM excluded!)
# Join the it_companies with a string '#;  '
# Check if a certain company exists in the it_companies list.
# Sort the list using sort() method
# Reverse the list in descending order using reverse() method
# Slice out the first 3 companies from the list
# Slice out the last 3 companies from the list
# Slice out the middle IT company or companies from the list
# Remove the first IT company from the list
# Remove the middle IT company or companies from the list
# Remove the last IT company from the list
# Remove all IT companies from the list
# Destroy the IT companies list

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[::3])
it_companies[3] = 'Samsung'
print(it_companies)
it_companies.append('Apple')
it_companies.insert(len(it_companies)//2, 'Netflix')
print(it_companies)
it_companies[2] = it_companies[2].upper()
print(it_companies)
x = '#; '.join(it_companies)
print(x)
print('Google' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[3:])
print(it_companies[:-3])
print(it_companies)
print(it_companies[len(it_companies)//2:(len(it_companies)//2)+1])
del it_companies[0]
print(it_companies)
del it_companies[len(it_companies)//2-1:len(it_companies)//2+1]
print(it_companies)
del it_companies[len(it_companies)-1]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
# print(it_companies)

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_list = front_end + back_end
print(new_list)

# After joining the lists. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = new_list.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

# Exercises: Level 2

# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('Min age is:', min(ages) , '\nMax age is:', max(ages))
ages.append(max(ages))
ages.append(min(ages))
print(ages)
median_age = (ages[(len(ages)//2)-1] + ages[len(ages)//2])/2
print(median_age)
ages.sort()
average_age = sum(ages)/len(ages)
print(average_age)
range_of_ages = max(ages) - min(ages)
print(range_of_ages)
value1 = min(ages) - average_age
value2 = max(ages) - average_age
print('absolute value of min-average is',abs(value1))
print('absolute value of max-average is',abs(value2))
print("min-average is > than max-average?",abs(value1)>abs(value2))

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic = country_list
print(first)
print(second)
print(third)
print(scandic)