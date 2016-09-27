'''
Created on Sep 4, 2016

@author: Dushyant Sapra
'''

from org.ds.queue.Queue import Queue

class GraphMatrixImplementation:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount;
        self.vertexIndexMap = {};
        self.indexVertexMap = {};
        self.matrix = [[0 for y in range(vertexCount)] for x in range(vertexCount)];
#         self.weightMatrix = [[float("inf") for y in range(vertexCount)] for x in range(vertexCount)];
        self.weightMatrix = [[0 for y in range(vertexCount)] for x in range(vertexCount)];

    def getVertexCount(self):
        return self.vertexCount;

    def getVertexIndexMap(self):
        return self.vertexIndexMap;

    def getIndexVertexMap(self):
        return self.indexVertexMap;

    def getGraphMatrix(self):
        return self.matrix;

    def getGraphWeightMatrix(self):
        return self.weightMatrix;

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

    def dfsUsingRecursionHelper(self, index, visitedVertexList):
        print(self.indexVertexMap[index]);

        visitedVertexList[index] = True;

        for iLoop in range(self.vertexCount):
            if self.matrix[index][iLoop] == 1 and not visitedVertexList[iLoop]:
                self.dfsUsingRecursionHelper(iLoop, visitedVertexList);

    def dfsUsingRecursion(self, sourceVertexName=None):
        visitedVertexList = [False] * (self.vertexCount);

        if sourceVertexName:
            sourceVertexIndex = self.vertexIndexMap[sourceVertexName];
        else:
            self.vertexIndexMap.values()[1]

        self.dfsUsingRecursionHelper(sourceVertexIndex, visitedVertexList);

        return visitedVertexList;

    def bfsHelper(self, vertexIndex, visitedVertexIndexMap):
        queue = Queue();

        visitedVertexIndexMap[vertexIndex] = True;

        queue.enQueue(vertexIndex);

        while queue.getSize() > 0:
            iVertex = queue.deQueue();

            print("Vertex : " + str(iVertex));
            for jVertex in range(self.vertexCount):
                if self.matrix[iVertex][jVertex] == 1 and not visitedVertexIndexMap[jVertex]:
                    queue.enQueue(jVertex);
                    visitedVertexIndexMap[jVertex] = True;

    def bfs(self):
        visitedVertexIndexMap = {};

        for vertexIndex in self.vertexIndexMap.itervalues():
            visitedVertexIndexMap[vertexIndex] = False; 

        print("BFS");
        for iIndex in self.vertexIndexMap.itervalues():
            if not visitedVertexIndexMap[iIndex]:
                self.bfsHelper(iIndex, visitedVertexIndexMap);

if __name__ == '__main__':
    g = GraphMatrixImplementation(6);

    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");

    g.addEdge("V0", "V1", 4);
    g.addEdge("V0", "V5", 10);

    g.addEdge("V1", "V2", 2);

    g.addEdge("V2", "V3", 3);

    g.addEdge("V3", "V4", 8);

    g.addEdge("V4", "V0", 1);

    g.addEdge("V5", "V2", 5);
    g.addEdge("V5", "V4", 12);

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
    
#     g.dfsUsingRecursion();
    g.bfs();
