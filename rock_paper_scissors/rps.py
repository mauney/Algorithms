#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    # set up a lists of lists
    combos = [[None for _ in range(n)] for _ in range(3**n)]
    # loop through each position in a sequence
    for i in range(n):
        divisor = 3**(n - i - 1)
        # for every sequence assign a value to the ith element
        for j, sequence in enumerate(combos):
            sequence[i] = plays[(j // divisor) % 3]

    return combos



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')