#MAKE A QUIS SYSTEM THAT IS RANDOM AND HAS CATEGORIES like GEOGRAPHY , HISTORY AND OTHERS. . .
import random


A = random.randint(1,20)
B = random.randint(1,20)
D = A + B
num = [0]
Points = 0

#1--------------------------------

print(f'{A} + {B}')
D2 = int(input())
if D2 == D:
    print(f'Its True!')
    Points = Points + 1
    print(f'Your points: {Points}')
else:
    print(f'Its False it was {D}')
    Points = Points - 1
    print(f'Your points: {Points}')

#2---------------------------

A2 = random.randint(1,30)
B2 = random.randint(1,30)
Z = A2 + B2

print(f'{A2} + {B2}')
D3 = int(input())
if D3 == Z:
     print(f'Its True!')
     Points = Points + 1
     print(f'Your points: {Points}')
else:
    print(f'Its False it was {Z}')
    Points = Points - 1
    print(f'Your points: {Points}')

#3------------------------------------

A3 = random.randint(1,40)
B3 = random.randint(1,40)
Z2 = A3 + B3

print(f'{A3} + {B3}')
D3 = int(input())
if D3 == Z2:
     print(f'Its True!')
     Points = Points + 1
     print(f'Your points: {Points}')
else:
    print(f'Its False it was {Z2}')
    Points = Points - 1
    print(f'Your points: {Points}')

#4--------------------------------

A4 = random.randint(1,50)
B4 = random.randint(1,50)
Z3 = A4 + B4

print(f'{A4} + {B4}')
D3 = int(input())
if D3 == Z3:
     print(f'Its True!')
     Points = Points + 1
     print(f'Your points: {Points}')
else:
    print(f'Its False it was {Z3}')
    Points = Points - 1
    print(f'Your points: {Points}')

#5---------------------------------------

A5 = random.randint(10,70)
B5 = random.randint(10,70)
Z4 = A5 + B5

print(f'{A5} + {B5}')
D3 = int(input())
if D3 == Z4:
     print(f'Its True!')
     Points = Points + 1
     print(f'Your points: {Points}')
else:
    print(f'Its False it was {Z4}')
    Points = Points - 1
    print(f'Your points: {Points}')

#6--------------------------------------

A6 = random.randint(10,85)
B6 = random.randint(10,85)
Z5 = A6 + B6

print(f'{A6} + {B6}')
D3 = int(input())
if D3 == Z5:
     print(f'Its True!')
     Points = Points + 1
     print(f'Your points: {Points}')
else:
    print(f'Its False it was {Z5}')
    Points = Points - 1
    print(f'Your points: {Points}')


#7----------------------------------------

while True:
 A7 = random.randint(10,100)
 B7 = random.randint(10,100)
 Z6 = A7 + B7
 print(f'{A7} + {B7}')
 D3 = int(input())
 if D3 == Z6:
     print(f'Its True!')
     Points = Points + 1
     print(f'Your points: {Points}')
 if Points == 10:
        break
 else:
    print(f'Its False it was {Z6}')
    Points = Points - 1
    print(f'Your points: {Points}')
 if Points < 0:
         break
#BOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS--------------
 if Points == 10:
    print('BOSS LEVEL !!!')

 AA = random.randint(1, 10)
 BB = random.randint(1, 10)
 ZZ = AA * BB

 print(f'{AA} . {BB}')
 D3 = int(input())
 if D3 == ZZ:
         print(f'Its True!')
         Points = Points + 1
         print(f'Your points: {Points}')
         print(f'Your Now Level 2, Congratulations!')   #!!!!
 if Points > 10:
    break
 else:
         print(f'Its False it was {ZZ}')
         Points = Points - 1
         print(f'Your points: {Points}')
 if Points < 0:
    break
 print('You Lost The game...')


# NOW LEVEL !!! ------------------------------------

while True:
  AA2 = random.randint(1, 15)
  BB2 = random.randint(1, 15)
  ZZ2 = AA2 * BB2

  print(f'{AA2} . {BB2}')
  D3 = int(input())
  if D3 == ZZ2:
     print(f'Its True!')
     Points = Points + 1
     print(f'Your points: {Points}')
     if Points > 15:
        break
  else:
     print(f'Its False it was {ZZ2}')
     Points = Points - 1
     print(f'Your points: {Points}')

  if Points < 0:
     print("You lost the game...")
     break


#1--------------------------------------
import random
while True:
 AA3 = random.randint(1, 20)
 BB3 = random.randint(1, 20)
 ZZ3 = AA3 * BB3

 print(f'{AA3} . {BB3}')
 D3 = int(input())
 if D3 == ZZ3:
    print(f'Its True!')
    Points = Points + 1
    print(f'Your points: {Points}')
 else:
     print(f'Its False it was {ZZ3}')
     Points = Points - 1
     print(f'Your points: {Points}')

 if Points < 0:
     print("You lost the game...")
     break
 break
#2------------------------------------------
 import random
 while True:
   AA4 = random.randint(1, 25)
   BB4 = random.randint(1, 25)
   ZZ4 = AA4 * BB4

   print(f'{AA4} . {BB4}')
   D3 = int(input())
   if D3 == ZZ4:
    print(f'Its True!')
    Points = Points + 1
    print(f'Your points: {Points}')
   else:
    print(f'Its False it was {ZZ4}')
    Points = Points - 1
    print(f'Your points: {Points}')

 if Points == 30:
    print(f"You Win The Game! You Have {Points} Points good job!")
    print("Want to try again?")
 while True:
   AA5 = random.randint(1, 25)
   BB5 = random.randint(1, 25)
   ZZ5 = AA5 * BB5

   print(f'{AA5} . {BB5}')
   D3 = int(input())
   if D3 == ZZ5:
    print(f'Its True!')
    Points = Points + 1
    print(f'Your points: {Points}')
   else:
    print(f'Its False it was {ZZ5}')
    Points = Points - 1
    print(f'Your points: {Points}')