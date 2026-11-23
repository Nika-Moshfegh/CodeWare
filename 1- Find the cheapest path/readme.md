Find the cheapest path

You should be familiar with the "Find the shortest path" problem. But what if moving to a neighboring coordinate counted not as 1 step but as N *steps? *

INSTRUCTIONS

Your task is to find the path through the field which has the lowest cost to go through.

As input you will receive:

a toll_map matrix (as variable t) which holds data about how expensive it is to go through the given field coordinates
a start coordinate (tuple) which holds information about your starting position
a finish coordinate (tuple) which holds information about the position you have to get to
As output you should return:

the directions list
EXAMPLE

INPUT:

toll_map  |  start  |  finish
          |         |
[         |         |
 [1,9,1], |  (0,0)  |  (0,2)
 [2,9,1], |         |
 [2,1,1], |         |
]         |         |



OUTPUT:

["down", "down", "right", "right", "up", "up"]
CLARIFICATIONS

the start and finish tuples represent (row, col) indices
the total cost is increased after leaving the matrix coordinate, not entering it
the field will be rectangular, not necessarily a square
the field will always be of correct shape
the actual tests will check total_cost based on your returned directions list, not the directions themselves, so you shouldn't worry about having multiple possible solutions