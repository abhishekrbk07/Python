import csv

students = [
    {"name": "Ram", "marks": 85},
    {"name": "Sita", "marks": 92},
]

# Write using field names
with open("results.csv", "w", newline="") as file:
    fields = ["name", "marks"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()  # Write column titles
    writer.writerows(students)  # Write all list entries

# Read using column names
with open("results.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} scored {row['marks']}")