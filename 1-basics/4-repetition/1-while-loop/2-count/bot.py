print("How many live cables should I avoid?")
amount = int(input(""))
count = 0
while count in amount:  
    print("Avoiding...Done!" , count, "live cables avoided")
    count = count + 1
    
print("All live cables have been avoided.")