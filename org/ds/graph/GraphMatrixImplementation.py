'''
Created on Sep 4, 2016

@author: Dushyant Sapra
'''

class GraphMatrixImplementation:
    def __init__(self, vertexCount):
        self.matrix = [[0 for y in range(vertexCount)] for x in range(vertexCount)];
        self.weightMatrix = [[float("inf") for y in range(vertexCount)] for x in range(vertexCount)];

    def getGraphMatrix(self):
        return self.matrix;
    
    def addEdge(self, sIndex, eIndex, weight):
        self.matrix[sIndex][eIndex] = 1;
        self.weightMatrix[sIndex][eIndex] = weight;