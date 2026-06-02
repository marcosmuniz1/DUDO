import numpy as np
import random

players = [1,2]
remaining_dices={1:5,2:5}
rnum=0

def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]

while remaining_dices[1]>0 and remaining_dices[2]>0:
    rnum+=1
    print(f"Round {rnum}")
    d1=roll_dice(remaining_dices[1])
    d2=roll_dice(remaining_dices[2])
    print(f"dices for player 1: {d1}")
    fv1=int(input("Place guess for face value (1-6): "))
    m1=int(input("Place gues for number of matching dices: "))
    fv2=fv1
    m2=m1+1
    print(f"CPU guess is {m2} dices with a {fv2}")
    challenge=input("Do you challenge? y/n: ")
    if challenge=="y":
        matches=d1.count(fv2)+d1.count(fv1)
        print(f"{matches} dices match the face value")
    remaining_dices[1]=remaining_dices[1]-1