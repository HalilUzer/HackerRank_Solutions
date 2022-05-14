#!/bin/python3

import os
import sys


class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None
        self.health = 2


class BinaryTree:

    def __init__(self, data):
        self.root = Node(data)
        self.queue = []
        self.queue.append(self.root)

    def insert(self, data, left_right):
        new = Node(data)

        
        if left_right is True:
            self.queue[0].left = new

            self.queue.append(new)
                
        else:
            self.queue[0].right = new

            self.queue.append(new)

        


    
    def _traversal_private(self, foot, values):

        if foot:
            self._traversal_private(foot.left, values)
            values.append(foot.data)
            self._traversal_private(foot.right, values)

    def traversal(self):

        values = []

        self._traversal_private(self.root, values)

        return values
    

    def _swap_private(self, node, depth, swap_depth):
        if node:

            if depth % swap_depth == 0:

                temp = node.left
                node.left = node.right
                node.right = temp
        
            self._swap_private(node.left, depth + 1, swap_depth)
            self._swap_private(node.right, depth + 1, swap_depth)

        

    def swap(self, swap_depth):

        self._swap_private(self.root, 1, swap_depth)



#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):

    results = [[]  for _ in range(len(queries))]
    

    tree = BinaryTree(1)

    counter = 0

    for indexes_2 in indexes:
        
        for index in indexes_2:
            while True:
                
                if tree.queue[0].health > 0 and  index != -1:

                    if counter % 2 == 0:
                        tree.insert(index, True) 

                    else:
                        tree.insert(index, False)
                    
                    tree.queue[0].health -= 1

                    counter += 1

                    break

                elif tree.queue[0].health <= 0:
                    
                    del tree.queue[0]
                    continue

                elif index == -1:

                    tree.queue[0].health -= 1

                    counter += 1

                    break
            
                

      

                
    counter = 0

    for querie in queries:
        tree.swap(querie)
        results[counter].append(tree.traversal())
        counter += 1 

    return results
        
        
    

if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    results = swapNodes(indexes, queries)
    for result in results:
        fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
        fptr.write('\n')

    fptr.close()
