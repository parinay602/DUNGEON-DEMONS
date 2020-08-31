import cmd
import os
import textwrap
import time
import random
import sys
inventory=[]


currentplace = "s1"

screen_width=100
health=100
class player:
    def __init__ (self):
        self.name=" "
        self.hp=0
        self.mp=0
        self.status_effect=[]
        self.location='start'
myPlayer= player()

def input_screen_selections():
    option= input(">")
    if option.lower()==("play"):
        start_game() 
    elif option.lower()==("help"):
        help_menu()
    elif option.lower()==("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter a valid command")
        option=input('>')
        if option.lower()==("play"):
            start_game() 
        elif option.lower()==("help"):
            help_menu()
        elif option.lower()==("quit"):
            sys.exit()

def title_screen():
    os.system('cls')  
    print("##############################")
    print("# Welcome to DUNGEONS&DEMONS #") 
    print("##############################")
    print("#           -Play-           #")
    print("#           -Help-           #")
    print("#           -Quit-           #")
    print("##############################")
    (input_screen_selections())

def help_menu():
    print()
    print("#############################")
    print("#Welcome to  DUNGEONS&DEMONS#") 
    print("#############################")
    print("-Use Up,Down,Left,Right to move")
    print("-Type your commands to implement them.")
    print("Command Syntax:")
    print("go [direction]")
    print("get [item]")  
    print("examine(Please examine each and every place for some more insight)")
    print("-Good luck and have fun guys.")
    print()
    (input_screen_selections())


def showStatus():
  print('---------------------------')
  print('You are in the '+ zonemap[currentplace]["ZONENAME"])
  print('Health points-',health)
  print("Inventory : " + str(inventory))
  directions_available=["right","left","up","down"]
  directions=[]
  for dirs in directions_available:
    if dirs in zonemap[currentplace]:
        directions.append(dirs)
  print("Directions Available= ", directions)
        

#   if "iteam1" in zonemap[currentplace]:
#     print('You see a ' + zonemap[currentplace]['iteam1'])
#   if "iteam2" in zonemap[currentplace]: 
#       print('You see a ' + zonemap[currentplace]['iteam2'])
  print("---------------------------")

