# Create an empty dictionary called dog
dog = {} # dog = dict()

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Tyson'
dog['color'] = 'Brown'
dog['breed'] = 'Pitbull'
dog['legs'] = 4
dog['age'] = 2

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Stonics',
    'last_name': 'Lite',
    'gender': 'Male',
    'age': 20,
    'is_married': False,
    'skills': ['mysql','CSS','HTML','JS','React','Python','Java','DevOps'],
    'country': 'USA',
    'city':'New York',
    'address': {
        'Street':'Near Times Square',
        'pincode': 5656565
    }
}
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('Django')
print(student)

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.popitem() #student.pop('skills') #del student['skills']
print(student)

# Delete one of the dictionaries
del student
