# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

def take_pile(test_case):
    pile = []
    while len(test_case) != 0:
        if test_case[0] > test_case[-1]:
            pile.append(test_case.popleft())
        else:
            pile.append(test_case.pop())
                   
    return pile


def check_condition(pile):
    for i in range(len(pile) - 1):
        if pile[i] < pile[i + 1]:
            return False
    return True
    

test_case_count = int(input())
test_cases = []
for _ in range(test_case_count): 
    input()
    test_cases.append(collections.deque(x for x in map(int, input().split())))
    
for test_case in test_cases:
    pile = take_pile(test_case)
    print('Yes') if check_condition(pile) else print('No')
