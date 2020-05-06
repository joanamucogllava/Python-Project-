# Import modules and custom created functions
import networkx as nx
from functions.weighted_graph_drawings import *
from functions.prims_functions import *

 
def prims_algorithm(G, starting_node, draw = False, attrib = False):
    # This function automates the process to find a Minimum
    # Spanning Tree using Prim's Algorithim
    
    # Initilize T as a graph
    T = nx.Graph()
    
    # Initilize the first node of the subtree T
    T.add_node(starting_node)
    
    # This will draw the Graph G with the starting node of T
    if draw == True:
        draw_subtree(G, T)
    
    # This while loop checks to see if the set of vertices in Subgraph T 
    # is equal to the set of vertices in Graph G
    while set(T.nodes()) != set(G.nodes()):
        e = min_possible_prims_edge(G, T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
        
        # Overlays the subtree T onto the Graph G
        if draw == True:
            draw_subtree(G, T)
    
    # Statistics of the Subgraph T including the list of Vertices(nodes),
    # the list of edges, and the Total Cost of the edge weights summed
    if attrib == True:
        total_cost = sum(cost(G,e) for e in T.edges())
        print('-------------------PROPERTIES OF THE TREE T---------------------')
        print('')
        print('----------------------------------------------------------------')
        print(f'V(T) = {list(T.nodes())}')
        print(f'E(T) = {list(T.edges())}')
        print(f'Total Cost = {total_cost}')
        print('----------------------------------------------------------------')
    
    return T
