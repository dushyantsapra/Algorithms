'''
Created on Aug 14, 2016

@author: Dushyant sapra
'''

from org.ds.graph.DisjointSet import DisjointSet
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
        return "Edge With Name : " + self.name + " And Weight : " + str(self.weight);
#         return "Edge With Starting Vertex : " + self.fromVertex.getName() + ", End Vertex : " + self.toVertex.getName() + ", Name : " + self.name + " And Weight : " + str(self.weight);
    
    def getFromVertex(self):
        return self.fromVertex;

    def getToVertex(self):
        return self.toVertex;
    
    def getName(self):
        return self.name;

    def getWeight(self):
        return self.weight;

class Graph:
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

        if edge in self.edgeMap:
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
            
    def bfs(self, vertexName):
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
                queue.enQueue(tempVertex);
    
    def dfsUsingStack(self, vertexName):
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
                stack.push(tempVertex);

    def defUsingRecursionHelper(self, vertex, visitedVertexList):
        print(vertex.getName());
        visitedVertexList.append(vertex);
        
        for v in vertex.getOutVerticesList():
            if v in visitedVertexList:
                continue;
            
            self.dfsUsingRecursionHelper(v, visitedVertexList);

    def dfsUsingRecursion(self, vertexName):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;
        
        vertex = self.vertexMap[vertexName];
        self.dfsUsingRecursionHelper(vertex, []);

    def dfsUsingStackForConnectedComponent(self, vertexName, visitedVertexMap, counterValue):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;

        vertex = self.vertexMap[vertexName];

        stack = StackUsingLinkedList();
        visitedVertexList = [];

        stack.push(vertex);
        visitedVertexList.append(vertex);
        visitedVertexMap[vertex] = counterValue;

        while stack.getSize() > 0:
            v = stack.pop();
            print(v.getName());

            for tempVertex in v.getAdjacentVertex():
                if tempVertex in visitedVertexList:
                    continue;

                visitedVertexList.append(tempVertex);
                visitedVertexMap[tempVertex] = counterValue;
                stack.push(tempVertex);

    def bfsForConnectedComponent(self, vertexName, visitedVertexMap, counterValue):
        vertex = self.getVertexWithName(vertexName);

        queue = Queue();
        visitedVertexList = [];

        queue.enQueue(vertex);
        visitedVertexList.append(vertex);
        visitedVertexMap[vertex] = counterValue;

        while queue.getSize() > 0:
            v = queue.deQueue();
            print(v.getName());

            for tempVertex in v.getAdjacentVertex():
                if tempVertex in visitedVertexList:
                    continue;

                visitedVertexList.append(tempVertex);
                visitedVertexMap[tempVertex] = counterValue;
                queue.enQueue(tempVertex);

    def countAndPrintconnectedComponents(self):
        visitedVertexMap = {};
        counter = 0;
        for key, value in self.vertexMap.iteritems():
            visitedVertexMap[value] = 0;

        for key, value in visitedVertexMap.iteritems():
            if value == 0:
                counter += 1;
                print("Connected Component Number " + str(counter) + " Vertices are:");
                self.dfsUsingStackForConnectedComponent(key.getName(), visitedVertexMap, counter);
            else:
                continue;

        print("Total Connected Components are : %d", counter);
        
    def checkForCycleInGraph(self):
        disjoinSet = DisjointSet();
        for key in self.vertexMap.iterkeys():
            disjoinSet.makeSet(key);

        for value in self.edgeMap.itervalues():
            fromParentNode = disjoinSet.findSet(value.getFromVertex().getName());
            toParentNode = disjoinSet.findSet(value.getToVertex().getName());
            
            if fromParentNode is toParentNode:
                print("Graph Contains A Cycle");
                return False;
        
            disjoinSet.union(value.getFromVertex().getName(), value.getToVertex().getName());

        print("Graph Doesn't have a Cycle");
        return False;

if __name__ == '__main__': 

    """# Test Case 1
    g = Graph();
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
    
    print("\n*****BFS*****");Graph
    g.bfs("V1");
    
    print("\n*****DFS Using Stack*****");
    g.dfsUsingStack("V2");
    
    print("\n*****DFS Using Recursion*****");
    g.dfsUsingStack("V2");"""
    
    
    """# Test Case 2, Checking For Connected Component's in a graph
    g = Graph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
    g.addVertex("V8");
    g.addVertex("V9");
    g.addVertex("V10");
    g.addVertex("V11");
    g.addVertex("V12");
    g.addVertex("V13");
    g.addVertex("V14");
    
    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V5", "E2");
    g.addEdge("V2", "V3", "E3");
    g.addEdge("V3", "V4", "E4");
    g.addEdge("V4", "V5", "E5");
    
    g.addEdge("V6", "V7", "E6");
    g.addEdge("V6", "V8", "E7");
    g.addEdge("V7", "V8", "E8");
    
    g.addEdge("V9", "V10", "E9");
    g.addEdge("V9", "V12", "E10");
    g.addEdge("V10", "V11", "E11");
    g.addEdge("V11", "V12", "E12");
    
    g.countAndPrintconnectedComponents();"""
    
    g = Graph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    
    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V4", "E2");
    
    g.addEdge("V2", "V5", "E3");
    # g.addEdge("V2", "V3", "E4");
    
    g.addEdge("V3", "V6", "E5");
    
    g.addEdge("V5", "V6", "E6");
    
    g.checkForCycleInGraph();
