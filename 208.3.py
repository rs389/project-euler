# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 10:36:29 2017

@author: Ronak
"""


def getdirections(moves):
    # takes a list of moves (-1 for L and +1 for R)
    # returns list d of directions faced before the corresponding move
    # d[0] = 0 since you always start facing north which is zero 

    # starting direction
    current = 0
    d = [0]
  
    # make list of directions
    for move in moves:
        current = (current + move) % 5
        d.append(current)
  
    # remove the last one (ending direction) else you have #moves + 1 directions
    d.pop()
    
    return d
    

def addtoclass(moves):
  # creates 5 classes 0R = 1L, 1R = 2L, ..., 4R = 0L
  # moves is an ordered sequence of moves (-1 is L and +1 is R)
  # direction is a list of directions (0 to 4) faced before the corresponding move
  
  # in order we have classes 0R, ..., 3R, 4R which also correspond to 1L, ..., 4L, 0L
  classes = [0,0,0,0,0]
  
  directions = getdirections(moves)
  
  # first look at right moves (+1). looking at classes 0R, ..., 4R
  for i in range(len(moves)):
    if moves[i] == +1:
      classes[directions[i]] += 1
  
  # corresponding left moves classes are 1L,..., 4L, 0L
  for i in range(len(moves)):
    if moves[i] == -1:
      classes[(directions[i] - 1) % 5] += 1
  
  return classes


def check(moves):
  # checks if a set of moves results in a closed loop
  # moves is a list of +1s (Right moves) and -1s (Left moves)
  
  # make congruency classes
  classes = addtoclass(moves)
  
  # check if size of all classes is equal
  return (all(x == classes[0] for x in classes))


#moves = [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1 1,1,1,1,1, 1,1,1,1,1]

def stillsmall(l):
    # checks if any item in the list is greater than n/5
    for item in l:
        if item > 5:
            return False
    return True


def generate(moves, directions, classes, l):
    # moves is current state of moves
    # directions is current state of directions
    # classes is current state of classes
    
    # goes through all possible moves incrementing counter if valid loop
    # l is a list but just has one element counting complete loops
    
    # if you have a full path then check if it is a loop and increment the counter
    if len(moves) == 25:
        if (all(x == classes[0] for x in classes)):
            l[0] += 1
    
    # if your path is not yet full, check if it can still make a loop
    # if it cannot make a loop (one of the classes > n/5), then dont pursue it    
    elif stillsmall(classes):
        
        # make a copy of the current moves, classes and directions
        tm = list(moves)
        td = list(directions)
        tc = list(classes)
        
        # add a right turn 
        # add +1 to the moves, and update directions and classes
        tm.append(1)
        td.append((directions[-1] + moves[-1]) % 5)
        tc[td[-1]] += 1
        
        # add a left turn
        # add -1 to the moves. directions will be same as above. update classes
        moves.append(-1)
        directions = td
        classes[(td[-1] - 1) % 5] += 1
        
        generate(moves, directions, classes, l)
        generate(tm, td, tc, l)
        
#moves = [-1,1,-1,-1, -1,1,1,1, 1,-1,1,1, -1,1,-1,-1, -1,-1,1,-1, -1,1,-1,-1, -1]
l = [0]
moves = [-1]
directions = [0]
classes = [0,0,0,0,1]
generate(moves, directions, classes, l)
print(l[0]*2)