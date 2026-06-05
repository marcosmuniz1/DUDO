import math
import random

def binom_cdf(k, n, p):
    total = 0
    for i in range(k + 1):
        coeff = math.comb(n, i)
        total += coeff * (p ** i) * ((1 - p) ** (n - i))
    return total

def agent_challenges(current_fv, current_m, agent_dice, total_dice):
    # how many matches the agent can directly observe
    observed = agent_dice.count(current_fv)
    
    # how many matches still needed from unknown dice
    m_unobserved = current_m - observed
    if m_unobserved <= 0:
        return False
    
    # unknown dice are everything except the agent's own
    unknown_dice = total_dice - len(agent_dice)
    
    # probability that unknown dice produce enough matches to meet the bid
    p_valid = 1 - binom_cdf(m_unobserved - 1, unknown_dice, 1/6)
    return random.random() > p_valid

def agent_bid(current_fv, current_m, agent_dice, total_dice):
    return current_fv, current_m + 1

