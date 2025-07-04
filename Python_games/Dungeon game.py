# Welcome to the Dungeon game! in this game you have to choose hard designs to survive.

#  # -> wall
#  @ -> you
#  0 -> hole
#  $ -> gold
#  ! -> enemy
#  % -> Door
# Oder words or numbers mey change, when the speaker talks.

print(">>> tape the number to do something")
print()
print("Wake up!")
print()
print("(1) try to wake up")
print()

action = int(input())

if action == 1:
    print("Wake up!")
    print()
    print("(1) try to wake up")
    print()

    action = int(input())
    if action == 1:              #IN GAME -----------------------------
       inventory = [""] #INVENTORI---------------------------------------------------------------<>
       print("You see a dark room, all covered in vines and plants, there are dirty puddles on the ground, and in the darkness you see a weapon? ...")
       print("")
       print(">>> What is the weapon?")
       print("")
       print("(1) axe")
       print("(2) sword")
       print("(3) hammer")
       print("(4) bow and arrow")
       print("(5) book")

       choice = int(input(""))   #choice -----------------------------
       list1 = [1,2,3,4,5]

       if choice == 1:
           print("")
           print("when you take the axe, you remember something about your past... You remember that you were a barbarian, that was here to test his skills, and take the money for your family...")
           print("and when you look around you sse a door covered in plants, like it is one of wall?")
           print("")
           print(">>> if there is no question, press any button to continue, and pres enter")

           action = (input())

              #DOOR PART------------------------------------------
           print(">>> What do you do?")
           print("(1) inspect room")
           print("(2) brake door ")
           print("(3) open door")

           action_for_room = int(input())

           list2 = [1,2,3]

           if action_for_room == 1:
               print(1)
           if action_for_room == 2:
               print(2)
           if action_for_room == 3:
               print(3)
           if action_for_room not in list2:
               print(f"there is no ting as {action_for_room}")



       if choice == 2:
           print("")
           print("when you take the sword, you remember something about your past self... You remember... you were a knight, that was here for his king, the king was almost dead...")
           print("and when you look around you sse a door covered in plants, like it is one of wall?")
           print("")
           print(">>> if there is no question, press any button to continue, and pres enter")

           action = (input())

       if choice == 3:
           print("")
           print("when you take the hammer, you remember something about you... you were a engineer, trying to take the money of the dungeon, to make his machine... ")
           print("and when you look around you sse a door covered in plants, like it is one of wall?")
           print("")
           print(">>> if there is no question, press any button to continue, and pres enter")

           action = (input())

       if choice == 4:
           print("")
           print("when you take the bow and arrow, You remember... you were a hunter or an a adventurer.. you like to tell your self that. You are here for the adventure")
           print("and when you look around you sse a door covered in plants, like it is one of wall?")
           print("")
           print(">>> if there is no question, press any button to continue, and pres enter")

           action = (input())

       if choice == 5:
           print("")
           print("when you take the book?, you immediately realize your purpose in this room, this is a dungeon that you studied a lot about, and you want to sse the dungeon, and investigate why its here, You are a wizard... ")
           print("and when you look around you sse a door covered in plants, like it is one of wall?")
           print("")
           print(">>> if there is no question, press any button to continue, and pres enter")

           action = (input())


       if choice not in list1:
           print(f"there is no ting as {choice}")





       #print("##  ##")
       #print("#    #")
       #print("#    #")
       #print("# @  #")
       #print("######")

    else:
        print(f"there is no ting as {action}")
else:
    print(f"there is no ting as {action}")

