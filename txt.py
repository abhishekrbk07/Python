# WRITING & APPENDING TO TEXT FILES

# 'w' mode creates a new file or overwrites an existing one
with open("notes.txt", "w") as file:
    file.write("Hello, World!\n")  # \n moves to the next line
    file.write("Python is easy to learn.\n")

# 'a' mode appends (adds) new text to the end without deleting anything
with open("notes.txt", "a") as file:
    file.write("This line was added later.\n")

print("Text file written successfully!\n")


# READING TEXT FILES

# 'r' mode opens the file for reading
with open("notes.txt", "r") as file:
    # Read line by line using a loop
    for line in file:
        print(line.strip())  # .strip() removes trailing extra lines