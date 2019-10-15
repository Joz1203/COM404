#User input markings found
print("What strange markings do you see?")
markings = input()
print()

#Identify the markings
print("Identifying ...")
print()

#display markings
for number in range(0, len(markings), 1):
    print("index", number, ":", markings[number])