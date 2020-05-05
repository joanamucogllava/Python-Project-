"""

This Script Initializes the program and also checks to 
see what Operating System it is being executed on

"""

import networkx as nx
from sys import platform

print('')
print("-----------------PRIM'S ALGORITHIM----------------")
print('')
print('--------------------------------------------------')
print('')
print('The available graphs to select are G1, G2, or G3')
print('')
print("Initialize Prim's Algorithim below")
print('')
print('--------------------------------------------------')
choose_graph = input('Select one of the graphs by typing either G1, G2, or G3 here: ')


# If the user selected G1, the code below will check their
# OS then set the intial graph, G, to the text document G1
# using the proper file path notation
if choose_graph == 'G1':
    print('')
    print('-------------------------')
    print('Choose a node between 0-7')
    print('-------------------------')
    if platform == "linux" or platform == "linux2":
        # linux
        G = nx.read_weighted_edgelist('data/G1.txt',
                              nodetype = int)
    elif platform == "darwin":
        #OSX
        G = nx.read_weighted_edgelist('data/G1.txt',
                              nodetype = int)
        
    elif platform == "win32":
        #Windows
        G = nx.read_weighted_edgelist('data\G1.txt',
                              nodetype = int)
        

# If the user selected G2, the code below will check their
# OS then set the intial graph, G, to the text document G2
# using the proper file path notation   
if choose_graph == 'G2':
    print('')
    print('--------------------------')
    print('Choose a node between 0-12')
    print('--------------------------')
    if platform == "linux" or platform == "linux2":
        # linux
        G = nx.read_weighted_edgelist('data/G2.txt',
                              nodetype = int)
    elif platform == "darwin":
        #OSX
        G = nx.read_weighted_edgelist('data/G2.txt',
                              nodetype = int)
    elif platform == "win32":
        #Windows
        G = nx.read_weighted_edgelist('data\G2.txt',
                              nodetype = int)

        
# If the user selected G3, the code below will check their
# OS then set the intial graph, G, to the text document G3
# using the proper file path notation        
if choose_graph == 'G3':
    print('')
    print('-------------------------')
    print('Choose a node between 0-8')
    print('-------------------------')
    if platform == "linux" or platform == "linux2":
        # linux
        G = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
    elif platform == "darwin":
        #OSX
        G = nx.read_weighted_edgelist('data/G3.txt',
                              nodetype = int)
    elif platform == "win32":
        #Windows
        G = nx.read_weighted_edgelist('data\G3.txt',
                              nodetype = int)
