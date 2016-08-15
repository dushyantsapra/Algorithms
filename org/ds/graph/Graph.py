'''
Created on Jul 29, 2016
@author: Dushyant Sapra
'''


"""
A Graph is G = (V, E)

Graph can be of two Type
    i) Directed
    ii) UnDirected

Each Vertex has Status of one of the following:
    i) UnDiscovered(White): Initial State, the vertex is not visited yet.
    ii) Discovered(Gray): Vertex is visited but not all its incident edges i.e have some white adjacent vertices
    iii) Processed(Black): After discovering the vertex, we have visited ALL its incident edges as well

There are 3 way's of implementing Graph
    i) Edge List
    ii) Adjacency List
    iii) Adjacency Matrix

Here Implementation is Combination of First 2.
"""

from org.ds.graph.DisjointSet import DisjointSet


from org.ds.queue.Queue import Queue;
from org.ds.stack.Stack import StackUsingLinkedList;

class Vertex:
    def __init__(self, name):
        self.outEdges = [];
        self.inEdges = [];
        self.outVertices = [];
        self.inVertices = [];
        self.name = name;
        
    def __hash__(self):
        return hash(self.name);

    def __eq__(self, other):
        return self.name is other.name;

    def __str__(self):
        print("Vertex Name is " + self.name);

    def getName(self):
        return self.name;

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
            print(len(self.outVertices));
            self.outVertices.remove(edge.getToVertex());
            print(len(self.outVertices));

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

class Edge:
    def __init__(self, fromVertex, toVertex, name=None, weight=0):
        self.fromVertex = fromVertex;
        self.toVertex = toVertex;
        self.weight = weight;
        self.name = name;

    def __eq__(self, other):
        return (self.fromVertex == other.getFromVertex()) and (self.toVertex == other.getToVertex());

    def getFromVertex(self):
        return self.fromVertex;

    def getToVertex(self):
        return self.toVertex;

    def getWeight(self):
        return self.weight;

    def getName(self):
        return self.name;

class GraphDirected:
    def __init__(self):
        self.vertexList = [];
        self.edgeList = [];
        
    def addVertex(self, name):
        vertex = Vertex(name);
        if vertex in self.vertexList:
            print("Given Vertex \"" + name + "\" Already Exists");
            return False;
        
        self.vertexList.append(vertex);
    
    def getVertexWithName(self, name):
        for v in self.vertexList:
            if v.getName() is name:
                return v;
        return None;
        
    def addEdge(self, fromVertexName, toVertexName, name=None, weight=0):
        fromVertex = self.getVertexWithName(fromVertexName);
        toVertex = self.getVertexWithName(toVertexName);

        if fromVertex is None:
            print("From Vertex \"" + fromVertexName + "\" is Absent");
            return False;

        if toVertex is None:
            print("To Vertex \"" + toVertex + "\" is Absent");
            return False;

        edge = Edge(fromVertex, toVertex, name, weight);

        if edge in self.edgeList:
            print("Edge from start Vertex \"" + fromVertexName + "\" & end Vertex \"" + toVertexName + "\" is Present"); 
            return False;

        fromVertex.addEdge(edge);
        toVertex.addEdge(edge);
        self.edgeList.append(edge);

    def listVertex(self):
        for vertex in self.vertexList:
            print("Vertex Name is " + vertex.name);

    def listVertexWithInAndOutEdges(self):
        for vertex in self.vertexList:
            vertex.listOutEdges();
            vertex.listInEdges();

    def getNumberOfEdges(self):
        print("Number of Edges is " + len(self.edgeList));
        return len(self.edgeList);

    def isEdgeListEmpty(self):
        if len(self.edgeList) == 0:
            return True;
        else:
            return False;

    def getNumberOfVertices(self):
        print("Number of Vertices are " + len(self.vertexList));
        return len(self.vertexList);

    def listEdges(self):
        for edge in self.edgeList:
            print("Edge Having Start Vertex " + edge.getFromVertex().name + " & End Vertex " + edge.getToVertex().name);

    def removeEdge(self, fromVertexName, toVertexName):
        fromVertex = self.getVertexWithName(fromVertexName);
        toVertex = self.getVertexWithName(toVertexName);

        isRemoved = False;

        edge = Edge(fromVertex, toVertex);

        for e in self.edgeList:
            if edge == e:
                fromVertex.removeEdge(edge);
                toVertex.removeEdge(edge);
                self.edgeList.remove(e);
                isRemoved = True;

        if isRemoved:
            print("Edge From Vertex \"" + fromVertexName + "\" To Vertex " + toVertexName + "\" Has been Removed");
        else:
            print("No Edge Exists From Vertex \"" + fromVertexName + "\" To Vertex \"" + toVertexName + "\"");

    def removeVertex(self, vertexName):
        vertex = Vertex(vertexName);
        if vertex in self.vertexList:
            for e in self.edgeList[:]:
                if e.getFromVertex() == vertex or e.getToVertex() == vertex:
                    e.getFromVertex().removeOutEdge(e);
                    e.getToVertex().removeInEdge(e);
                    self.edgeList.remove(e);

            self.vertexList.remove(vertex);
        else:
            print("Vertex With Name " + vertexName + " Not Present");

