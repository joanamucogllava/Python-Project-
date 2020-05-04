def cost(graph, e):
    return graph.edges()[e]['weight']

def is_spanning(graph, subgraph):
    return graph.nodes() == subgraph.nodes()

def possible_prims_edges(graph, tree):
    possible_e = []
    for e in set(graph.edges()) - set(tree.edges()):
        for v in tree.nodes():
            if v in e:
                possible_e.append(e)
            
    return possible_e


def min_possible_prims_edge(G, T):
    possible_e = possible_prims_edges(G, T)
    min_e = possible_e[0]
    for e in possible_e:
        if cost(G, e) < cost(G, min_e):
            min_e = e
     return min_e
