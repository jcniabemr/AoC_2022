#!/usr/bin/env python

###Advent of Code 2022 
####Import functions 
import sys 

####Day 1 (Part1) Calorie counting 
####Open and split data 
#data=open(sys.argv[1]).read().split('\n\n')
####Transform string to a list of integers 
#int_list=[tuple(map(int, x.split())) for x in data]
####Find the highest value of the list of tuples
#highest_val=max(map(sum, int_list)) 
#print('The highest single sum value is', highest_val)
####Day 1 (Part2) 
####Order intlit by sum of values descending 
#int_list.sort(key=sum, reverse=True)
#largest_val_3=sum(map(sum, int_list[:3]))
#print('The sum of the sum of the largest three is', largest_val_3)


###Day2 (Part1) Rock paper scissors 
SCORES = (
    1 + 3, # A (rock)     vs X (rock)     -> draw
    2 + 6, # A (rock)     vs Y (paper)    -> win
    3 + 0, # A (rock)     vs Z (scissors) -> loss
    1 + 0, # B (paper)    vs X (rock)     -> loss
    2 + 3, # B (paper)    vs Y (paper)    -> draw
    3 + 6, # B (paper)    vs Z (scissors) -> win
    1 + 6, # C (scissors) vs X (rock)     -> win
    2 + 0, # C (scissors) vs Y (paper)    -> loss
    3 + 3, # C (scissors) vs Z (scissors) -> draw
)

table=str.maketrans('ABCXYZ', '036123')

data=open(sys.argv[1]).read().translate(table)

for x in data.splitlines():
	a,b=map(int, x.split())
	score += SCORE[a+b]

print('RPS Score ='score)