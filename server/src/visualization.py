""" Visualize the ontology graph."""
import networkx as nx
import matplotlib.pyplot as plt
from rdflib import URIRef


class StoryVisualizer:
    """ Class for visualizing the ontology graph."""
    def __init__(self, ontology):
        self.ontology = ontology
        self.graph = nx.DiGraph()

    def build_graph(self):
        """Build a graph from the ontology."""
        for s, p, o in self.ontology:
            if isinstance(o, URIRef):
                self.graph.add_edge(s, o, label=p)

    def visualize(self):
        """ Visualize the ontology graph."""
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw(self.graph, pos, with_labels=True,
                node_size=2000, node_color="skyblue")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()
