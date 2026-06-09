import random
from agent import agent_challenges, agent_bid

def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]

class Game:
    def __init__(self):
        self.remaining_dices = {1: 5, 2: 5}
        self.rnum = 0
        self.d1 = []
        self.d2 = []
        self.current_fv = 0
        self.current_m = 0
        self.current_bidder = 1
        self.total_dice = 10

    def start_round(self):
        self.rnum += 1
        self.total_dice = self.remaining_dices[1] + self.remaining_dices[2]
        self.d1 = roll_dice(self.remaining_dices[1])
        self.d2 = roll_dice(self.remaining_dices[2])
        self.current_fv = 0
        self.current_m = 0
        self.current_bidder = 1

    def player_bid(self, fv, m):
        if not (fv > self.current_fv or m > self.current_m):
            return {"error": "Must raise face value or matches"}
        self.current_fv = fv
        self.current_m = m
        return self.cpu_turn()

    def cpu_turn(self):
        if agent_challenges(self.current_fv, self.current_m, self.d2, self.total_dice):
            result = self.resolve_challenge(challenger=2)
            return {"cpu_action": "challenge", **result}
        else:
            new_fv, new_m = agent_bid(self.current_fv, self.current_m, self.d2, self.total_dice)
            self.current_fv = new_fv
            self.current_m = new_m
            return {"cpu_action": "bid", "fv": new_fv, "m": new_m}

    def player_challenge(self):
        return self.resolve_challenge(challenger=1)

    def resolve_challenge(self, challenger):
        matches = self.d1.count(self.current_fv) + self.d2.count(self.current_fv)
        bid_valid = matches >= self.current_m
        loser = 2 if (challenger == 2 and bid_valid) or (challenger == 1 and not bid_valid) else 1
        self.remaining_dices[loser] -= 1
        return {
            "matches": matches,
            "bid_valid": bid_valid,
            "loser": loser,
            "d1": self.d1,
            "d2": self.d2,
            "remaining_dices": dict(self.remaining_dices)
        }

    def is_over(self):
        return self.remaining_dices[1] == 0 or self.remaining_dices[2] == 0