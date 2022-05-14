# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

list_number, modulus_number = map(int ,input().split())
ls = [[num for num in map(int, input().split()[1:])] for _ in range(list_number)]
print(max(map(lambda x: sum(i**2 for i in x) % modulus_number, itertools.product(*ls))))