from itertools import permutations
def permut(s) :
    for i in permutations(s) :
        print(''.join(i))

s=str(input())
permut(s)