#     Print all out Edges From a Vertex
    def listAdjacentVertics(self, vertexName):
        vertex = self.getVertexWithName(vertexName);

        if vertex:
            if len(vertex.getOutEdgeList()) > 0:
                for e in vertex.getOutEdgeList():
                    print(e.getToVertex().getName());
            else:
                print("No Adjacent Vertex from Given Vertex \"" + vertexName + "\"");
        else:
            print("Vertex With Given Name \"" + vertexName + " \" is Absent ");

class GraphUnDirected:
    def __init__(self):
        self.vertexList = [];
        self.edgeList = [];

    def addVertex(self, name):
        vertex = Vertex(name);
        if vertex in self.vertexList:
            print("Given Vertex \"" + name + "\" Already Exists");
            return False;

        self.vertexList.append(vertex);

    def getVertexWithName(self, name):
        for v in self.vertexList:
            if v.getName() is name:
                return v;
        return None;

    def addEdge(self, fromVertexName, toVertexName, name=None, weight=0):
        fromVertex = self.getVertexWithName(fromVertexName);
        toVertex = self.getVertexWithName(toVertexName);

        if fromVertex is None:
            print("From Vertex \"" + fromVertexName + "\" is Absent");
            return False;

        if toVertex is None:
            print("To Vertex \"" + toVertex + "\" is Absent");
            return False;

        fromEdge = Edge(fromVertex, toVertex, name, weight);
        toEdge = Edge(toVertex, fromVertex, name, weight);

        if fromEdge in self.edgeList:
            print("Edge from start Vertex \"" + fromVertexName + "\" & end Vertex \"" + toVertexName + "\" is Present"); 
            return False;

        if toEdge in self.edgeList:
            print("Edge from start Vertex \"" + toVertexName + "\" & end Vertex \"" + fromVertexName + "\" is Present"); 
            return False;

        fromVertex.addEdge(fromEdge);
        toVertex.addEdge(fromEdge);
        self.edgeList.append(fromEdge);

        fromVertex.addEdge(toEdge);
        toVertex.addEdge(toEdge);
        self.edgeList.append(toEdge);

    def listVertex(self):
        for vertex in self.vertexList:
            print("Vertex Name is " + vertex.name);

    def listVertexWithInAndOutEdges(self):
        for vertex in self.vertexList:
            vertex.listOutEdges();
            vertex.listInEdges();
        
    def listVertexWithInAndOutVertices(self):
        for vertex in self.vertexList:
            vertex.listOutVertices();
            vertex.listInVertices();

    def getNumberOfEdges(self):
        print("Number of Edges is " + len(self.edgeList));
        return len(self.edgeList);

    def isEdgeListEmpty(self):
        if len(self.edgeList) == 0:
            return True;
        else:
            return False;

    def getNumberOfVertices(self):
        print("Number of Vertices are " + len(self.vertexList));
        return len(self.vertexList);

    def listEdges(self):
        for edge in self.edgeList:
            print("Edge Having Start Vertex " + edge.getFromVertex().name + " & End Vertex " + edge.getToVertex().name);

    def removeEdge(self, fromVertexName, toVertexName):
        fromVertex = self.getVertexWithName(fromVertexName);
        toVertex = self.getVertexWithName(toVertexName);

        if fromVertex is None:
            print("From Vertex \"" + fromVertexName + "\" is Absent");
            return False;

        if toVertex is None:
            print("To Vertex \"" + toVertexName + "\" is Absent");
            return False;

        isFromRemoved = False;
        isToRemoved = False;

        fromEdge = Edge(fromVertex, toVertex);
        toEdge = Edge(toVertex, fromVertex);
        
        if fromEdge in self.edgeList:
            fromVertex.removeEdge(fromEdge);
            toVertex.removeEdge(fromEdge);
            self.edgeList.remove(fromEdge);
            isFromRemoved = True;
            
        if toEdge in self.edgeList:
            fromVertex.removeEdge(toEdge);
            toVertex.removeEdge(toEdge);
            self.edgeList.remove(toEdge);
            isToRemoved = True;
    
        if isFromRemoved and isToRemoved:
            print("Edge From Vertex \"" + fromVertexName + "\" To Vertex " + toVertexName + "\" Has been Removed");
            print("Edge From Vertex \"" + toVertexName + "\" To Vertex " + fromVertexName + "\" Has been Removed");
        else:
            print("No Edge Exists From Vertex \"" + fromVertexName + "\" To Vertex \"" + toVertexName + "\"");

    def removeVertex(self, vertexName):
        vertex = Vertex(vertexName);
        if vertex in self.vertexList:
            for e in self.edgeList[:]:
                if e.getFromVertex() == vertex or e.getToVertex() == vertex:
                    e.getFromVertex().removeOutEdge(e);
                    e.getToVertex().removeInEdge(e);
                    self.edgeList.remove(e);

            self.vertexList.remove(vertex);
        else:
            print("Vertex With Name " + vertexName + " Not Present");

