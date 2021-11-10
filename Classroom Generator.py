#Classroom Skill Generator, created as a fun little project.
import random

DoroSk1 = 0
DoroSk2 = 0
RichSk1 = 0
RichSk2 = 0
DoroTaught1 = 0
DoroTaught2 = 0
RichTaught1 = 0
RichTaught2 = 0
def main():

    global count
    global DoroSk1
    global DoroSk2 
    global RichSk1
    global RichSk2
    global DoroTaught1
    global DoroTaught2
    global RichTaught1
    global RichTaught2
    
    print('Welcome to the Classroom Skill Generator!')
    print('This program is designed to automatically generate the skills-')
    print('-taught by both Professor Dorothea and Richten every week for an entire month, or 4 weeks.')
    for count in range(4):
        classInput()
        classOutput()
        
#This function randomizes and asks the user for the past in
def classInput():

    global DoroSk1
    global DoroSk2 
    global RichSk1
    global RichSk2
    global DoroTaught1
    global DoroTaught2
    global RichTaught1
    global RichTaught2
            
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

    DoroTaught1 = DoroSk1

    DoroTaught2 = DoroSk2

    RichTaught1 = RichSk1

    RichTaught2 = RichSk2
        
 
        
def classOutput():

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

    currentWeek = count + 1

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

    print('The skills Professor Dorothea is teaching for week', currentWeek, 'are as follows:', skillTaught1, 'and', skillTaught2)
    print('The skills Professor Richten is teaching for week', currentWeek, 'are as follows:', rskillTaught1, 'and', rskillTaught2)
    print(DoroSk1, DoroSk2, RichSk1, RichSk2)        


main()


