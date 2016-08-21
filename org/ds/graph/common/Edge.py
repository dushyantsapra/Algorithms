'''
Created on Aug 21, 2016

@author: Dushyant Sapra
'''

class Edge:
    def __init__(self, fromVertex, toVertex, name=None, weight=0):
        self.fromVertex = fromVertex;
        self.toVertex = toVertex;
        self.name = name;
        self.weight = weight;
        
    def __gt__(self, other):
        return self.weight > other.weight;
    
    def __ge__(self, other):
        return self.weight >= other.weight;

    def __lt__(self, other):
        return self.weight < other.weight;
    
    def __le__(self, other):
        return self.weight <= other.weight;

    def __eq__(self, other):
        return (self.fromVertex == other.getFromVertex()) and (self.toVertex == other.getToVertex());

    def __str__(self):
        return "Edge With Starting Vertex : " + self.fromVertex.getName() + ", End Vertex : " + self.toVertex.getName() + ", Name : " + self.name + " And Weight : " + str(self.weight);
#         return "Edge With Name : " + self.name + " And Weight : " + str(self.weight);
    
    def getFromVertex(self):
        return self.fromVertex;

    def getToVertex(self):
        return self.toVertex;
    
    def getName(self):
        return self.name;

    def getWeight(self):
        return self.weight;