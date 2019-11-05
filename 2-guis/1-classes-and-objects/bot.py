class Bot:
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display(self):
        #Name
        print("##########")
        print("#  {}   #".format(self.name))
        print("##########")  
        print()

        #Cake
        print("    {}    ".format(self.age))
        print("##########")
        print("~~~~~~~~~~")
        print("##########")
        print()

       #Bars
        print("||||| = {}".format(self.energy))
        print()

       #Shield
        print("  |`-.__/\__.-`|")
        print("  |     ||     |")
        print("  |____o()o____|")
        print("  |__((<{}>))__|".format(self.shield))
        print("  \    o\/o    /")
        print("   \    ||    /")
        print("    \   ||   /")
        print("     '..||..'")
        print("        ``")

robot = Bot("Bob", 18, 5, 94)

robot.display()

__str__
