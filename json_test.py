import json
with open('file1.json', 'r') as file:
    data = json.load(file)

print(data)


# Writing JSON data to a file
with open('data.json', 'w') as file:
    json.dump(python_dict, file, indent=4, sort_keys=True)
print("done")