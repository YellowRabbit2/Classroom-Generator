#Classroom Skill Generator, created as a fun little project.
import random

#Declaring variables (a surprise tool for later)
DoroSk1 = 0
DoroSk2 = 0
RichSk1 = 0
RichSk2 = 0
DoroTaught1 = 0
DoroTaught2 = 0
RichTaught1 = 0
RichTaught2 = 0
confirmLoop = 'Y'

def main():

    #Declaring the count variable so that we may use it again later 
    global count
    global confirmLoop
    print('Welcome to the Classroom Skill Generator!')
    print('This program is designed to automatically generate the skills-')
    print('-taught by both Professor Dorothea and Richten an entire month, or 4 weeks.')

    #The loop for all 4 weeks of classes, which asks the user if they want to use the program again without having to rerun.
    while confirmLoop == 'Y' or confirmLoop == 'y':
        for count in range(4):
            classInput()
            classOutput()

        confirmLoop = input(str('Would you like to do another loop? Type Y for yes, anything else for no.'))
        
#This function randomizes the skills the professors teach each week, and
#remembers the skills taught by the professors the week before. 
def classInput():

    #Using some of the variables we declared earlier.
    global DoroSk1
    global DoroSk2 
    global RichSk1
    global RichSk2
    global DoroTaught1
    global DoroTaught2
    global RichTaught1
    global RichTaught2

    #Assigning a random Skill that hasn't been used in the last week, or this week. 
    DoroSk1 = random.randint(1, 10)
    while DoroSk1 == DoroTaught1 or DoroSk1 == DoroTaught2 or DoroSk1 == RichTaught1 or DoroSk1 == RichTaught2 or DoroSk1 == RichSk1 or DoroSk1 == RichSk2:
        DoroSk1 = random.randint(1, 10)

    DoroSk2 = random.randint(1, 10)       
    while DoroSk2 == DoroTaught1 or DoroSk2 == DoroTaught2 or DoroSk2 == DoroSk1 or DoroSk2 == RichTaught1 or DoroSk2 == RichTaught2 or DoroSk2 == RichSk1 or DoroSk2 == RichSk2:
        DoroSk2 = random.randint(1, 10)

    RichSk1 = random.randint(1, 10)
    while RichSk1 == RichTaught1 or RichSk1 == RichTaught2 or RichSk1 == DoroSk1 or RichSk1 == DoroSk2 or RichSk1 == DoroTaught1 or RichSk1 == DoroTaught2:
        RichSk1 = random.randint(1, 10)

    RichSk2 = random.randint(1, 10)
    while RichSk2 == RichTaught1 or RichSk2 == RichTaught2 or RichSk2 == DoroSk1 or RichSk2 == DoroSk2 or RichSk2 == RichSk1 or RichSk2 == DoroTaught1 or RichSk2 == DoroTaught2:
        RichSk2 = random.randint(1, 10)

    #The way the program remembers what Skill was taught the week before. 
    DoroTaught1 = DoroSk1

    DoroTaught2 = DoroSk2

    RichTaught1 = RichSk1

    RichTaught2 = RichSk2
        
 