def fightatc1():
    global health
    f1= """You look around and  see everything covered with cobwebs...\nNow you hear some eerily sound near the door and decide to inspect\nWhile you head towards the door you feel a sudden sting on your left shoulder and are \npulled back to come face to face with this giant spider guarding the castle\nThis is the moment where you have to prove yourself by taking the best possible decisions\nand finding your way by defeating this spider\nThe spider is venemous so remember to keep your distance from it \nBut it also has some weaknesses try to exploit them.
    """
    typewriter_writer(f1)
    time.sleep(3)
    print(" ")
    weapon_choose=''
    spider_health=200
    print("Inventory=",inventory)
    weapon_availble=["sword","bow","axe"]
    while weapon_choose=='' or weapon_choose=="herbs":
        weapon_choose=input("Choose the weapon you would like to fight with from the inventory: ")
    if weapon_choose in weapon_availble:
        if weapon_choose== "sword":
            print("""You have two attack types-
                1)stab(Hard hit)
                2)slash(Quick hit) """)
            print("")
            time.sleep(1)
            print("Spider Health -",spider_health)
            print("")
            while spider_health>0:
                attack=input("Choose your attack: ")
                print('')
                if attack =="stab":
                    spider_health-=50
                    print("# You stabbed the spider for 50 damage with",weapon_choose)
                    print("# Spider Health-",spider_health)
                    print('')
                    time.sleep(3)
                    health-=15
                    print("# The spider stung you for 15 hp")
                    print('# Health-',health)
                    print("")
                    time.sleep(3)

                if attack =="slash":
                    spider_health-=40
                    print("# You slashed the spider for 40 damage with",weapon_choose)
                    print("# Spider Health-",spider_health)
                    print('')
                    time.sleep(3)
                    health-=10
                    print("# The spider damaged you for 10 hp")
                    print('# Health-',health)
                    print('')
                    time.sleep(3)
                if spider_health<60:
                    print("# You were poisoned by the spider")
                    print('')
                    time.sleep(3)
            else:

                at1="""Congratulations! You killed the spider\nBut you are heavily injured"""
                typewriter_writer(at1)
                time.sleep(3)
                using_herbs()
        elif weapon_choose=="axe":
            print("""You have two attack types-
                1)stab(Hard hit)
                2)slash(Quick hit) """)
            print("")
            time.sleep(3)
            print("Spider Health -",spider_health)
            print("")
            while spider_health>0:
                attack=input("Choose your attack: ")
                print('')
                if attack =="stab":
                    spider_health-=50
                    print("# You stabbed the spider for 50 damage with",weapon_choose)
                    print("# Spider Health-",spider_health)
                    print('')
                    time.sleep(3)
                    health-=15
                    print("# The spider stung you for 15 hp")
                    print('# Health-',health)
                    print("")
                    time.sleep(3)

                if attack =="slash":
                    spider_health-=40
                    print("# You slashed the spider for 40 damage with",weapon_choose)
                    print("# Spider Health-",spider_health)
                    print('')
                    time.sleep(3)
                    health-=10
                    print("# The spider damaged you for 10 hp")
                    print('# Health-',health)
                    print('')
                    time.sleep(3)
                if spider_health<60:
                    print("# You were poisoned by the spider")
                    print('')
                    time.sleep(3)
            else:

                at2="""Congratulations! You killed the spider\nBut you are heavily injured"""
                typewriter_writer(at2)
                time.sleep(3)
                using_herbs()
                      
        elif weapon_choose=="bow":
            print("""You have two attack types-
                1)power shot(Hard hit)
                2)precise shot(Quick hit)
                Enter the numbers. Ex: Choose your attack: 1 """)
            print("")
            time.sleep(3)
            print(" Spider Health -",spider_health)
            print("")
            while spider_health>0:
                attack=input("Choose your attack: ")
                print('')
                if attack =="1":
                    spider_health-=50
                    print("You sniped the spider for 50 damage with the bow")
                    print("Spider Health-",spider_health)
                    print('')
                    time.sleep(3)
                    health-=15
                    print("The spider shot you with his webs for 15 hp")
                    print('Health-',health)
                    print('')
                    time.sleep(3)

                if attack =="2":
                    spider_health-=40
                    print("You shot the spider for 40 damage with the bow")
                    print("Spider Health-",spider_health)
                    print('')
                    time.sleep(3)
                    health-=10
                    print("The spider shot you with his webs  for 10 hp")
                    print('Health-',health)
                    print('')
                    time.sleep(3)
                if spider_health<60:
                    print('')
                    print("The spider spat his venom at you and poisoned you")
                    print('')
                    time.sleep(3)
            else:
                at1="""Congratulation! You killed the spider\nBut you are heavily injured"""
                print('')
                typewriter_writer(at1)
                time.sleep(3)
                print(" ")
                using_herbs()
    else:
        if "sword" not in inventory:
            if "axe" not in inventory:
                if "bow" not in inventory:
                    no_wep="You dont have any weapon, you didnt pick it up at the starting\nSo you lost the game......Better Luck Next Time....GAME OVER !"
                    typewriter_writer1(no_wep)
                    time.sleep(10)

                    sys.exit()
