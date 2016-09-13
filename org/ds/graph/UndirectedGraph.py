'''
Created on Aug 14, 2016

@author: Dushyant sapra
'''

from org.ds.graph.common.Edge import Edge
from org.ds.graph.common.Vertex import Vertex
from org.ds.queue.Queue import Queue
from org.ds.stack.Stack import StackUsingLinkedList

class UnDirectedGraph:
    def __init__(self):
        self.vertexMap = {};
        self.edgeMap = {};
        
    def getVertexMap(self):
        return self.vertexMap;
    
    def getEdgeMap(self):
        return self.edgeMap;
        
    def addVertex(self, vertexName):
        if vertexName in self.vertexMap:
            print("Vertex Already Exists");
            return False;
        else:
            vertex = Vertex(vertexName);
            self.vertexMap[vertexName] = vertex;
            return True;
    
    def addEdge(self, fromVertexName, toVertexName, name=None, weight=0):
        fromVertex = None;
        toVertex = None;
        if fromVertexName not in self.vertexMap:
            fromVertex = Vertex(fromVertexName);
            self.vertexMap[fromVertexName] = fromVertex;
        else:
            fromVertex = self.vertexMap[fromVertexName];

        if toVertexName not in self.vertexMap:
            toVertex = Vertex(toVertexName);
            self.vertexMap[toVertexName] = toVertex;
        else:
            toVertex = self.vertexMap[toVertexName];

        edge = Edge(fromVertex, toVertex, name, weight);

        if name in self.edgeMap:
            print("Edge from start Vertex \"" + fromVertexName + "\" & end Vertex \"" + toVertexName + "\" is Present"); 
            return False;

        self.edgeMap[name] = edge;
        fromVertex.setAdjacentVertexAndEdge(edge, toVertex);
        toVertex.setAdjacentVertexAndEdge(edge, fromVertex);

    def removeVertex(self, vertexName):
        if vertexName in self.vertexMap:
            vertex = self.vertexMap[vertexName];
            for key, value in self.edgeMap.iteritems()[:]:
                if value.getFromVertex() == vertex or value.getToVertex() == vertex:
                    value.getFromVertex().removeUndirectedEdge(value);
                    value.getToVertex().removeUndirectedEdge(value);

                    value.getFromVertex().removeVertex(vertex);
                    value.getToVertex().removeVertex(vertex);
                    del self.edgeMap[key];

            del self.vertexMap[vertexName];
        else:
            print("Vertex Doesn't Exists");

    def bfs(self, vertexName, visitedVertexMap=None):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;

        vertex = self.vertexMap[vertexName];
    
        if visitedVertexMap is None:
            visitedVertexMap = {};

        queue = Queue();

        queue.enQueue(vertex);
        visitedVertexMap[vertex] = 1;

        while queue.getSize() > 0:
            v = queue.deQueue();
            print(v.getName());

            for tempVertex in v.getAdjacentVertex():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                    continue;

                visitedVertexMap[tempVertex] = 1;
                queue.enQueue(tempVertex);
            
    def dfsUsingStack(self, vertexName, visitedVertexMap=None):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;

        vertex = self.vertexMap[vertexName];
    
        if visitedVertexMap is None:
            visitedVertexMap = {};

        stack = StackUsingLinkedList();

        stack.push(vertex);
        visitedVertexMap[vertex] = 1;

        while stack.getSize() > 0:
            v = stack.pop();
            print(v.getName());

            for tempVertex in v.getAdjacentVertex():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                    continue;

                visitedVertexMap[tempVertex] = 1;
                stack.push(tempVertex);

    def dfsUsingRecursionHelper(self, vertex, arrivalMap, departureMap, isPrint=True, visitedVertexMap=None, currentCount=0):
        if visitedVertexMap is None:
            visitedVertexMap = {};

        visitedVertexMap[vertex] = 1;
        currentCount += 1;
        arrivalMap[vertex] = currentCount;

        if isPrint:
            print("Vertex Name: " + vertex.getName() + ", Arrival Time: " + str(currentCount));

        for tempVertex in vertex.getAdjacentVertex():
            if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                continue;

            currentCount = self.dfsUsingRecursionHelper(tempVertex, arrivalMap, departureMap, isPrint, visitedVertexMap, currentCount);
        currentCount += 1;
        departureMap[vertex] = currentCount;
        if isPrint:
            print("Vertex Name: " + vertex.getName() + ", Departure Time: " + str(currentCount));
        return currentCount;

    def dfsUsingRecursion(self, vertexName, isPrint=True):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;

        vertex = self.vertexMap[vertexName];

        arrivalMap = {};
        departureMap = {};
        visitedVertexMap = {};
        self.dfsUsingRecursionHelper(vertex, arrivalMap, departureMap, isPrint, visitedVertexMap);
        return visitedVertexMap;

    def printAllDFSHelper(self, vertex, destinationVertex, visitedVertexMap, pathList):
        visitedVertexMap[vertex] = True;
        pathList.append(vertex);

        if vertex == destinationVertex:
            print("Path");
            for vertex in pathList:
                print(vertex);
        else:
            for tempVertex in vertex.getAdjacentVertex():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex]:
                    continue;
                self.printAllDFSHelper(tempVertex, destinationVertex, visitedVertexMap, pathList);
        visitedVertexMap[vertex] = False;
        pathList.pop();

    def printAllDFS(self, sourceVertexName, destinationVertexName):
        visitedVertexMap = {};

        for vertex in self.vertexMap.values():
            visitedVertexMap[vertex] = False;

        sourceVertex = self.vertexMap[sourceVertexName];
        destinationVertex = self.vertexMap[destinationVertexName];
        pathList = [];

        self.printAllDFSHelper(sourceVertex, destinationVertex, visitedVertexMap, pathList);

if __name__ == '__main__': 
    # Test Case 1
    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    
    g.addEdge("V1", "V3", "E1");
    g.addEdge("V1", "V4", "E2");
    
    g.addEdge("V2", "V3", "E5");
    g.addEdge("V2", "V4", "E3");
    g.addEdge("V2", "V5", "E4");
    
    g.addEdge("V3", "V5", "E6");
    
    g.addEdge("V4", "V5", "E7");
    g.addEdge("V4", "V6", "E8");
    
    g.addEdge("V5", "V6", "E9");
    
    print("\n*****BFS*****");
    g.bfs("V1");
    
    print("\n*****DFS Using Stack*****");
    g.dfsUsingStack("V2");
    
    print("\n*****DFS Using Recursion*****");
    g.dfsUsingRecursion("V2");
    
    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
    g.addVertex("V8");
    g.addVertex("V9");

    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V3", "E2");
    
    g.addEdge("V2", "V3", "E3");

    g.addEdge("V3", "V4", "E4");
    
    g.addEdge("V4", "V5", "E5");
    g.addEdge("V4", "V6", "E6");
    
    g.addEdge("V5", "V6", "E7");
    
    g.addEdge("V6", "V7", "E8");
    
    g.addEdge("V7", "V8", "E9");
    g.addEdge("V7", "V9", "E10");
    
    g.addEdge("V8", "V9", "E11");
    
    g.printAllDFS("V1", "V9");
