"""

This is the main Python script to run to determine Prim's MST 
for any graph G. 

Follow the instructions in the Console to begin

"""


from algorithims.prims import *
from functions.OS_Check import *


T = prims_algorithm(G,int(input('Choose a node to begin: ')), True, True)
