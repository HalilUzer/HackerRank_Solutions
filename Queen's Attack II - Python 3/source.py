#!/bin/python3

import math
import os
import random
import re
import sys

class Queen:

    def __init__(self,x_axis,y_axis):
        self.x_axis = x_axis - 1
        self.y_axis = y_axis - 1
    


class Obstacle:

    def __init__(self,x_axis,y_axis):
        self.x_axis = x_axis - 1
        self.y_axis = y_axis - 1
    


class Table:

    def __init__(self,size,queen,obstacles):
        self.queen = queen
        self.__obstacles_temp = obstacles
        self.__obstacles = obstacles
        self.size = size
        self.__north = []
        self.__south = []
        self.__west = []
        self.__east = []
        self.__north_west = []
        self.__north_east = []
        self.__south_west = []
        self.__south_east = []
        self.__closest_north = 0
        self.__closest_south = 0
        self.__closest_west = 0 
        self.__closest_east = 0
        self.__closest_north_west = 0
        self.__closest_north_east = 0
        self.__closest_south_west = 0
        self.__closest_south_east = 0
        self.__determine_obstacle_paths()
        self.__determine_closest()



    def determine_movable_paths(self):
        movable_paths = 0
        
        if self.__closest_north == 0 and self.queen.x_axis != 0:
            movable_paths += self.queen.x_axis
        elif self.queen.x_axis != 0:
            movable_paths += self.queen.x_axis - self.__closest_north.x_axis - 1 #north

        if  self.__closest_south == 0 and self.queen.x_axis != self.size -1:
            movable_paths += self.size - self.queen.x_axis - 1
        elif self.queen.x_axis != self.size -1:
            movable_paths += self.__closest_south.x_axis - self.queen.x_axis  - 1   #south
        
        if self.__closest_east == 0 and self.queen.y_axis != self.size - 1: #east
            movable_paths += self.size - self.queen.y_axis - 1
        elif self.queen.y_axis != self.size - 1:
            movable_paths += self.__closest_east.y_axis - self.queen.y_axis  - 1
        
        if self.__closest_west == 0 and self.queen.y_axis != 0:  #west
            movable_paths += self.queen.y_axis
        elif self.queen.y_axis != 0:
            movable_paths += self.queen.y_axis - self.__closest_west.y_axis - 1  
        
        if self.__closest_north_east == 0 and self.queen.x_axis != 0 and self.queen.y_axis != self.size - 1:
            if self.size -self.queen.y_axis - 1 > self.queen.x_axis:
                movable_paths += self.queen.x_axis
            else:
                movable_paths += self.size - self.queen.y_axis - 1

        elif self.queen.x_axis != 0 and self.queen.y_axis != 0 and self.queen.y_axis != self.size - 1:
            movable_paths += self.__closest_north_east.y_axis - self.queen.y_axis - 1  #north east
        
        if self.__closest_north_west == 0 and self.queen.x_axis != 0 and self.queen.y_axis != 0:
            if self.queen.y_axis > self.queen.x_axis:
                movable_paths += self.queen.x_axis
            else:
                movable_paths += self.queen.y_axis
        elif self.queen.x_axis != 0 and self.queen.y_axis != 0:
            movable_paths += self.queen.y_axis - self.__closest_north_west.y_axis - 1 #north west
        
        if self.__closest_south_east == 0 and self.queen.x_axis != self.size - 1 and self.queen.y_axis != self.size - 1:
            if self.size - self.queen.x_axis - 1 > self.size - self.queen.y_axis - 1:
                movable_paths += self.size - self.queen.y_axis - 1
            else:
                movable_paths += self.size - self.queen.x_axis - 1
        elif self.queen.x_axis != self.size - 1 and self.queen.y_axis != self.size - 1:
            movable_paths += self.__closest_south_east.y_axis - self.queen.y_axis - 1  #south east
        
        if self.__closest_south_west == 0 and self.queen.x_axis != self.size -1 and self.queen.y_axis != 0: #south west
            if self.size - self.queen.x_axis - 1  > self.queen.y_axis:
                movable_paths += self.queen.y_axis
            else:
                movable_paths += self.size - self.queen.x_axis - 1
        elif self.queen.x_axis != self.size -1 and self.queen.y_axis != 0:    
            movable_paths += self.queen.y_axis - self.__closest_south_west.y_axis - 1 
        
        return movable_paths



    def __determine_closest(self):

        if len(self.__obstacles) == 0:
            return

        if len(self.__north) != 0:   
            closest_obstacle = self.__north[0]

            for obstacle in self.__north:        #north
                if abs(self.queen.x_axis - closest_obstacle.x_axis) + abs(self.queen.y_axis - closest_obstacle.y_axis) > abs(self.queen.x_axis - obstacle.x_axis) + abs(self.queen.y_axis - obstacle.y_axis):
                    closest_obstacle = obstacle
            self.__closest_north = closest_obstacle

        if len(self.__south)  != 0:
            closest_obstacle = self.__south[0]

            for obstacle in self.__south:   #south
                if abs(self.queen.x_axis - closest_obstacle.x_axis) + abs(self.queen.y_axis - closest_obstacle.y_axis) > abs(self.queen.x_axis - obstacle.x_axis) + abs(self.queen.y_axis - obstacle.y_axis):
                    closest_obstacle = obstacle
        
            self.__closest_south = closest_obstacle
        
        if len(self.__west) != 0:
        
            closest_obstacle = self.__west[0]

            for obstacle in self.__west:    #west
                if abs(self.queen.x_axis - closest_obstacle.x_axis) + abs(self.queen.y_axis - closest_obstacle.y_axis) > abs(self.queen.x_axis - obstacle.x_axis) + abs(self.queen.y_axis - obstacle.y_axis):
                    closest_obstacle = obstacle
        
            self.__closest_west = closest_obstacle

        if len(self.__east) != 0:

            closest_obstacle = self.__east[0]

            for obstacle in self.__east:    #east
                if  abs(self.queen.x_axis - closest_obstacle.x_axis) + abs(self.queen.y_axis - closest_obstacle.y_axis) > abs(self.queen.x_axis - obstacle.x_axis) + abs(self.queen.y_axis - obstacle.y_axis):
                    closest_obstacle = obstacle
        
            self.__closest_east = closest_obstacle


        if len(self.__north_east) != 0:

            closest_obstacle = self.__north_east[0]

            for obstacle in self.__north_east:  #north east
                if  abs(self.queen.x_axis - closest_obstacle.x_axis) + abs(self.queen.y_axis - closest_obstacle.y_axis) > abs(self.queen.x_axis - obstacle.x_axis) + abs(self.queen.y_axis - obstacle.y_axis):
                    closest_obstacle = obstacle
        
            self.__closest_north_east = closest_obstacle
        
        if len(self.__north_west) != 0:

            closest_obstacle = self.__north_west[0]

            for obstacle in self.__north_west:  #north west
                if  abs(self.queen.x_axis - closest_obstacle.x_axis) + abs(self.queen.y_axis - closest_obstacle.y_axis) > abs(self.queen.x_axis - obstacle.x_axis) + abs(self.queen.y_axis - obstacle.y_axis):
                    closest_obstacle = obstacle
        
            self.__closest_north_west = closest_obstacle  

        if len(self.__south_east) != 0:

            closest_obstacle = self.__south_east[0]

            for obstacle in self.__south_east:  #south east
                if  abs(self.queen.x_axis - closest_obstacle.x_axis) + abs(self.queen.y_axis - closest_obstacle.y_axis) > abs(self.queen.x_axis - obstacle.x_axis) + abs(self.queen.y_axis - obstacle.y_axis):
                    closest_obstacle = obstacle
        
            self.__closest_south_east = closest_obstacle
        

        if len(self.__south_west) != 0:

            closest_obstacle = self.__south_west[0]

            for obstacle in self.__south_west:  #south west
                if  abs(self.queen.x_axis - closest_obstacle.x_axis) + abs(self.queen.y_axis - closest_obstacle.y_axis) > abs(self.queen.x_axis - obstacle.x_axis) + abs(self.queen.y_axis - obstacle.y_axis):
                    closest_obstacle = obstacle
        
            self.__closest_south_west = closest_obstacle
    
    

    def __determine_obstacle_paths(self):
        for obstacle in self.__obstacles_temp:
            if obstacle.y_axis == self.queen.y_axis and obstacle.x_axis < self.queen.x_axis:
                self.__north.append(obstacle)
                del obstacle
        
        for obstacle in self.__obstacles_temp:
            if obstacle.y_axis == self.queen.y_axis and obstacle.x_axis > self.queen.x_axis:
                self.__south.append(obstacle)
                del obstacle
        
        for obstacle in self.__obstacles_temp:
            if obstacle.x_axis == self.queen.x_axis and obstacle.y_axis < self.queen.y_axis:
                self.__west.append(obstacle)
                del obstacle
                
        
        for obstacle in self.__obstacles_temp:
            if obstacle.x_axis == self.queen.x_axis and obstacle.y_axis > self.queen.y_axis:
                self.__east.append(obstacle)
                del obstacle
        
        for obstacle in self.__obstacles_temp:
            k =  abs(self.queen.x_axis  - obstacle.x_axis)
            if obstacle.x_axis < self.queen.x_axis and obstacle.y_axis > self.queen.y_axis and self.queen.y_axis + k == obstacle.y_axis:
                self.__north_east.append(obstacle)
                del obstacle

        for obstacle in self.__obstacles_temp:
            k = abs(self.queen.x_axis - obstacle.x_axis)
            if obstacle.x_axis < self.queen.x_axis and obstacle.y_axis < self.queen.y_axis and self.queen.y_axis - k == obstacle.y_axis:
                self.__north_west.append(obstacle)
                del obstacle
        
        for obstacle in self.__obstacles_temp:
            k = abs(self.queen.x_axis - obstacle.x_axis)
            if obstacle.x_axis  > self.queen.x_axis and obstacle.y_axis > self.queen.y_axis and self.queen.y_axis + k == obstacle.y_axis:
                self.__south_east.append(obstacle)
                del obstacle
        
        for obstacle in self.__obstacles_temp:
            k = abs(self.queen.x_axis - obstacle.x_axis)
            if obstacle.x_axis > self.queen.x_axis and obstacle.y_axis < self.queen.y_axis and self.queen.y_axis - k == obstacle.y_axis:
                self.__south_west.append(obstacle) 
                del obstacle
# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    my_queen = Queen(r_q,c_q)
    my_obstacles = []
    for obstacle in obstacles:
        my_obstacles.append(Obstacle(obstacle[0],obstacle[1]))
    
    my_table = Table(n,my_queen,my_obstacles)
    blocks = my_table.determine_movable_paths()
    return blocks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
