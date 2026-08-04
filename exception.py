#HANDLING MISSING FILES
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    # This code runs only if the file does not exist
    print("Error: The file you are looking for does not exist!")


#HANDLING MULTIPLE ERRORS
try:
    num = int(input("Enter a number: "))  # Might raise ValueError if user types "abc"
    result = 100 / num  # Might raise ZeroDivisionError if user types 0

except ValueError:
    print("Error: Please enter numbers only!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

else:
    # Runs ONLY if no error occurred in the try block
    print(f"Success! Result is {result}")

finally:
    # ALWAYS runs regardless of errors (used for cleanup)
    print("Operation finished.")