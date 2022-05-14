#!/bin/python3

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = input()
    counter =  collections.Counter(s)
    counter = sorted(counter.items(), key=lambda x: x[0])
    counter = sorted(counter, key=lambda x: x[1], reverse=True)
    for item in counter[:3:]:
        print(' '.join(map(str, item)))
    