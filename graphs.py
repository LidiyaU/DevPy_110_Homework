pairs = [
    (1, 2),
    (2, 4),
    (3, 5),
    (2, 5),
    (7, 9),
    (9, 10),
    (8, 7),
	(11,12)
]

import networkx as nx

def graphs(pairs):
	graph = nx.from_edgelist(pairs)
	graph_list = list(nx.connected_components(graph))
	res = len(graph_list)
	return res

print(graphs(pairs))