class Person:
    def __init__(self, name):
        self.name = name
        self.father = None

    def set_father(self, father):
        self.father = father

# Create persons involved in the riddle
speaker = Person("Speaker")
that_man = Person("That Man")

# Setting up the relationship (that man's father is speaker's father's son)
speaker.set_father(Person("Father"))
that_man.set_father(speaker)

# Solve the riddle
if that_man.father == speaker:
    print(f"That man is the speaker's son.")
else:
    print(f"Cannot deduce the relationship.")