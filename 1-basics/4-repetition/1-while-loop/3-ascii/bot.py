print("How many bars should be charged?")
bars = int(input())
print()
count = 0
while count < bars:  
    count = count + 1
    print("Charging: ", "█ " * count)

print()
print("The battery is fully charged.")