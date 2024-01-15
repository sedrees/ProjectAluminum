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

    def skills_by_category(skill_list, category):
        return [skill for skill in skill_list if skill.category == category]

    class Skill:
        def __init__(self, title, category, level):
            self.title = title
            self.category = category
            self.level = level

        def __eq__(self, other):
            return (
                isinstance(other, Skill) and self.title == other.title and self.category == other.category and self.level == other.level
            )

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

    $ player_skills = [
        #Init creative skills
        Skill("Drawing", "Creative", renpy.random.randint(0,10)),
        Skill("Storytelling", "Creative", renpy.random.randint(0,10)),
        Skill("Typography", "Creative", renpy.random.randint(0,10)),
        Skill("Design", "Creative", renpy.random.randint(0,10)),

        #Init dev skills
        Skill("Frontend", "Development", renpy.random.randint(0,10)),
        Skill("Backend", "Development", renpy.random.randint(0,10)),
        Skill("API", "Development", renpy.random.randint(0,10)),

        #Init admin skills
        Skill("Administration", "Administration", renpy.random.randint(0,10)),
        Skill("Automation", "Administration", renpy.random.randint(0,10)),
        Skill("Databases", "Administration", renpy.random.randint(0,10)),
        Skill("Presentation", "Administration", renpy.random.randint(0,10)),

        #Init soft skills
        Skill("Charisma", "Soft Skills", renpy.random.randint(0,50)),
        Skill("Morality", "Soft Skills", renpy.random.randint(0,50)),
        Skill("Organization", "Soft Skills", renpy.random.randint(0,50)),
        Skill("Communication", "Soft Skills", renpy.random.randint(0,50)),
        Skill("Confidence", "Soft Skills", renpy.random.randint(0,50))
    ]

    #Make available globally?
    $ persistent.player_skills = player_skills

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
    $ player_last = "Oyl"
    $ cur_title = "Junior Administrator"
    $ first_time = 1

    #not debug
    $ p = Character(player)

    scene office
    show fchar at right
    call screen main_game(player, player_last, cur_title)

    if first_time == 0:
        p "Today is the first day of the rest of my life. I guess it's time to start my journey of self-improvement... or something..."

        p "If I don't, I'll have nothing to post on LinkedIn..."

        $ first_time = 1

    # while not start_month:
    $ renpy.pause(15)

return

