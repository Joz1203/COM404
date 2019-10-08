print("How many numbers should I sum up?")
user_response = int(input())
print()
answer = 0
count = 0
while count < user_response:
    count = count + 1
    print("Please enter number "+str(count)+" of "+str(user_response)+":")
    number = int(input())
    answer += number
print()
print("The answer is "+str(answer)+".")