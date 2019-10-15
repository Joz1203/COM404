#user input brightness level
print("What level of brightness is required?")
brightness = int(input(""))
print()
print("Adjusting brightness...")
print()

for number in range(2, brightness + 1, 2):
    print("Beep's brightness level:", number * "*")
    print("Bop's brightness level:", number * "*")
    print()
print("Adjustments complete!")