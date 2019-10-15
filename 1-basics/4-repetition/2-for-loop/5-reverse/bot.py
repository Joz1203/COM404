# User Phrase
print("What phrase do you see?")
phrase = input()

#reverse phrase
print()
print("Reversing...")
print()
print("The phrase is ", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")