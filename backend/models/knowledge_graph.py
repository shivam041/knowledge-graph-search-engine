import networkx as nx

def build_knowledge_graph(entities, relations):
    graph = nx.Graph()
    for entity, label in entities:
        graph.add_node(entity, label=label)
    for subj, verb, obj in relations:
        graph.add_edge(subj, obj, label=verb)
    return graph