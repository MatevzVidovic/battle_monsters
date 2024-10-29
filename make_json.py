import json
import base64

# Define the data as a Python dictionary
data = {
    'card_name': 'Alice',
    'level': 30,
    'effect': 'New York',
    'img_path': 'cards/alice.png',
}

img_path = data['img_path']
with open(img_path, 'rb') as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode('utf-8')


data['img'] = img_base64

# Write data to a JSON file
with open('cards/alice.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully.")