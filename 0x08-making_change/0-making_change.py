#!/usr/bin/python3
"""Testing File"""

def makeChange(coins, amount):
    """
    Types of coins?
    How many left. How much money left?
    How many coins in my pocket?
    """
    
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        amount -= num * coin
        count += num
    return count if amount == 0 else -1
