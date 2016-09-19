'''
Created on Jul 29, 2016
@author: Dushyant Sapra
'''

from org.ds.graph.common.Edge import Edge
from org.ds.graph.common.Vertex import Vertex


from org.ds.queue.Queue import Queue;
from org.ds.stack.Stack import StackUsingLinkedList;

class DirectedGraph:
    def __init__(self):
        self.vertexMap = {};
        self.edgeMap = {};

    def getVertexMap(self):
        return self.vertexMap;
    
    def getEdgeMap(self):
        return self.edgeMap;

    def addVertex(self, vertexName):
        if vertexName in self.vertexMap:
            print("Given Vertex \"" + vertexName + "\" Already Exists");
            return False;

        vertex = Vertex(vertexName);
        self.vertexMap[vertexName] = vertex;

    def addEdge(self, fromVertexName, toVertexName, edgeName, weight=0):
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

        edge = Edge(fromVertex, toVertex, edgeName, weight);

        if edge in self.edgeMap.itervalues():
            print("Edge from start Vertex \"" + fromVertexName + "\" & end Vertex \"" + toVertexName + "\" is Present"); 
            return False;

        fromVertex.addEdge(edge);
        toVertex.addEdge(edge);
        self.edgeMap[edgeName] = edge;

    def listVertex(self):
        for vertex in self.vertexMap.itervalues():
            print("Vertex Name is " + vertex.name);

    def listVertexWithInAndOutEdges(self):
        for vertex in self.vertexMap.itervalues():
            vertex.listOutEdges();
            vertex.listInEdges();

    def getNumberOfEdges(self):
        print("Number of Edges is " + len(self.edgeMap));
        return len(self.edgeMap);

    def isEdgeListEmpty(self):
        if len(self.edgeMap) == 0:
            return True;
        else:
            return False;

    def getNumberOfVertices(self):
        print("Number of Vertices are " + len(self.vertexMap));
        return len(self.vertexMap);

    def listEdges(self):
        for edge in self.edgeMap.itervalues():
            print("Edge Having Start Vertex " + edge.getFromVertex().name + " & End Vertex " + edge.getToVertex().name);

    def removeEdge(self, fromVertexName, toVertexName):
        if fromVertexName not in self.vertexMap:
            print("From Vertex \"" + fromVertexName + "\" is Absent");
            return False;
        
        if toVertexName not in self.vertexMap:
            print("To Vertex \"" + toVertexName + "\" is Absent");
            return False;
        
        fromVertex = self.vertexMap[fromVertexName];
        toVertex = self.vertexMap[toVertexName];

        isRemoved = False;

        edge = Edge(fromVertex, toVertex);

        for e in self.edgeMap.values():
            if edge == e:
                fromVertex.removeEdge(edge);
                toVertex.removeEdge(edge);
                del self.edgeMap[e.getName()];
                isRemoved = True;

        if isRemoved:
            print("Edge From Vertex \"" + fromVertexName + "\" To Vertex " + toVertexName + "\" Has been Removed");
        else:
            print("No Edge Exists From Vertex \"" + fromVertexName + "\" To Vertex \"" + toVertexName + "\"");

    def removeVertex(self, vertexName):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;
        vertex = self.vertexMap[vertexName];

        if vertex in self.vertexMap.itervalues():
            for e in self.edgeMap.itervalues()[:]:
                if e.getFromVertex() == vertex or e.getToVertex() == vertex:
                    e.getFromVertex().removeOutEdge(e);
                    e.getToVertex().removeInEdge(e);
                    del self.edgeMap[e.getName()];

            self.vertexList.remove(vertex);
            del self.vertexMap[vertex.getName()];

