# Implementation of some classes needed for  a Graph Class

class Node(object):
    def __init__(self, name):
        """ Assumes name is a string """
        self.name = name
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """ Assumes src,dest are nodes """
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getDestination()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)          # Take advantage of inherited constructor
        self.weight = weight
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return self.src.getName() + '-> (' + str(self.weight) + ')' + self.dest.getName()


# Build out a functional Digraph and Graph Class using classes from GraphObjects.py
# For this simple implemntation we make a Digraph wiht adjancency lists as opposed to a matrx


class Digraph(object):
    # nodes is a list of nodes in the graph
    # edges is a dict mapping each node to its children

    def __init__(self):
        self.nodes = []
        self.edges = {}
    
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate node")

        else:
            self.nodes.append(node)
            self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()

        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")

        self.edges[src].append(dest)
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.nodes
    
    def getNode(self, name):                # use this getter to easily refer to Nodes
        for n in self.edges:
            if n.getName() == name:
                return n
        
        raise NameError(name)

    def __str__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result += src.getName() + '->' + dest.getName()
        return result

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)



