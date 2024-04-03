import json

# JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON to Python object
data_object = json.loads(json_data)

# Access the object properties
name = data_object['name']
age = data_object['age']
city = data_object['city']

# Print the object properties
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")