#This function assigns the Skill "ID"'s to a string that will print what
#Skill ID corresponds to which skill, and what skills are being taught for
#the current week.
def classOutput():

    #Using the variables that we declared before and some new ones
    #(P.S. (for tech peeps) As tech experienced people may have spotted,
    #there are probably some variables that don't need do be declared globally
    #at all or multiple times, but that's just me being extra cautious/lazy.
    #With that said, feel free to edit this yourself and send it to the gang
    #more polished than I. Right now though, it works so ¯\_(ツ)_/¯)
    global DoroSk1
    global DoroSk2 
    global RichSk1
    global RichSk2
    global DoroTaught1
    global DoroTaught2
    global RichTaught1
    global RichTaught2
    global skillTaught1
    global skillTaught2
    global rskillTaught1
    global rskillTaught2
    global count

    #Creates and Declares a variable that will be used to display the current week.
    currentWeek = count + 1

    #A long, long string of arguments that assigns each Skill ID their own
    #corresponding Skill string.
    if DoroSk1 == 1:
        skillTaught1 = 'Swords'
    elif DoroSk1 == 2:
        skillTaught1 = 'Lance'
    elif DoroSk1 == 3:
        skillTaught1 = 'Axes'
    elif DoroSk1 == 4:
        skillTaught1 = 'Bow'
    elif DoroSk1 == 5:
        skillTaught1 = 'Guile'
    elif DoroSk1 == 6:
        skillTaught1 = 'Reason'
    elif DoroSk1 == 7:
        skillTaught1 = 'Faith'
    elif DoroSk1 == 8:
        skillTaught1 = 'Heavy Armor'
    elif DoroSk1 == 9:
        skillTaught1 = 'Riding'
    elif DoroSk1 == 10:
        skillTaught1 = 'Flying'

    if DoroSk2 == 1:
        skillTaught2 = 'Swords'
    elif DoroSk2 == 2:
        skillTaught2 = 'Lance'
    elif DoroSk2 == 3:
        skillTaught2 = 'Axes'
    elif DoroSk2 == 4:
        skillTaught2 = 'Bow'
    elif DoroSk2 == 5:
        skillTaught2 = 'Guile'
    elif DoroSk2 == 6:
        skillTaught2 = 'Reason'
    elif DoroSk2 == 7:
        skillTaught2 = 'Faith'
    elif DoroSk2 == 8:
        skillTaught2 = 'Heavy Armor'
    elif DoroSk2 == 9:
        skillTaught2 = 'Riding'
    elif DoroSk2 == 10:
        skillTaught2 = 'Flying'

    if RichSk1 == 1:
        rskillTaught1 = 'Swords'
    elif RichSk1 == 2:
        rskillTaught1 = 'Lance'
    elif RichSk1 == 3:
        rskillTaught1 = 'Axes'
    elif RichSk1 == 4:
        rskillTaught1 = 'Bow'
    elif RichSk1 == 5:
        rskillTaught1 = 'Guile'
    elif RichSk1 == 6:
        rskillTaught1 = 'Reason'
    elif RichSk1 == 7:
        rskillTaught1 = 'Faith'
    elif RichSk1 == 8:
        rskillTaught1 = 'Heavy Armor'
    elif RichSk1 == 9:
        rskillTaught1 = 'Riding'
    elif RichSk1 == 10:
        rskillTaught1 = 'Flying'

    if RichSk2 == 1:
        rskillTaught2 = 'Swords'
    elif RichSk2 == 2:
        rskillTaught2 = 'Lance'
    elif RichSk2 == 3:
        rskillTaught2 = 'Axes'
    elif RichSk2 == 4:
        rskillTaught2 = 'Bow'
    elif RichSk2 == 5:
        rskillTaught2 = 'Guile'
    elif RichSk2 == 6:
        rskillTaught2 = 'Reason'
    elif RichSk2 == 7:
        rskillTaught2 = 'Faith'
    elif RichSk2 == 8:
        rskillTaught2 = 'Heavy Armor'
    elif RichSk2 == 9:
        rskillTaught2 = 'Riding'
    elif RichSk2 == 10:
        rskillTaught2 = 'Flying'
        
    #Finally, a way to display the Skill strings noting exactly what week
    #the skills are taught, along with the respective Skill ID's for possible
    #debugging.
    print('The skills Professor Dorothea is teaching for week', currentWeek, 'are as follows:', skillTaught1, 'and', skillTaught2)
    print('The skills Professor Richten is teaching for week', currentWeek, 'are as follows:', rskillTaught1, 'and', rskillTaught2)
    print(DoroSk1, DoroSk2, RichSk1, RichSk2)        


main()
