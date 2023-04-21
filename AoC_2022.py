#!/usr/bin/env python

###Advent of Code 2022 
####Import functions 
import sys 

##############################
#                            #
#   Day 1 calorie counting   #
#   ######################   #
#                            #
##############################
####Open and split data 
data=open(sys.argv[1]).read().split('\n\n')

####Transform string to a list of integers 
int_list=[tuple(map(int, x.split())) for x in data]

####Find the highest value of the list of tuples
highest_val=max(map(sum, int_list)) 
print(highest_val)

####(Part2) 
####Order intlit by sum of values descending 
int_list.sort(key=sum, reverse=True)
largest_val_3=sum(map(sum, int_list[:3]))
print(largest_val_3)

#################################
#                               #
#   Day 2 rock paper scissors   #
#   #########################   #
#                               #
#################################

####Open and split data 
data=open(sys.argv[1]).read().strip().split('\n')

###Dict of possible results
poss_results={"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9, "C X":7, "C Y":2, "C Z":6}

####Add up points 
points=0
for x in data:
	points+=poss_results[x]

print (points)

####(Part2)
####Manipulate winning and losing 
man_poss_results={"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9, "C X":2, "C Y":6, "C Z":7}

####Add up points 
points_2=0
for x in data:
	points_2+=man_poss_results[x]

print(points_2)

#####################################
#                                   #
#   Day 3 rucksack reorganisation   #
#   #############################   #
#                                   #
#####################################
from string import ascii_letters

####Open and split data 
data=open(sys.argv[1]).read().strip().split("\n")

#Find length of half rucksack and set of unique characters in the left and right side 
count=0
for x in data:
	y=len(x)//2
	leftside=set(x[:y])
	rightside=set(x[y:])
#	print (x, leftside, rightside)
	for n,l in enumerate(ascii_letters):
		if l in leftside and l in rightside:
			count+=n+1

print (count)

####(Part2)
####Iterate through rucksacks in threes and find common character 
count=0
end=3
for x in range(0, len(data),3):
	r=data[x:end]
	end+=3
	#print (r)
	for n,l in enumerate(ascii_letters):
		if l in r[0] and l in r[1] and l in r[2]:
			count+=n+1

print (count) 


