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

#########################
                        #
  Day 4 camp cleanup    #
  ##################    #
                        #
#########################


###Open and split data 
data=open(sys.argv[1]).read().strip().split("\n")

####Find overlaps 
overlaps=0
for x in data:
	f,s=x.split(",")
#	print (f,s)
	firstval=[int(y) for y in f.split("-")]
	secondval=[int(y) for y in s.split("-")]
	#print (firstval, secondval)
	if firstval[0] <= secondval[0] and firstval[1] >= secondval[1]:
		overlaps+=1
	elif secondval[0] <= firstval[0] and secondval[1] >= firstval[1]:
		overlaps+=1

print (overlaps)	

####(Part2)
###Find overlaps in pairs of data 
overlaps=0
for x in data:
	f,s=x.split(",")
	firstval=[int(y) for y in f.split("-")]
	secondval=[int(y) for y in s.split("-")]
	if firstval[0] in range(secondval[0], secondval[1]+1) or firstval[1] in range(secondval[0], secondval[1]+1):
		overlaps+=1
	elif secondval[0] in range(firstval[0], firstval[1]+1) or secondval[1] in range(firstval[0], firstval[1]+1):
		overlaps+=1

print (overlaps)    

##########################
#                        #
#   Day 5 crate moving   #
#   ##################   #
#                        #
##########################

####Open data and spit by linebreak put top list in stack strings and bottom list in instructions  
with open(sys.argv[1]) as file:
	stack_strings,instructions=(i.splitlines() for i in file.read().strip("\n").split("\n\n"))

####Store crate values (stack strings[-1]) in dict as key and stacks is list and replace empty spaces 
stacks={int(digit):[] for digit in stack_strings[-1].replace(" ","")}

###Check stacks 
def displaystacks():
	print("\n\nStacks:\n")
	for stack in stacks:
		print(stack,stacks[stack])
	print("\n")

#displaystacks()

####Find indexes of crate numbers to allow assignent of crate characters later 
indexes=[index for index, char in enumerate(stack_strings[-1]) if char !=" "]

####Load stacks characters into dict, use insert to add to beginning of list 
def loadstacks():
	for string in stack_strings[:-1]:
		stack_num=1
		for index in indexes:
			if string[index] != " ":
				stacks[stack_num].insert(0,string[index])
			stack_num+=1

def emptystacks():
	for stack_num in stacks:
		stacks[stack_num].clear()

def getStackEnds():
	answer=""
	for stack in stacks:
		answer+=stacks[stack][-1]
	return answer


loadstacks()
#emptystacks()
#displaystacks()

for instruction in instructions:
	instruction=instruction.replace("move","").replace("from ","").replace("to ","").strip().split(" ")
	instruction=[int(i) for i in instruction]
	crates=instruction[0]
	from_stack=instruction[1]
	to_stack=instruction[2]
	for crate in range(crates):
		crate_removed=stacks[from_stack].pop()
		stacks[to_stack].append(crate_removed)

#Part 1 answer
print(getStackEnds())

####(Part2)
emptystacks()
loadstacks()

for instruction in instructions:
	instruction=instruction.replace("move","").replace("from ","").replace("to ","").strip().split(" ")
	instruction=[int(i) for i in instruction]
	crates=instruction[0]
	from_stack=instruction[1]
	to_stack=instruction[2]
####Get a list of how many crates to remove, from the end so - and : to go to the end	
	crates_to_remove=stacks[from_stack][-crates:]
####Remove crates from the beginning up to crated to remove
	stacks[from_stack]=stacks[from_stack][:-crates]
####Add crates to a different stack 
	for crate in crates_to_remove:
		stacks[to_stack].append(crate)

print(getStackEnds())