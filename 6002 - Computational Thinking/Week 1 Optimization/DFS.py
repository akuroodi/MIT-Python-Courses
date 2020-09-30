# Using class Graph, we look at an example of a shortest path algorithm using DFS
# DFS = Depth First Search

from GraphClass import*

def buildCityGraph(graphType):
    """ Build a map of cities as a graph 
        Input: the type of graph you want to build (Graph or Digraph)
        Output: a graph representing city connections
    """
    
    g = graphType()

    # Add cities to graph as nodes
    for name in ['Boston', 'LA', 'NYC', 'SF']:
        g.addNode(Node(name))
    
    # Define arbitrary connections to each city
    # Treat as unweighted edges for simplicity
    e1 = Edge(g.getNode('Boston'), g.getNode('SF'))
    e2 = Edge(g.getNode('Boston'), g.getNode('NYC'))
    e3 = Edge(g.getNode('SF'), g.getNode('Boston'))
    e4 = Edge(g.getNode('NYC'), g.getNode('Boston'))
    e5 = Edge(g.getNode('LA'), g.getNode('SF'))
    e6 = Edge(g.getNode('SF'), g.getNode('LA'))
    e7 = Edge(g.getNode('SF'), g.getNode('NYC'))

    # Add edges to the graph
    for edge in [e1, e2, e3, e4, e5, e6, e7]:
        g.addEdge(edge)
    
    return g

cities = buildCityGraph(Digraph)

