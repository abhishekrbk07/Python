import csv  # Import Python's built-in CSV module

# WRITING TO A CSV FILE

# newline="" prevents empty blank lines on Windows
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the column headers
    writer.writerow(["Name", "Age", "Program"])

    # Write individual rows of data
    writer.writerow(["Ram", 19, "BCS"])
    writer.writerow(["Sita", 20, "BIT"])


# READING FROM A CSV FILE 

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip the header row

    for row in reader:
        # row[0] is Name, row[1] is Age, row[2] is Program
        print(f"Name: {row[0]}, Age: {row[1]}, Program: {row[2]}")