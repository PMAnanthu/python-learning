"""Flip coin code"""

import random

if __name__=="__main__":
    rand = random.randint(0,1)
    if rand == 1:
        print("Head")
    else:
        print("Tail")
