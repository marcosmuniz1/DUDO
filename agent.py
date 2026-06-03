from scipy.stats import binom

def agent_challenges(current_fv, current_m, agent_dice, total_dice):
    return False

def agent_bid(current_fv, current_m, agent_dice=1, total_dice=2):
    ## calculation is meaningless untill i pass the real parameters in games
    # how many matches the agent can directly observe
    observed = agent_dice.count(current_fv)
    
    # how many matches still needed from unknown dice
    m_unobserved = current_m - observed
    
    # unknown dice are everything except the agent's own
    unknown_dice = total_dice - len(agent_dice)
    
    # probability that unknown dice produce enough matches to meet the bid
    p_valid = 1 - binom.cdf(m_unobserved - 1, unknown_dice, 1/6)
    
    print(f"[agent] observed={observed}, need {m_unobserved} from {unknown_dice} unknown dice, p_valid={p_valid:.2f}")
    
    return current_fv, current_m + 1