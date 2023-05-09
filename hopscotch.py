# This little task was a technical test in a recruitment process.

# A child (Object) is playing hopscotch, 
# the grid has 100 consecutive squares.

# If the number of the square is an even number, the child shouts "Coca!"
# If the number is evenly divisable by 5, the child shouts "Cola!"
# If the number is even and evenly divisable by 5, the child shouts "Coca Cola!"

class Child:
    def __init__(self, name):
        self.name = name

    def shout(self):
        for i in range(1, 101):
            if i % 2 == 0:
                if i % 5 == 0:
                    print(i, "Coca Cola!")
                else: 
                    print(i, "Coca!")
            elif i % 5 == 0:
                print(i, "Cola!")

c1 = Child("Anna") 

c1.shout()
