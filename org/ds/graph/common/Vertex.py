'''
Created on Aug 23, 2016

@author: Dushyant Sapra
'''

class Vertex:
    def __init__(self, name):
#         For Directed Graph
        self.outEdges = [];
        self.inEdges = [];
        self.outVertices = [];
        self.inVertices = [];
#         For Undirected Graph
        self.edgeList = [];
        self.adjacentVertex = [];
#         Common
        self.name = name;

#     Common Methods Starts
    def __eq__(self, other):
        return self.name is other.name;

    def __hash__(self):
        return hash(self.name);

    def __str__(self):
        return "Vertex Name is " + self.name;
    
    def getName(self):
        return self.name;
#     Common Methods Ends

#     Method's For Directed Graph Starts
    def getOutEdgeList(self):
        return self.outEdges;

    def getInEdgeList(self):
        return self.inEdges;
    
    def getOutVerticesList(self):
        return self.outVertices;

    def getInVerticesList(self):
        return self.inVertices;

    def addEdge(self, edge):
        if edge.getFromVertex() is self:
            self.outEdges.append(edge);
            self.outVertices.append(edge.getToVertex());
        else:
            self.inEdges.append(edge);
            self.inVertices.append(edge.getFromVertex());

    def removeEdge(self, edge):
        if edge.getFromVertex() == self:
            self.removeOutEdge(edge);
        elif edge.getToVertex() == self:
            self.removeInEdge(edge);

    def removeOutEdge(self, edge):
        if edge in self.outEdges:
            self.outEdges.remove(edge);
            self.outVertices.remove(edge.getToVertex());

    def removeInEdge(self, edge):
        if edge in self.inEdges:
            self.inEdges.remove(edge);
            self.inVertices.remove(edge.getFromVertex());

    def listOutEdges(self):
        print("Out Edge From Vertex " + self.name + " are : ");
        for e in self.outEdges:
            print(e.getName());

    def listInEdges(self):
        print("In Edge From Vertex " + self.name + " are : ");
        for e in self.inEdges:
            print(e.getName());
            
    def listOutVertices(self):
        print("Out Vertices From Vertex " + self.name + " are : ");
        for v in self.outVertices:
            print(v.name);

    def listInVertices(self):
        print("In Vertices From Vertex " + self.name + " are : ");
        for v in self.inVertices:
            print(v.name);
#     Method's For Directed Graph Ends

#     Method's For UnDirected Graph Starts
    def setAdjacentVertexAndEdge(self, edge, vertex):
        self.edgeList.append(edge);
        self.adjacentVertex.append(vertex);

    def removeUndirectedEdge(self, edge):
        return self.edgeList.remove(edge);

    def removeVertex(self, vertex):
        return self.adjacentVertex.remove(vertex);
    
    def getEdgeList(self):
        return self.edgeList;

    def getAdjacentVertex(self):
        return self.adjacentVertex;
#     Method's For UnDirected Graph Ends