#!/bin/python3

import os
import sys

class Stack:

    def __init__(self):
        self.values = []


    def push(self, data):

        self.values.append(data)

    def pop(self):

        value = self.values[-1]
        del self.values[-1]
        return value

    def is_empty(self):

        if len(self.values) == 0:

            return True

        else:

            return False

    def __len__(self):

        return len(self.values)


    def top(self):

        return self.values[-1]

    def copy(self):

        cop = Stack()

        for value in self.values:
            cop.values.append(value)

        return cop



def first_N_primes(N): 
    prime_numbers = []
    # Declare the variables 
    i, j, flag = 0, 0, 0; 
  
  
    # Traverse each number from 1 to N 
    # with the help of for loop 
    for i in range(1, N + 1, 1): 
  
        # Skip 0 and 1 as they are 
        # niether prime nor composite 
        if (i == 1 or i == 0): 
            continue; 
  
        # flag variable to tell 
        # if i is prime or not 
        flag = 1; 
  
        for j in range(2, ((i // 2) + 1), 1): 
            if (i % j == 0): 
                flag = 0; 
                break; 
  
        # flag = 1 means i is prime 
        # and flag = 0 means i is not prime 
        if (flag == 1): 
            prime_numbers.append(i)


    return prime_numbers
            


def waiter(number, q):

    waiting_plates = Stack()
    B = []
    results = []
    non_divisible_plates = Stack()
    
    primes = first_N_primes(10000)

    for num in number:
        waiting_plates.push(num)

   

    for ith in range(q):
        B.append(Stack())

        while waiting_plates.is_empty() is False:
            waiting_plate = waiting_plates.pop()

            if waiting_plate % primes[ith] == 0:

                B[-1].push(waiting_plate)

            else:
                non_divisible_plates.push(waiting_plate)

        
        waiting_plates = non_divisible_plates.copy()
        non_divisible_plates = Stack()


    for B_stack in B:
        
        while B_stack.is_empty() is False:

            results.append(B_stack.pop())


    while  waiting_plates.is_empty() is False:

        results.append(waiting_plates.pop())

    return results


    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
