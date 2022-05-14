# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools


length, letters, select_count = int(input()), input().split(), int(input())
combinations = list(itertools.combinations(letters, select_count))
k = len(combinations)
includes = len(list(filter(lambda x: 'a' in x, combinations)))
print(float(includes) / float(k))