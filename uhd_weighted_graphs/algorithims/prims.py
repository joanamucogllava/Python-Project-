import networkx as nx
from functions.weighted_graph_drawings import *
from functions.prims_functions import *


def prims_algorithm(G, starting_node, draw = False, attrib = False):
    
    T = nx.Graph()
    T.add_node(starting_node)
    
    if draw == True:
        draw_subtree(G, T)
    
    while set(T.nodes()) != set(G.nodes()):
        e = min_possible_prims_edge(G, T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
        
        if draw == True:
            draw_subtree(G, T)
    
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