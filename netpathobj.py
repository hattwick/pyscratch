# Simple graph theory to check for network isolation and survivability scenarios
# Copied and modified from Berd Klein at Bodenseo

# This is the object approach

class Graph(object):

    def __init__(self, graph_dict=None):
    """ Initialize graph object.
    """

    if graph_dict == None:
        graph_dict = {}
    self.graph_dict = graph_dict

    def vertices(self):
        """Return the vertices of the graph"""
        return list(self.__graph_dict.keys())

    def edges(self):
        """Return the edges of the graph"""
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """Add key vertex to self.__graph_dict with an empty list if vertex not there"""
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

