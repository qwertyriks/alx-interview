#!/usr/bin/python3
""" A Module for 0-minoperations"""

def minOperations(n):
    """
    Getting the fewest of operations needed to result in exactly n H characters
    """
    # Now, all outputs should be at least 2 char long: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root,
        if n % root == 0:
            # the total even divisions by root = total operations
            ops += root
            # sets n to the remainder
            n = n / root
            # should reduce root to find remaining smaller values that evenly-divide n
            root -= 1
            # increment root until it evenly-divides n
        root += 1
    return ops