#     Print all out Edges From a Vertex
    def listAdjacentVertics(self, vertexName):
        vertex = self.getVertexWithName(vertexName);

        if vertex:
            if len(vertex.getOutEdgeList()) > 0:
                for e in vertex.getOutEdgeList():
                    print(e.getToVertex().getName());
            else:
                print("No Adjacent Vertex from Given Vertex \"" + vertexName + "\"");
        else:
            print("Vertex With Given Name \"" + vertexName + " \" is Absent ");
        
    def bfs(self, vertexName):
        vertex = self.getVertexWithName(vertexName);

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
        vertex = self.getVertexWithName(vertexName);
        
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

    def defUsingRecursionHelper(self, vertex, visitedVertexList):
        print(vertex.getName());
        visitedVertexList.append(vertex);
        
        for v in vertex.getOutVerticesList():
            if v in visitedVertexList:
                continue;
            
            self.dfsUsingRecursionHelper(v, visitedVertexList);

    def dfsUsingRecursion(self, vertexName):
        vertex = self.getVertexWithName(vertexName);
        
        self.dfsUsingRecursionHelper(vertex, []);
    
    def dfsUsingStackForConnectedComponent(self, vertexName, visitedVertexMap, counterValue):
        vertex = self.getVertexWithName(vertexName);
        
        stack = StackUsingLinkedList();
        visitedVertexList = [];
        
        stack.push(vertex);
        visitedVertexList.append(vertex);
        visitedVertexMap[vertex] = counterValue;
        
        while stack.getSize() > 0:
            v = stack.pop();
            print(v.getName());

            for tempVertex in v.getOutVerticesList():
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

            for tempVertex in v.getOutVerticesList():
                if tempVertex in visitedVertexList:
                    continue;

                visitedVertexList.append(tempVertex);
                visitedVertexMap[tempVertex] = counterValue;
                queue.enQueue(tempVertex);

    def countAndPrintconnectedComponents(self):
        visitedVertexMap = {};
        counter = 0;
        for v in self.vertexList:
            visitedVertexMap[v] = 0;

        for key, value in visitedVertexMap.iteritems():
            if value == 0:
                counter += 1;
                print("Connected Component Number " + str(counter) + " Vertices are:");
                self.dfsUsingStackForConnectedComponent(key.getName(), visitedVertexMap, counter);
            else:
                continue;

        print("Total Connected Components are : %d", counter);
    
#     1. If in BFS we find an edge, both of whose end points are in same level then that Graph is not is bipartite
#     2. If G has a odd Cycle(Means Cycle having odd nbr. of edges) then G is not bipartite
#     If a Graph is not fully connected that is we have more then one connected component, then we have to check the above property for
#     every component. If a single component is not bipartite then the graph is not bipartite
    def checkIfGraphIsBipartite(self):
        print();
        
    def checkForCycle(self):
        disJointSet = DisjointSet();

        for v in self.vertexList:
            disJointSet.makeSet(v.getName());

        for e in self.edgeList:
            sParentNode = disJointSet.findSet(e.getFromVertex().getName());
            eParentNode = disJointSet.findSet(e.getToVertex().getName());
            
            if sParentNode is eParentNode:
                print("There is a Cycle in Given Graph");
                return;
        
        print("Graph has no Cycle");

if __name__ == '__main__':
    """
    # Test Case 1
    g = GraphDirected();
    g.addVertex("NDLS");
    g.addVertex("REW");
    g.addVertex("GGN");
    
    g.listVertex();
    
    g.addEdge("NDLS", "GGN");
    g.addEdge("GGN", "REW");
    g.addEdge("NDLS", "REW");
    
    print(len(g.edgeList));
    
    g.removeEdge("GGN", "REW");
    g.listEdges();
    
    print(len(g.edgeList));"""
    
    
    """# Test Case 2
    g = GraphDirected();
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
    g = GraphUnDirected();
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
    g = GraphUnDirected();
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
    
    # Test Case 5
    g = GraphUnDirected();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    
    # g.addEdge(fromVertexName, toVertexName, name, weight);
