import json

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# JSON data 
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Convert to Python object
data = json.loads(json_data)

# Create Person object from data 
person = Person(name=data['name'], age=data['age'], city=data['city'])

print(person.name)
print(person.age)
print(person.city)
