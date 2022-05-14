#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    arr = [0] * n
    
    for querie in queries:
        querie[0] -= 1 
        querie[1] -= 1
        arr[querie[0]] += querie[2]
        if querie[1] != n - 1:
            arr[querie[1] + 1] -= querie[2]
            
    ma = 0
    su = 0
    for number in arr:
      su += number
      if su > ma:
        ma = su
        
    
    return ma
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
