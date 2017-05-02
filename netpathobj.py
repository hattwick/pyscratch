# Simple graph theory to check for network isolation and survivability scenarios
# Copied and modified from Berd Klein at Bodenseo

# This is the object approach

class Graph(object):

    def __init__(self, graph_dict=None):
        """ Initialize graph object."""
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

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

    def add_edge(self, edge):
        """Add edge between two vertices. Edge is of type set, tuple or list"""
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """Generate all edges of the graph.  Edges require 1 or 2 vertices."""
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

if __name__ == "__main__":
    sites = {"HQ": ["DC1", "DC2"],
             "BackOffice": ["DC1", "DC2"],
             "DC1": ["HQ", "BackOffice", "DC2", "Colo1", "Colo2", "Colo3"],
             "DC2": ["HQ", "BackOffice", "DC1", "Colo1", "Colo2", "Colo3"],
             "Colo1": ["DC2", "Colo3"],
             "Colo2": ["DC1"],
             "Colo3": ["Colo1"],
             "Colo4": []
             }

    graph = Graph(sites)
    print("Vertices:")
    print(graph.vertices())

    graph = Graph(sites)


