#Player
image fchar = "olive_oyl.png"
image mchar = "oscar wilde.png"

#Important stuff
define dbg = Character("Debug")

#Game loop
default start_month = False
default months = 0

#Trigger story text in first month
default first_time = 0

#Skills
init python:
    class Skill:
        def __init__(self, title, category, level):
            self.title = title
            self.category = category
            self.level = level

        def skill_change(self, change):
            self.level += change
            if change > 0:
                direction = "increased"
            else:
                direction = "decreased"
            renpy.notify("Your " + str(self.title) + " " + direction + " by " + str(abs(change)) + ". It is now " + str(self.level) + ".")
            renpy.pause(5)

        
# The game starts here.

label start:

    #Init creative skills
    $ drawing = Skill("Drawing", "Creative", renpy.random.randint(0,10))
    $ storytelling = Skill("Storytelling", "Creative", renpy.random.randint(0,10))
    $ typography = Skill("Typography", "Creative", renpy.random.randint(0,10))
    $ design = Skill("Design", "Creative", renpy.random.randint(0,10))

    #Init dev skills
    $ frontend = Skill("Frontend", "Development", renpy.random.randint(0,10))
    $ backend = Skill("Backend", "Development", renpy.random.randint(0,10))
    $ api = Skill("API", "Development", renpy.random.randint(0,10))

    #Init admin skills
    $ administration = Skill("Administration", "Administration", renpy.random.randint(0,10))
    $ automation = Skill("Automation", "Administration", renpy.random.randint(0,10))
    $ databases = Skill("Databases", "Administration", renpy.random.randint(0,10))
    $ presentation = Skill("Presentation", "Administration", renpy.random.randint(0,10))

    #Init soft skills
    $ charisma = Skill("Charisma", "Soft Skills", renpy.random.randint(0,100))
    $ morality = Skill("Morality", "Soft Skills", renpy.random.randint(0,100))
    $ organization = Skill("Organization", "Soft Skills", renpy.random.randint(0,100))
    $ communication = Skill("Communication", "Soft Skills", renpy.random.randint(0,100))
    $ confidence = Skill("Confidence", "Soft Skills", renpy.random.randint(0,100))

    scene intro 1

    "You wake up, blinking slowly. You wonder if the events of yesterday were maybe just a dream... "

    $ charisma.skill_change(500)

    "Suddenly."

    "It hits you again. It was very real, and you are now very unemployed."
    scene intro 2

    "Redundant. A statistic. You wonder how awkward the conversations will be with friends and family."

    "You begin to question yourself. Is this who I am now? What will I do?"

    scene intro 3

    "Who am I?"

    $ player = renpy.input("First name")
    $ player_last = renpy.input("Surname")

    jump main

label main:

    #DEBUG
    $ player = "Olive"
    $ first_time = 1

    #not debug
    $ p = Character(player)

    scene office
    show fchar at right
    call screen main_game

    if first_time == 0:
        p "Today is the first day of the rest of my life. I guess it's time to start my journey of self-improvement... or something..."

        p "If I don't, I'll have nothing to post on LinkedIn..."

        $ first_time = 1

    # while not start_month:
    $ renpy.pause(15)

return

