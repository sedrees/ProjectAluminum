#Player defaults
default player = "Olive"
default player_last = "Oyl"

#Skills

init python:
    class Skill:
        def __init__(self, title, skills):
            self.cat = title
            self.skills = skills

    def skill_change(self, skill, change):
        skill += change
        if change > 0:
            direction = "increased"
        else:
            direction = "decreased"
        renpy.notify("Your " + str(skill) + " " + direction + " by " + str(abs(change)))

# The game starts here.

label start:
    
    #Init creative skills
    default drawing = renpy.random.randint(0, 10)
    default storytelling = renpy.random.randint(0, 10)
    default typography = renpy.random.randint(0, 10)
    default design = renpy.random.randint(0, 10)

    #Init dev skills
    default frontend = renpy.random.randint(0, 10)
    default backend = renpy.random.randint(0, 10)
    default api = renpy.random.randint(0, 10)

    #Init admin skills
    default administration = renpy.random.randint(0, 10)
    default automation = renpy.random.randint(0, 10)
    default databases = renpy.random.randint(0, 10)
    default presentation = renpy.random.randint(0, 10)

    #Init soft skills
    default charisma = renpy.random.randint(0, 100)
    default morality = renpy.random.randint(0, 100)
    default organization = renpy.random.randint(0, 100)
    default confidence = renpy.random.randint(0, 100)
    default communication = renpy.random.randint(0, 100)

    $ creative = Skill("Creative", [drawing, storytelling, typography, design])
    $ dev = Skill("Development", [frontend, backend, api])
    $ admin = Skill("Administration", [administration, automation, databases, presentation])
    $ soft = Skill("Soft Skills", [charisma, morality, organization, confidence, communication])

    scene intro 1

    "You wake up, blinking slowly. You wonder if the events of yesterday were maybe just a dream... "

    $ creative.skill_change(drawing, -11)

    "Suddenly."

    return

    

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

    scene messy office
