# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print stars in one row
    for col in range(size):
        print("*", end="")
    # Move to the next line after a row is done
    print()
    # Move to the next row
    row += 1
