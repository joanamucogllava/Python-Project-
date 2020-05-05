def cost(graph, e):
    return graph.edges()[e]['weight']


def valid_incident_edges(graph, tree):
    edges = []
    for e in graph.edges():
        if (e[0] in tree.nodes() or e[1] in tree.nodes()):
            edges.append(e)
    
    valid_edges = []
    for v in edges:
        if not((v[0] in tree.nodes()) and (v[1] in tree.nodes())):
            valid_edges.append(v)
    
    return valid_edges

def min_possible_prims_edge(graph, tree):
    possible_e = valid_incident_edges(graph, tree)
    min_e = possible_e[0]
    for e in possible_e:
        if cost(graph, e) < cost(graph, min_e):
            min_e = e
    return min_e


