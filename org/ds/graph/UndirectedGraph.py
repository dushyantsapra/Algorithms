'''
Created on Aug 14, 2016

@author: Dushyant sapra
'''

from org.ds.graph.common.Edge import Edge
from org.ds.queue.Queue import Queue
from org.ds.stack.Stack import StackUsingLinkedList


class Vertex:
    def __init__(self, name):
        self.name = name;
        self.edgeList = [];
        self.adjacentVertex = [];
        
    def __eq__(self, other):
        return self.name is other.name;

    def __hash__(self):
        return hash(self.name);

    def __str__(self):
        return "Vertex Name is " + self.name;

    def setAdjacentVertexAndEdge(self, edge, vertex):
        self.edgeList.append(edge);
        self.adjacentVertex.append(vertex);

    def removeEdge(self, edge):
        return self.edgeList.remove(edge);

    def removeVertex(self, vertex):
        return self.adjacentVertex.remove(vertex);
    
    def getEdgeList(self):
        return self.edgeList;

    def getAdjacentVertex(self):
        return self.adjacentVertex;
    
    def getName(self):
        return self.name;
    
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
                    value.getFromVertex().removeEdge(value);
                    value.getToVertex().removeEdge(value);

                    value.getFromVertex().removeVertex(vertex);
                    value.getToVertex().removeVertex(vertex);
                    del self.edgeMap[key];

            del self.vertexMap[vertexName];
        else:
            print("Vertex Doesn't Exists");
            
    """def bfs(self, vertexName):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;

        vertex = self.vertexMap[vertexName];

        queue = Queue();
        visitedVertexList = [];

        queue.enQueue(vertex);
        visitedVertexList.append(vertex);

        while queue.getSize() > 0:
            v = queue.deQueue();
            print(v.getName());

            for tempVertex in v.getAdjacentVertex():
                if tempVertex in visitedVertexList:
                    continue;

                visitedVertexList.append(tempVertex);
                queue.enQueue(tempVertex);"""
        
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
            
    """def dfsUsingStack(self, vertexName):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;

        vertex = self.vertexMap[vertexName];

        stack = StackUsingLinkedList();
        visitedVertexList = [];

        stack.push(vertex);
        visitedVertexList.append(vertex);

        while stack.getSize() > 0:
            v = stack.pop();
            print(v.getName());

            for tempVertex in v.getAdjacentVertex():
                if tempVertex in visitedVertexList:
                    continue;

                visitedVertexList.append(tempVertex);
                stack.push(tempVertex);"""
            
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

    """def defUsingRecursionHelper(self, vertex, visitedVertexList):
        print(vertex.getName());
        visitedVertexList.append(vertex);

        for v in vertex.getAdjacentVertex():
            if v in visitedVertexList:
                continue;

            self.defUsingRecursionHelper(v, visitedVertexList);"""

    def defUsingRecursionHelper(self, vertex, arrivalMap, departureMap, visitedVertexMap=None, currentCount=0):
#         print(vertex.getName());
        if visitedVertexMap is None:
            visitedVertexMap = {};

        visitedVertexMap[vertex] = 1;
        currentCount += 1;
        arrivalMap[vertex] = currentCount;

        print("Vertex Name: " + vertex.getName() + ", Arrival Time: " + str(currentCount));

        for tempVertex in vertex.getAdjacentVertex():
            if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                continue;

            currentCount = self.defUsingRecursionHelper(tempVertex, arrivalMap, departureMap, visitedVertexMap, currentCount);
        currentCount += 1;
        departureMap[vertex] = currentCount;
        print("Vertex Name: " + vertex.getName() + ", Departure Time: " + str(currentCount));
        return currentCount;

    def dfsUsingRecursion(self, vertexName):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;

        vertex = self.vertexMap[vertexName];

        arrivalMap = {};
        departureMap = {};
#         self.defUsingRecursionHelper(vertex, []);
        self.defUsingRecursionHelper(vertex, arrivalMap, departureMap, {});

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
    
    g.addEdge("V2", "V4", "E3");
    g.addEdge("V2", "V5", "E4");
    g.addEdge("V2", "V3", "E5");
    
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
