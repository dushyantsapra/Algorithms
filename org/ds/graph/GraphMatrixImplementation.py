'''
Created on Sep 4, 2016

@author: Dushyant Sapra
'''

class GraphMatrixImplementation:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount;
        self.vertexIndexMap = {};
        self.indexVertexMap = {};
        self.matrix = [[0 for y in range(vertexCount)] for x in range(vertexCount)];
        self.weightMatrix = [[float("inf") for y in range(vertexCount)] for x in range(vertexCount)];

    def getVertexCount(self):
        return self.vertexCount;

    def getVertexIndexMap(self):
        return self.vertexIndexMap;

    def getIndexVertexMap(self):
        return self.indexVertexMap;

    def getGraphMatrix(self):
        return self.matrix;

    def addVertex(self, vertexName):
        if vertexName in self.vertexIndexMap:
            print("Vertex with Given Name already Exists");
            return False;
        
        if len(self.vertexIndexMap) < self.vertexCount:
            self.vertexIndexMap[vertexName] = len(self.vertexIndexMap);
            self.indexVertexMap[len(self.vertexIndexMap) - 1] = vertexName;
        else:
            print("No New Vertex can be added");
            return False;

    def addEdge(self, fromVertexName, toVertexName, weight=0):
        if fromVertexName not in self.vertexIndexMap:
            print("From Vertex doesn't Exists")
            return False;
#             self.vertexIndexMap[fromVertexName] = len(self.vertexIndexMap);

        if toVertexName not in self.vertexIndexMap:
            print("To Vertex doesn't Exists")
            return False;
#             self.vertexIndexMap[toVertexName] = len(self.vertexIndexMap);

        self.matrix[self.vertexIndexMap[fromVertexName]][self.vertexIndexMap[toVertexName]] = 1;
        self.weightMatrix[self.vertexIndexMap[fromVertexName]][self.vertexIndexMap[toVertexName]] = weight;

    def dfsUsingRecursionHelper(self, index, visitedVertexMatrix):
        print(self.indexVertexMap[index]);

        visitedVertexMatrix[index] = True;

        for iLoop in range(self.vertexCount):
            if self.matrix[index][iLoop] == 1 and not visitedVertexMatrix[iLoop]:
                self.dfsUsingRecursionHelper(iLoop, visitedVertexMatrix);

    def dfsUsingRecursion(self):
        visitedVertexMatrix = [False] * (self.vertexCount);

        self.dfsUsingRecursionHelper(self.vertexIndexMap.values()[1], visitedVertexMatrix);

if __name__ == '__main__':
    g = GraphMatrixImplementation(6);
    
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");

    g.addEdge("V1", "V2", 4);
    g.addEdge("V1", "V6", 10);
    
    g.addEdge("V2", "V3", 2);
    
    g.addEdge("V3", "V4", 3);
    
    g.addEdge("V4", "V5", 8);
    
    g.addEdge("V5", "V1", 1);
    
    g.addEdge("V6", "V3", 5);
    g.addEdge("V6", "V5", 12);
    
    """g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    
    g.addEdge("V0", "V1", 3);
    g.addEdge("V0", "V2", 6);
    g.addEdge("V0", "V3", 15);
    
    g.addEdge("V1", "V2", -2);
    
    g.addEdge("V2", "V3", 2);
    
    g.addEdge("V3", "V0", 1);"""
    
    g.dfsUsingRecursion();
