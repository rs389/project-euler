# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:30:28 2017

@author: Ronak
"""

# define a conditions function to check if we should move to new iteration


def conditions(visits, index, direction, n):
    # returns True if we can go ahead or False if no valid paths left 
   
    # set parity to be a list of parities from the visits
    parity = [i % 2 for i in visits]
   
    # if you just filled a node
    if visits[index] == n:
       # then check parity of next node
       
       # if parity of the next node is even (before going to that node)
       if parity[(index + direction) % 5] == 0:
           # then we need all others to be even too
           for i in range(1,4):
               # check 'other' nodes by going in minius the direction
               if parity[(index - i*direction) % 5] == 1:
                   return False
       
        # else the parity of the next node is odd (before going to it)
        # check if the other neighbour is also odd
       elif parity[(index - direction) % 5] == 1:
           # then we need the remaining two to be odd too
           if parity[(index - 2 * direction) % 5] == 0:
               return False
           if parity[(index - 3 * direction) % 5] == 0:
               return False
     
    return True       



# start reading code from point *** below. Then read the function

# define function to iterate over paths
# n is path length divided by 5
def iterate(visits, index, direction, count, n):
	
	# if complete path or failed path, stop. Otherwise branch out
	
	# if you have reached a complete path
	if all(i == n for i in visits):
		count[0] += 1
		
	# else if not in invalid state, branch out
	elif all(i <= n for i in visits):
		
		# make copies for branching
		vc = list(visits)
		ic = list(index)
		dc = list(direction)
		
		# if you move forward, add one to next index
		index[0] = (index[0] + 1) % 5
		visits[index[0]] += 1
		iterate(visits, index, direction, count, n)
		
		# if you change direction, add one to current index
		vc[ic[0]] += 1
		dc[0] *= -1
		iterate(vc, ic, dc, count, n)


# point***

# start on node 0 wlog.
visits = [1,0,0,0,0]

# we are starting on node 0
index = [0]

# set direction to be clockwise (+1) to start. -1 is anticlockwise
direction = [1]

# counts number of complete paths
count = [0]

iterate(visits, index, direction, count, 4)
# started at node 0 (0R). could have started at 4 (0L). so double result
print(count[0]*2)