def position_meter():
    global inventory
    global currentplace 
    x=1
    while True:
        while x==1:
            showStatus()
            x+=1
        move = ''
        while move == '':  
            move = input('>')
        
        move = move.lower().split()
        if move[0] == 'go':
            if move[1] in zonemap[currentplace]:
                currentplace= zonemap[currentplace][move[1]]
                showStatus()
                break
            else:
                print("You can't go that way!")
                showStatus()
        if move[0]=="get" and currentplace=="d1": 
            if "iteam1" in zonemap[currentplace] and move[1] in zonemap[currentplace]['iteam1']:
                inventory+= [move[1]]
                print(move[1]+ " " + 'added to the inventory.')
                showStatus()
                del zonemap[currentplace]["iteam1"] 
                if "iteam2" in zonemap[currentplace]:
                    del zonemap[currentplace]["iteam2"]
                break
            elif "iteam2" in zonemap[currentplace] and move[1] in zonemap[currentplace]['iteam2']:
                inventory += [move[1]]
                print(move[1]+ " " + 'added to the inventory.')
                showStatus()
                del zonemap[currentplace]["iteam2"] 
                if "iteam1" in zonemap[currentplace]:
                    del zonemap[currentplace]["iteam1"]
                break   
            else:
                print("Can't get" + " " + move[1]+ ' !')
                showStatus()
                break

        if move[0]=="get" and currentplace!="d1": 
            if "iteam1" in zonemap[currentplace] and move[1] in zonemap[currentplace]['iteam1']:
                inventory+= [move[1]]
                print(move[1]+ " " + 'added to the inventory.')
                showStatus()
                del zonemap[currentplace]["iteam1"] 
                if "iteam2" in zonemap[currentplace]:
                    del zonemap[currentplace]["iteam2"]
            elif "iteam2" in zonemap[currentplace] and move[1] in zonemap[currentplace]['iteam2']:
                inventory += [move[1]]
                print(move[1]+ " " + 'added to the inventory.')
                showStatus()
                del zonemap[currentplace]["iteam2"] 
                if "iteam1" in zonemap[currentplace]:
                    del zonemap[currentplace]["iteam1"]   
            else:
                print("Can't get" + " " + move[1]+ ' !')
                showStatus()
        
        
        if move[0]=="examine" and currentplace=="d2":
            examine_0=(zonemap[currentplace]["examine"])
            iteams_list=[]
            if "iteam1" in zonemap[currentplace]:
                iteams_list.append(zonemap[currentplace]['iteam1'])
            if "iteam2" in zonemap[currentplace]: 
                iteams_list.append(zonemap[currentplace]['iteam2'])
            break
        if move[0]=="examine":
            examine_0=(zonemap[currentplace]["examine"])
            iteams_list=[]
            if "iteam1" in zonemap[currentplace]:
                iteams_list.append(zonemap[currentplace]['iteam1'])
            if "iteam2" in zonemap[currentplace]: 
                iteams_list.append(zonemap[currentplace]['iteam2'])
            
            typewriter_writer1(examine_0)
            print()
            print("Items available are= ",iteams_list)
        if move[0]=="attack" and currentplace=="d2":
            attackind2()
        if move[0]=="exit":
           sys.exit()
def attackind2():
    print()
    end_endend="Demon had no idea that you are free and you took him by surprise\nYou saved the princess and saved the town from him\nYou are a True Hero.Your decisions took you to the right path and helped in defeating the demon\nWell Played.......YOU WON !!!!"
    typewriter_writer1(end_endend)
    time.sleep(20)
    
    sys.exit()
def typewriter_writer(message):
    os.system("cls")
    for char in message:
        if char!= "\n":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        elif char=="\n":
            time.sleep(1)
            print("")
def typewriter_writer1(message):
    
    for char in message:
        if char!= "\n":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        else:
            time.sleep(1)
            print("")

def using_herbs():
    global health
    global inventory
    if "herbs" in inventory:
        time.sleep(3)
        print()
        dd="""Use the herbs to make a healing potion to heal"""
        typewriter_writer1(dd)
        time.sleep(5)
        print()
        inventory.remove("herbs")
        inventory.append("healing potion")
        d_d= """You used your herbs to make a healing potion to get your health back."""
        typewriter_writer1(d_d)
        time.sleep(5)
        print()
        print("Inventory =",inventory)
        time.sleep(3)

        print("You healed yourself")
        print()
        time.sleep(2)
        inventory.remove("healing potion")
        health=100
        print('Health-',health)
        time.sleep(1)
        print()
        print("Inventory =",inventory)
        
    else:
        dd_die="""Your health is depleting due to the poison"""
        
        typewriter_writer1(dd_die)
        print()
        
        while health>0:
            health-=5
            print("Current Health-",health)
            time.sleep(0.6)    

        ending_text1=("You died Only if you had something to heal yourself with, you might have survived......")
        typewriter_writer1(ending_text1)
        (time.sleep(3))
        ending_text2=("Better Luck Next Time :)")
        time.sleep(5)
        typewriter_writer1(ending_text2)
        sys.exit()
