# User Sequence
print("Please enter a squence")
sequence = input()
print()

# User Marker
print("Please enter a character for the marker")
marker = input()
print()

# Find markers
marker1_position = -1
marker2_position = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if (letter == marker):
        if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position

# Display result
print("The distance between the markers is", marker2_position - marker1_position - 1)