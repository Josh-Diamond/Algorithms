#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    outcomes = []

    def find_outcome(n: int, result: list):
        if n == 0:
            outcomes.append(result)
            return
        for play in plays:
            find_outcome(n-1, result + [play])
    find_outcome(n, [])
    return outcomes

print(rock_paper_scissors(2))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')