def rope_breaker(): 
    global inventory
    global currentplace
    inventory1=inventory
    inventory=[]
    print()
    time.sleep(2)
    sa=("Now you have to cut your rope with the help of your weapon\nExamine the hall to find something useful....")   
    typewriter_writer1(sa)
    print()
    time.sleep(5)
    position_meter()
    cut_the_roops=""
    while cut_the_roops!="y" or cut_the_roops!="n":
        cut_the_roops=input("Would you like to cut the ropes? y/n  :")
        if cut_the_roops=="y":
            currentplace="d2" 
            sa1=("You have successfully freed yourself... \nNow you have to somehow kill the demon\n")
            typewriter_writer1(sa1)
            time.sleep(5)
            print()
            sa2="Examine your surrounding to get more help..."
            typewriter_writer1(sa2)
            print()
            time.sleep(5)
            position_meter()
            sa3="You should tie his legs(with vines you found in the jungle) as he is very tall and \nthen after he falls on the ground, stab him in the head."
            typewriter_writer1(sa3)
            print()
            time.sleep(6)
            if "vines" not in inventory1:
                print()
                sad_ending=("Sorry, you didn't pick up an essential item [vines] which are used to end the game......GAME LOST ! \nBetter Luck Next Time")
                typewriter_writer1(sad_ending)
                time.sleep(10)
                sys.exit()
            else:
                print()
                sa4="As you picked up the vines from the jungle, you can tie the demon and attack him. \nYou have also unlocked a special command attack[attack] which you will use to kill the demon \nNow use this attack command."
                typewriter_writer(sa4)
                time.sleep(5)
                print()
                position_meter()

        elif cut_the_roops=="n":
            print()
            saddest_ending="You were too lazy to cut the ropes and died in a heroic way.....GAME LOST !"
            typewriter_writer1(saddest_ending)
            time.sleep(10)
            sys.exit()
 
def start_game():
    d1= "Hello comrade, Welcome to DUNGEON&DEMONS \nA demon  destroyed your kingdom and captured your princess \nYour objective is to rescue the princess from the demon's castle"
    typewriter_writer(d1)
    time.sleep(10)
    print(" ")
    print(" ")
    print(" ")
    d2="Lets start the game....."
    typewriter_writer1(d2)
    print()
    time.sleep(2)
    if currentplace=="s1":
        d3=("You are in a forest with nothing but dark gloomy trees for miles and miles")
        typewriter_writer(d3)
        print(" ")
        time.sleep(2)
        position_meter()
        if currentplace=="s2":
            d4=("""You have come across a diversion, choose between the two ways:- \n1) (right)Continue to explore the jungle,you may find some useful plants and herbs \n2) (left) Leave the jungle and go to a village nearby """)
            typewriter_writer(d4)
            time.sleep(2)
            print()
            position_meter()
            if currentplace=="a1":
                d5="""You have come across the village of Balsa """
                typewriter_writer(d5)
                time.sleep(2)
                print()

                d6="""This village looks a bit strange, examine to check why..."""
                typewriter_writer1(d6)
                time.sleep(2)
                print()
                position_meter()
                if currentplace=="a2":
                    d7="""The village was raided by the demons, examine to see if you will find anything useful."""
                    typewriter_writer(d7)
                    print()
                    time.sleep(2)
                    position_meter()
                    if currentplace=="c1":
                        e3="""You have now reached the dungeon of the demons. \nThere is a castle in front of you, 20 feet tall and made out of black sandstone \nBut you have to fight the castle guard......"""
                        typewriter_writer(e3)
                        print()
                        time.sleep(5)
                        fightatc1()
                        position_meter()
                        #Game Ends In this case :(
                        
                        
            elif currentplace=="b1":
                e1="""Now, you are in the deep jungle. \nStay alert, there maybe wild animals on the hunt, look out for some useful plants"""
                typewriter_writer(e1)
                time.sleep(2)
                print()
                position_meter()
                if currentplace=="b2":
                    e2="""Looks like this jungle is full of monkeys swinging on the trees \nLook out you may find some useful stuff.... """
                    typewriter_writer(e2)
                    time.sleep(2)
                    print()
                    position_meter()
                    if currentplace=="c1":
                        e3="""You have now reached the dungeon of the demons.\nThere is a castle in front of you, 20 feet tall and made out of black sandstone \nBut you have to fight the castle guard......"""
                        typewriter_writer(e3)                                          
                        print()
                        time.sleep(5) 
                        fightatc1()
                        position_meter()
                        if currentplace=="d1":
                            e4= " You have now enterd the castle,\nYou are thirsty and hungry in front of you there is a huge table set with a feast enough to feed your whole village,\nYou rush  towards the table and you go and pick up a glass of wine\nor so you thought, but it is actually goblin blood. \nYour body starts shivering and you blackout\n you wake up in a cave,\n You look for your backpack and see that is still there.\nYou hear a noise and turn around and see the demon himself. He is humungous in size , a giant, red skinned beast with a crown made out of bones\nYou reach into your bag to take out your weapon You swing your weapon at the enormous beast but are unable to pierce its skin. \nYou prepare to attack again but suddenly a white light appears from behind the beast, you cover your eyes but are blinded by the bright light...."
                            typewriter_writer(e4)
                            time.sleep(20)
                            print()
                            print()
                            e5="""When you open your eyes and find yoursef bounded in ropes\nYou see the demon , he is talking to the princess,whom he has kept in a cage.\nIt is a good time to strike as you face the demon's back and he would have no clue about your actions"""
                            typewriter_writer(e5)
                            print()
                            time.sleep(5)
                            rope_breaker()
                                
