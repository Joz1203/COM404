# Amount of rows
print("How many rows should I have?")
rows = int(input())
print()

# Amount of columns
print("How many columns should I have?")
columns = int(input())
print()
print("Here I go...")
print()

# Display
for count in range (0, rows, 1):
    for number in range(0, columns, 1):
        print(":-) ", end="")
    print()

print()
print("Done!")