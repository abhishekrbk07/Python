import json  # Import Python's built-in JSON module

# Sample data dictionary
user_profile = {
    "name": "Ram Sharma",
    "age": 19,
    "subjects": ["Python", "Math"],
    "active": True,
}

# --- SAVING DATA TO JSON (dump) ---
with open("profile.json", "w") as file:
    # json.dump converts Python dictionary to JSON format and saves it
    # indent=4 makes the JSON text clean and readable
    json.dump(user_profile, file, indent=4)

print("JSON file saved!\n")


# --- LOADING DATA FROM JSON (load) ---
with open("profile.json", "r") as file:
    # json.load reads JSON and converts it back into a Python dictionary
    data = json.load(file)

print(f"Loaded Name: {data['name']}")
print(f"Loaded Subjects: {data['subjects']}")