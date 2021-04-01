
class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def __len__(self):
        return len(self.graph)

# AddNode()
# Adds a new node to the graph
# Takes in the value of that node
# Returns the added node

    def add_node(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

# AddEdge()
# Adds a new edge between two nodes in the graph
# Include the ability to have a “weight”
# Takes in the two nodes to be connected by the edge
# Both nodes should already be in the Graph

    def add_edge(self, start_vertex, end_vertex, weight=1):
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start vertex does not exist in graph.')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End vertex does not exist in graph.')
        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)



# GetNodes()
# Returns all of the nodes in the graph as a collection (set, list, or similar)

    def get_node(self, value):
        if value in self._adjacency_list:
            return value
        if value not in self._adjacency_list:
            return 'Value not found'




# GetNeighbors()
# Returns a collection of edges connected to the given node
# Takes in a given node
# Include the weight of the connection in the returned collection

    def get_neighbor(self, value):
        return self._adjacency_list[value]

        

     


# Size()
# Returns the total number of nodes in the graph


    def __len__(self):
        return len(self._adjacency_list)



     


class Vertex:

    def __init__(self, value):
        self.value = value

class Edge:

    def __init__(self, vertex, weight = 1):
        self.vertex = vertex
        self.weight = weight

# Given a business trip itinerary, and an Alaska Airlines route map, is the trip possible with direct flights? If so, how much will the total trip cost be?
#    
# Write a function based on the specifications above, which takes in a graph, and an array of city names. Without utilizing any of the built-in methods available to your language, return whether the full trip is possible with direct flights, and how much it would cost.




