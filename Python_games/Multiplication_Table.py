import  random
import time
from turtledemo.penrose import start

#start_time = time.time()

points = 0

while True:
    #SE_time = time.time() - start_time

    left_side = random.randint(1, 10)  # Направи го според теб!
    right_side = random.randint(1, 10)  # Направи го според теб!

    print(f'{left_side}.{right_side}=???')
    LR = left_side * right_side
    gess_num = int(input())

    #end_time = time.time()

   # print(SE_time)
  #  if SE_time >= 2:
   #     print(f'To show! {SE_time:.2f}')
    #    break

    if gess_num >= LR:
        print(True)
        points += 1
        print(f'points: {points}')
    else:
        print(f"NO! it was {LR}, try again!")
        points -= 1
        print(f'points: {points}')

    if points == -3:
        print(f'You lost! too meny mistakes!')
        break
#time.sleep(1)


