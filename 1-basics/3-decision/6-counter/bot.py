print("Please enter the first whole number.")
first_number = int(input())
print("Please enter the second whole number.")
second_number = int(input())
print("Please enter the third whole number.")
third_number = int(input())
even_count = 0
odd_count = 0
if (first_number % 2 == 0):
    even_count = even_count + 1
else: odd_count += 1
if (second_number % 2 == 0):
    even_count = even_count + 1
else: odd_count += 1
if (third_number % 2 == 0):
    even_count = even_count + 1
else: odd_count += 1
print("There were " + str(even_count) + " even and " + str(odd_count) + " odd numbers.")  