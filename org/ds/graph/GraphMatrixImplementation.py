'''
Created on Sep 4, 2016

@author: Dushyant Sapra
'''

class GraphMatrixImplementation:
    def __init__(self, vertexCount):
        self.matrix = [[0 for x in range(vertexCount)] for y in range(vertexCount)];
    
    def getGraphMatrix(self):
        return self.matrix;
    
    def addEdge(self, sIndex, eIndex):
        self.matrix[sIndex][eIndex] = 1;