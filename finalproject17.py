# Game in which the player must make it through a normal Magnet school day

class Character(object):
    """character template"""
    def __init__(self, name):
        self.name = name
        self.gp = 100 #gp stands for "grade points"
        self.sp = 100 #sp stands for "self-esteem points"

    def bang_head_against_wall(self):
        """deducts 5 points from sp"""
        self.sp -= 5
        print(input('''You lost 5 self-esteem points.

[ENTER]'''))

    def powerschool(self):
        print(input(f'''You have {you.sp} self-esteem points.
You have {you.gp} grade points.

[ENTER]'''))


you = Character("you") #How the player is referred to the entire game



def end_game():
    if you.sp <= 0 or you.gp <= 0:
        print(input('''Magnet is too much for you.

You go back to your home district.

[ENTER]'''))
        exit()

print(input('''___WELCOME PUT TEXT HERE LATER_____________________.
To continue, press [ENTER]''')) # game introduction


# Choice_1: Has two options
# If the player inputs anything other than 'a' or 'b', the question will repeat itself
def choice_1():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b":
        choice = input('''The lovely smell of bus fumes at 7:55 AM fills the air. You know you’re a slow walker.
Do you cut across the grass like a barbarian, or walk along the pathway?
 a  I’m a barbarian
 b  Walk along pathway

Type a or b: ''')

    if choice is "a":
        print("\033[H\033[J") #clears screen
        print(input('''You cut across the grass and trip on a rock. Good. You deserve it.

[ENTER]'''))
        choice_2() #leads to choice_2
    else:
        print("\033[H\033[J") #clears screen
        print(input('''You walk the entire length of the pavement, taking in your surroundings.

The sun illuminates the sky. A flock of geese fly by. The gnome in the window of the magnet senior lounge waves “hi.”

[ENTER] '''))
        print("\033[H\033[J")
        print(input('''You’re so lost in the moment that you trip over a student who stopped to tie his shoelaces in the middle of the path.

You break your nose.

Minus 10 self-esteem points.

[ENTER]'''))
        you.sp -= 10
        choice_2()

def choice_2():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice !="b":
        print(input('''You approach the front doors of Magnet. Someone holds the door open for you. You give them a pat on the back.

[ENTER]'''))
        print("\033[H\033[J")
        choice = input('''You go to swipe in, but realize your lanyard isn’t hanging around your neck.

Do you wear a temporary ID or not?

 a  Wear temporary ID
 b  Don't wear temporary ID

 Type a or b: ''')

    if choice is "a":
        print("\033[H\033[J")
        print(input('''You wear your temporary ID. Three freshmen walk by and make fun of you.

Minus 10 self-esteem points.

[ENTER]'''))
        you.sp -= 10
        print("\033[H\033[J")
        print(input('''You see __NAME__ waving to you from down the hallway

[ENTER]'''))
        print("\033[H\033[J")
        print(input('''__NAme__: Hey! Did you know if you check Powerschool you can see how many self-esteem points and grade points you have?!?

[ENTER]'''))
        print(input('''You: What?

[ENTER]'''))
        print(input('''__Name__: What?

[ENTER]'''))
        print(input('''__Name__: Barrel-rolls away

[ENTER]'''))
        print("\033[H\033[J")
        print(input(''' You continue on to your locker on the second floor

[ENTER]'''))
        choice_3()

    if choice is "b":
        print("\033[H\033[J")
        print(input('''You take the green sticker, rip it in half and stomp on it.

[ENTER]'''))
        print("\033[H\033[J")
        print(input('''Mr. Rafalowski sees the whole thing and lets out a disapproving sigh.

[ENTER]'''))
        print("\033[H\033[J")
        print(input('''You try to tape the pieces back together, but in doing so, you lose all your dignity.

Minus 100 self-esteem points.

[ENTER]'''))
        you.sp -= 100
        end_game()

def choice_3():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''Do you remember your locker combination?

 a  10-14-35
 b  Nope
 c  powerschool

Type a, b, or c: ''')
        if choice is "a":
            print("\033[H\033[J")
            print(input('''You remembered correctly!

Plus 5 self-esteem points.

[ENTER]'''))
            you.sp += 5
            print("\033[H\033[J")
            print(input('''You open up your locker only to find a void of empty space.
Oh that's right, you don’t use your locker anyway.

[ENTER]'''))
            print("\033[H\033[J")
            print(input('''...
It's 7:59! You have one minute to get to class.

[ENTER]'''))
            print("\033[H\033[J")
            print(input('''You hurry over to English.
Once you get there, you see Ms. Arnold passing out tests.

You sit down and open up a textbook for some last-minute studying, but when you open it, you find what looks like the answer key stuck in the pages!!

[ENTER]'''))

            choice_4()
        if choice is "b":
            print("\033[H\033[J")
            print(input('''You don’t remember, so you try every possible combination of numbers sequentially.

[ENTER]'''))
            print(input('''Life goes on.

[ENTER]'''))
            print(input('''You finally get the correct combination, but everyone has graduated high school already.

Minus 100 self-esteem points.

[ENTER]'''))
            you.sp -= 100
            end_game()
        if choice is "c":
            you.powerschool()
            choice_3()

def choice_4():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''Do you cheat and use the answer key?

 a  Yes
 b  No
 c  powerschool

Type a, b, or c: ''')
        if choice is "a":
            print("\033[H\033[J")
            print(input('''You hide the key underneath your desk and copy down the answers exactly...

    1. C, 2. C, 3. C, 4. C, 5. C...

[ENTER]'''))
            print(input('''But the questions were all "True or False."

Minus 50 grade points.

[ENTER]'''))
            you.gp -= 50
            print("\033[H\033[J")
            print(input('''BELL BELL BELL

You leave English. It's been a stressful morning.

[ENTER]'''))
            choice_5()
        if choice is "b":
            print("\033[H\033[J")
            print(input('''You remember the academic honesty policy that you signed at the beginning of the year and choose not to cheat.

But you didn't study anyway.

Minus 20 grade points.

[ENTER]'''))
            you.gp -= 20
            print(input('''BELL BELL BELL

You leave English. It's been a stressful morning.

[ENTER]'''))
            choice_5()

        if choice is "c":
            print('You decide to check powerschool to see how much you can afford to fail this next test.')
            you.powerschool()
            choice_4()

def choice_5():
    end_game()
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''**You’ve learned a new coping mechanism!**

[bang_head_against_wall]

Use now?

 a  Yes
 b  No

Type a or b: ''')
        if choice is "a":
            print("\033[H\033[J")
            you.bang_head_against_wall()
            choice_6()

        if choice is "b":
            print("\033[H\033[J")
            print(input('''You make it to your ¾ class– Tech.

Before you can sit down and open up your chromebook, you hear the fire alarm!
The clock is flashing FIRE FIRE FIRE. You walk over to the doorway.

[ENTER]'''))
            #choice_7()

def choice_6():
    end_game()
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''Repeat?

 a  Bang head against wall again
 b  Have a little self-respect
 c  Powerschool

Type a, b, or c: ''')
        if choice is "a":
            print("\033[H\033[J")
            you.bang_head_against_wall()
            choice_6()
        if choice is "b":
            print("\033[H\033[J")
            print(input('''You make it to your ¾ class– Tech.

Before you can sit down and open up your chromebook, you hear the fire alarm!
The clock is flashing FIRE FIRE FIRE. You walk over to the doorway.

[ENTER]'''))
            #choice_7()
        if choice is "c":
            you.powerschool()
            choice_6()








choice_1()
you.bang_head_against_wall()
