# https://youtu.be/9N6a-VLBa2I
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-JSON

import json

# 🧠 json.load(f)
# Load json data into Python format

with open('01.Ref - states.json') as f:
    data = json.load(f)

# Check if it is a dictionary
print(type(data))

# ✅ How to print out all items in a dictionary
# Ref - https://stackoverflow.com/q/14547916

for state in data['states']:
    print(state['name'], state['abbreviation'])

print()
"""more in-depth view 👇"""
# print(i['name'])
# print(i['abbreviation'])
# print(i['area_codes'])
# print()

# 🧠 del i['attribute']
# del -> delete
# Delete one attribute from json string

for state in data['states']:
    del state['area_codes']

# 🧠 json.dumps(data, intent=2)
# 😎 much better view with indent=2 !
# Store the "trimmed" data into a new iteration

new_data = json.dumps(data, indent=2, sort_keys=True)

print(new_data)

# Save file into JSON format

with open('01.Ref - New_States.json', 'w') as f:
    json.dump(new_data, f)

# with open('01.Ref - New_States.json') as f:
#     read_new_data = json.load(f)

# print(read_new_data)
