#!/bin/python3

import math
import os
import random
import re
import sys


class Stack:

    def __init__(self):
        self.values = []


    def push(self, data):

        self.values.append(data)

    def pop(self):

        if self.is_empty() is True:
            raise Exception('Stack is empty')

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

# Complete the isBalanced function below.
def isBalanced(s):
    matched_brackets = {'(':')', '{':'}', '[':']'}
    opening_brackets = Stack()
    opening_bracket_types = ['(', '{', '[']
    closing_bracket_types = [')', '}', ']']


    for ch in s:

        if ch in opening_bracket_types:

            opening_brackets.push(ch)

        elif ch in closing_bracket_types:

            try:
                opening_bracket = opening_brackets.pop()

            except Exception:
                
                return 'NO'


            if matched_brackets[opening_bracket] != ch:

                return 'NO'

        else:

            continue

    if opening_brackets.is_empty() is True:

        return 'YES'

    else:

        return 'NO'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
