# Escape
def escape_by(plan):
    print("Please write one of the following statements: jumping over, running around, going deeper")
    x = input()
    if  x == ("jumping over"):
        print("We cannot escape that way! The boulder is too big!")
    elif x == ("running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    else:
        x == ("going deeper")
        print("That might just work! Let's go deeper!")
exit

# Call Escape
escape_by("plan")
print("We cannot escape that way! The boulder is in the way!")
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")

