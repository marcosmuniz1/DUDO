## DUDO Simulator

Work in progress - missing UI interface ----


Game Overview
A turn-based dice bidding game in which players make escalating claims about the total number of dice showing a given face value across all players. Each bid must be strictly higher than the previous, either by increasing the quantity, the face value, or both. A round end when a bid is challenged, with the loser surrendering a dice

Agent Bidding Logic
The agent uses a probabilistic strategy to select the best available bid. On its turn it:

* Builds a bid universe — considers all face values (1–6) paired with quantities of current_m and current_m + 1, filtering to only those that legally exceed the current bid.
Estimates probability for each candidate bid by:

- Counting how many matching dice the agent can already see in its own hand.
Computing how many additional matches are needed from the unseen dice (m_unobserved).
- Using a binomial CDF to calculate the probability that the unknown dice supply enough matches, assuming each die shows any given face with probability 1/6.

* Returns the bid with the highest probability of being valid — if the agent's own dice already satisfy a bid outright, that bid is returned immediately with certainty.

A similar logic is used to evaluate the rival's (users) bid and choosing to challenge or accept them, and therefore raise