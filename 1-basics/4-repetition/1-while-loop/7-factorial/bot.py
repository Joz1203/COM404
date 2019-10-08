print("Please enter a number:")
user_response = int(input())
print()
answer = user_response
count = user_response - 1
while count > 0:
    answer = answer * count 
    count = count - 1

print("The factorial is" ,answer)