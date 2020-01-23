#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# # recursive solution
# def eating_cookies_naive(n, cache=None):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache={0:1, 1:1, 2:2, 3:4}):
    # global calls
    # calls += 1
    if n not in cache:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

# calls = 0
# for n in [10, 20, 30, 40, 50]:
#     print(f'There are {eating_cookies(n)} ways for Cookie Monster to eat {n} cookies.')
#     print(f'This took {calls} calls\n')
#     calls = 0

# ans = 10562230626642

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')