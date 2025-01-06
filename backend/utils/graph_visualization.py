import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph):
    """
    Visualize the knowledge graph using matplotlib.
    
    Parameters:
    - graph: NetworkX graph object.
    """
    pos = nx.spring_layout(graph)
    labels = nx.get_node_attributes(graph, 'label')
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_labels(graph, pos, labels=labels)
    plt.show()