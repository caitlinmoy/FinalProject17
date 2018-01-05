class Character(object):
    """character template"""
    def __init__(self, name):
        self.name = name
        self.gp = 100 #gp stands for "grade points"
        self.sp = 100 #sp stands for "self-esteem points"

    def bang_head_against_wall(self):
        """deducts 5 points from sp"""
        self.sp -=5
        print("You lost 5 self-esteem points")

print(input("""Instructions go here
To continue, press [ENTER]"""))

print(input("story intro. Press [ENTER]"))

def choice_1():
    choice = ""
    while choice != "a" and choice != "b":
        choice = input("""It’s 7:48 and you know you’re a slow walker.
Do you cut across the grass like a barbarian, or walk along the pathway?
a  I’m a barbarian
b  Walk along pathway

Type A or B: """)

    if choice is "a":
        print("You cut across the grass. You feel ashamed, but you make it to school on time.")
    else:
        print("INSERT TEXT HERE")

choice_1()
