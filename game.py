import random
from agent import agent_challenges, agent_bid

remaining_dices = {1: 5, 2: 5}
rnum = 0

def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]

while remaining_dices[1] > 0 and remaining_dices[2] > 0:
    rnum += 1
    print(f"\nRound {rnum}")
    print(f"You have {remaining_dices[1]} remaining dices")
    print(f"CPU has {remaining_dices[2]} remaining dices")
    total_dice=remaining_dices[1]+remaining_dices[2]
    d1 = roll_dice(remaining_dices[1])
    d2 = roll_dice(remaining_dices[2])
    print(f"Your dice: {d1}")

    current_fv = 0
    current_m = 0
    current_bidder = 1

    while True:
        if current_bidder == 1:
            while True:
                fv = int(input("Your guess for face value (1-6): "))
                while fv not in [1, 2, 3, 4, 5, 6]:
                    print("Face value must be a number between 1 and 6")
                    fv = int(input("Your guess for face value (1-6): "))
                m = int(input("Your guess for number of matches: "))
                if fv > current_fv or m > current_m:
                    break
                print("You must raise either the face value or the matches.")
            current_fv, current_m = fv, m
            print(f"Your bid: {current_m} dices showing {current_fv}")
            current_bidder = 2

        if current_bidder == 2:
            if agent_challenges(current_fv, current_m):
                matches = d1.count(current_fv) + d2.count(current_fv)
                print(f"\nDice revealed — Player 1: {d1} | CPU: {d2}")
                print(f"{matches} dice show {current_fv}. Bid was {current_m}.")
                if matches >= current_m:
                    print("Bid was valid. CPU loses a die.")
                    remaining_dices[2] -= 1
                else:
                    print("Bid was incorrect. You lose a die.")
                    remaining_dices[1] -= 1
                break
            else:
                new_fv, new_m = agent_bid(current_fv, current_m)
                print(f"CPU raises to {new_m} dices showing {new_fv}")
                current_fv, current_m = new_fv, new_m
                current_bidder = 1

            challenge = input("Do you challenge? (y/n): ")
            while challenge not in ["y", "n"]:
                print("Invalid input.")
                challenge = input("Do you challenge? (y/n): ")
            if challenge == "y":
                matches = d1.count(current_fv) + d2.count(current_fv)
                print(f"\nDice revealed — Player 1: {d1} | CPU: {d2}")
                print(f"{matches} dice show {current_fv}. Bid was {current_m}.")
                if matches >= current_m:
                    print("Bid was valid. You lose a die.")
                    remaining_dices[1] -= 1
                else:
                    print("Bid was incorrect. CPU loses a die.")
                    remaining_dices[2] -= 1
                break

print("\nGame over.")
if remaining_dices[1] == 0:
    print("CPU wins!")
else:
    print("You win!")