#     Print all out Edges From a Vertex
    def listAdjacentVertics(self, vertexName):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;
 
        vertex = self.vertexMap[vertexName];
        if len(vertex.getOutEdgeList()) > 0:
            for e in vertex.getOutEdgeList():
                print(e.getToVertex().getName());
        else:
            print("No Adjacent Vertex from Given Vertex \"" + vertexName + "\"");

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

            for tempVertex in v.getOutVerticesList():
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

            for tempVertex in v.getOutVerticesList():
                if tempVertex in visitedVertexList:
                    continue;

                visitedVertexList.append(tempVertex);
                stack.push(tempVertex);

    """def dfsUsingRecursionHelper(self, vertex, visitedVertexList):
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
        self.dfsUsingRecursionHelper(vertex, []);"""
        
    
    def dfsUsingRecursionHelper(self, vertex, arrivalMap, departureMap, isReverse=False, isPrint=True, visitedVertexMap=None, currentCount=0):
        if visitedVertexMap is None:
            visitedVertexMap = {};

        visitedVertexMap[vertex] = 1;
        currentCount += 1;
        arrivalMap[vertex] = currentCount;

        if isPrint:
            print("Vertex Name: " + vertex.getName() + ", Arrival Time: " + str(currentCount));

        if isReverse:
            for tempVertex in vertex.getInVerticesList():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                    continue;
                
                currentCount = self.dfsUsingRecursionHelper(tempVertex, arrivalMap, departureMap, isReverse, isPrint, visitedVertexMap, currentCount);
        else:
            for tempVertex in vertex.getOutVerticesList():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                    continue;
                
                currentCount = self.dfsUsingRecursionHelper(tempVertex, arrivalMap, departureMap, isReverse, isPrint, visitedVertexMap, currentCount);
        currentCount += 1;
        departureMap[vertex] = currentCount;
        if isPrint:
            print("Vertex Name: " + vertex.getName() + ", Departure Time: " + str(currentCount));
        return currentCount;

    def dfsUsingRecursion(self, vertexName, isReverse=False, isPrint=True):
        if vertexName not in self.vertexMap:
            print("Vertex Doesn't Exists");
            return False;

        vertex = self.vertexMap[vertexName];

        arrivalMap = {};
        departureMap = {};
        visitedVertexMap = {};
        self.dfsUsingRecursionHelper(vertex, arrivalMap, departureMap, isReverse, isPrint, visitedVertexMap);
        return visitedVertexMap;
    
    def printAllDFSHelper(self, vertex, destinationVertex, visitedVertexMap, pathList):
        visitedVertexMap[vertex] = True;
        pathList.append(vertex);

        if vertex == destinationVertex:
            print("Path");
            for vertex in pathList:
                print(vertex);
        else:
            for tempVertex in vertex.getOutVerticesList():
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
    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");

    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V5", "E2");
    
    g.addEdge("V2", "V3", "E3");
    
    g.addEdge("V3", "V4", "E4");
    
    g.addEdge("V4", "V5", "E5");
    
    g.addEdge("V5", "V1", "E6");
    
    g.addEdge("V6", "V3", "E7");
    g.addEdge("V6", "V5", "E8");

    g.dfsUsingRecursion("V1");
    
    g.dfsUsingStack("V1");

    """# Test Case 2
    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    # g.addVertex("V4");
    # g.addVertex("V5");
    # g.addVertex("V6");
    
    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V3", "E2");
    # g.addEdge("V2", "V6", "E3");
    # g.addEdge("V3", "V1", "E4");
    # g.addEdge("V4", "V5", "E5");
    
    g.removeEdge("V1", "V2");
    
    print("Edge Lists \n");
    g.listEdges();
    
    # print("Vertex List\n");
    # g.listVertexWithInAndOutEdges();
    
    g.listAdjacentVertics("V2");
    
    g.removeVertex("V1");
    print("\n");
    
    print("Vertex List\n");
    g.listVertexWithInAndOutEdges();"""
    
    
    """# Test Case 3
    g = DirectedGraph();
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
    
    
    # print("\n");
    # g.removeVertex("V2");
    # print("Edge Lists \n");
    # g.listEdges();
    
    # print("Edge Lists \n");
    # g.listEdges();
    
    print("\n*****BFS*****");
    g.bfs("V2");
    
    print("\n*****DFS Using Stack*****");
    g.dfsUsingStack("V2");
    
    print("\n*****DFS Using Recursion*****");
    g.dfsUsingStack("V2");"""
    
    
    """# Test Case 4, Checking For Connected Component's in a graph
    g = DirectedGraph();
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

    g = DirectedGraph();
    
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
    
    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V3", "E2");
    
    g.addEdge("V2", "V3", "E3");

    g.addEdge("V3", "V4", "E4");
    g.addEdge("V3", "V6", "E5");

    g.addEdge("V4", "V5", "E6");

    g.addEdge("V6", "V7", "E7");
    
    g.addEdge("V7", "V4", "E8");

    print("\n");
    g.printAllDFS("V1", "V5");