zonemap={
        's1': {
            "ZONENAME" : "Jungle",
            "examine" : "You can see a sword and an axe, choose a weapon wisely as you can only carry one",                                                                                                                               
            "up" : 's2',
            "iteam1" : 'sword',
            "iteam2" : 'axe'
            },
        's2': {
            "ZONENAME" : "Diversion",
            "examine" : "There is a sign saying'The easier way may not be the right one' ",
         
            "right" : 'b1',
            "left" : 'a1',
            },
            
        'a1': {
            "ZONENAME" : "entry of village",
            "examine" : " Looks like the village has been abandoned village , you should explore this village",
            
            "up" : 'a2',
            
         },
        'b1': {
            "ZONENAME" : "deep jungle",
            "examine" : "The jungle is full of herbs that may interest you  ",          
            "up" : 'b2',
            'iteam1':'herbs',},
        'a2': {
            "ZONENAME" : "abandoned village",
            "examine" : "There is a bow on the ground",
            
            "right" : 'c1',
            "iteam1" : 'bow',


           
        },
        'b2': {
            "ZONENAME" : "Wild Area",
            "examine" : "the area is full of vines hanging from trees, these vines might help you",
            
            "left" : 'c1',
            "iteam1" : 'vines',
           
        },
        'c1': {
            "ZONENAME" : "Entrance of the castle ",
            "examine" : "You have come across a big hallway",
            "up" : 'd1',
        },
        'd1': {
            "ZONENAME" : "the castle,tied up.",
            "examine" : "There is a dagger lying nearby, try to get it to free yourself.",
            "iteam1": "dagger",
            "attack": "d2"},
        'd2' : { 
            "ZONENAME" : "the position to attack",
            "examine" : "Everyone has a weakness and so is the demon, attack him in the back of his head to kill him.",
        }

        }
# e4="""""You have now enterd the castle,
#                             \nYou are thirsty and hungry in front of you there is a huge table set with a feast enough to feed your whole village,
#                             \nYou rush  towards the table and you go and pick up a glass of wine
#                             \nor so you thought, but it is actually goblin blood. 
#                             \nYour body starts shivering and you black out,
#                             \n you wake up in a cave, you find your backpack on the other side of the cave. You crawl and see that everything in the backpack is still there.
#                             \nSuddenly a strong gust of wind passes you, you turn around and see the demon himself. He is humungous in size , a giant, red skinned beast with a crown made out of bones
#                             \nYou reach into your bag to take out your weapon You swing your weapon at the enormous beast but are unable to pierce its skin. 
#                             \nYou prepare to attack again but suddenly a white light appears from behind the beast, you cover your eyes but are blinded by the bright light...."""
#                             typewriter_writer(e1)
#                             time.sleep(2)
#                             print()
                            # e5="""when you open your eyes and find yoursef bounded in ropes
                            # \nYou see the demon , he is talking to the princess,whom he has kept in a cage.
                            # \nIt is a good time to strike as face the demon's back and he would have no clue about your movements"""
#                             typewriter_writer(e1)
#                             time.sleep(2)
#                             print()
#                             position_meter()
title_screen()



