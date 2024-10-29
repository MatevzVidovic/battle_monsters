import json
import base64



import argparse
import os
import json

def load_json_data(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Open and load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data



# Create the argument parser
parser = argparse.ArgumentParser(description='Load JSON data from a file path.')
# Add an optional positional argument with a default value
parser.add_argument('dir_path', nargs='?', default=os.getcwd(), help='Path to the file')

# Parse the arguments
args = parser.parse_args()


dir_path = args.dir_path



for filename in os.listdir(dir_path):
        if filename.endswith('.json'):

            file_path = os.path.join(dir_path, filename)

            # Load the JSON data
            try:
                data = load_json_data(file_path)
                print("Loaded JSON data:", data)
            except FileNotFoundError as e:
                print(e)
            except json.JSONDecodeError:
                print("Failed to decode JSON from the file.")


            print(data)


            img_name = data['img_name']
            img_path = os.path.join(dir_path, img_name)
            with open(img_path, 'rb') as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode('utf-8')


            data['img'] = img_base64

            # Write data to a JSON file
            with open(os.path.join(dir_path, (data["card_name"] + "_patched.json")), 'w') as file:
                json.dump(data, file, indent=4)

            print("JSON file created successfully.")