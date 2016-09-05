'''
Created on Aug 17, 2016

@author: Dushyant Sapra
'''

from org.ds.graph.DirectedGraph import DirectedGraph
from org.ds.graph.common.DFSApplicationUtil import DFSApplicationUtil
from org.ds.graph.common.Edge import Edge
from org.ds.stack.Stack import StackUsingLinkedList


class DFSApplicationDirectedGraph:
#     Logic:
    def topologicalSortUsingKhanAlgo(self, directedGraph):
        zeroInEdgeVertexList = [];
        topologicalSortedVertexList = [];

        vertexInEdgeListMap = {};

        for vertex in directedGraph.vertexMap.itervalues():
            vertexInEdgeListMap[vertex] = vertex.getInEdgeList();
            if len(vertex.getInEdgeList()) == 0:
                zeroInEdgeVertexList.append(vertex);

        while len(zeroInEdgeVertexList) > 0:
            vertex = zeroInEdgeVertexList.pop(0);
            topologicalSortedVertexList.append(vertex);
            for outVertex in vertex.getOutVerticesList():
                edge = Edge(vertex, outVertex);
                vertexInEdgeListMap[outVertex].remove(edge);
                if len(vertexInEdgeListMap[outVertex]) == 0:
                    zeroInEdgeVertexList.append(outVertex);

        isTrue = True;
        for lt in vertexInEdgeListMap.itervalues():
            if len(lt) > 0:
                isTrue = False;
                break;

        if isTrue:
            print("Topological Sort Using khan's Algo is : ");
            for v in topologicalSortedVertexList:
                print(v);
        else:
            print("Graph is not a Directed Acyclic Graph");

    def topologicalSortUsingDFSHelper(self, vertex, visitedVertexMap, stack):
        visitedVertexMap[vertex] = True;

        for tempVertex in vertex.getOutVerticesList():
            if visitedVertexMap[tempVertex]:
                continue;

            self.topologicalSortUsingDFSHelper(tempVertex, visitedVertexMap, stack);

        stack.push(vertex);

    def topologicalSortUsingDFS(self, graph, isPrint=True):
        visitedVertexMap = {};
        stack = StackUsingLinkedList();

        for vertex in graph.getVertexMap().values():
            visitedVertexMap[vertex] = False;

        for vertex, value in visitedVertexMap.iteritems():
            if not value:
                self.topologicalSortUsingDFSHelper(vertex, visitedVertexMap, stack); 

        if isPrint:
            print("Topological Sort Using DFS is : ");
            while stack.getSize() > 0:
                print(stack.pop());
        else:
            return stack;

    def checkIfGraphStronglyConnected(self, graph):
        visitedVertexMap = graph.dfsUsingRecursion(graph.getVertexMap().keys()[0], False, False);

        if len(visitedVertexMap) != len(graph.getVertexMap()):
            print("Graph is Not Strongly Connected");
            return

        visitedVertexMap = graph.dfsUsingRecursion(graph.getVertexMap().keys()[0], True, False);

        if len(visitedVertexMap) == len(graph.getVertexMap()):
            print("Graph is Strongly Connected");
        else:
            print("Graph is Not Strongly Connected");

    def checkIfGraphStronglyConnectedUsing2EdgeConnectivity(self, graph):
        vertex = graph.vertexMap.values()[0];

        arrivalMap = {};
        departureMap = {};
        bridgeEdgeMap = {};
        DFSApplicationUtil.checkIfGraphIs2EdgeConnectedHelper(True, vertex, vertex, arrivalMap, departureMap, bridgeEdgeMap, {});

        if len(bridgeEdgeMap) == 0:
            print("\nDirected Graph is Strongly Connected");
        else:
            print("\nDirected Graph is not Strongly Connected");

#     Logic: Maintain a Stack of Visited Vertices, 
#             Detected a Back Edge, To detect a back edge, we can keep track of vertices currently in recursion stack of function for DFS traversal. 
#             If we reach a vertex that is already in the recursion stack, then there is a cycle in the tree
    def checkForCycleInDirectedGraph(self, graph):
        visitedVertexMap = {};
        stack = StackUsingLinkedList();
        for v in graph.getVertexMap().values():
            visitedVertexMap[v] = 0;
        vertex = graph.getVertexMap().values()[0];

        if(DFSApplicationUtil.checkForCycleInDirectedGraphHelper(vertex, stack, visitedVertexMap)):
            print("Directed Graph has a Cycle");
        else:
            print("Directed Graph is ACyclic");

    def printStronglyConnectedCommponentUsingKosarajusAlgo(self, graph):
        connectedComponentCount = 0;

        visitedVertexMap = {};
        for vertex in graph.vertexMap.values():
            visitedVertexMap[vertex] = False;

        stack = StackUsingLinkedList();

        for vertex in graph.getVertexMap().values():
            if not visitedVertexMap[vertex]:
                DFSApplicationUtil.stronglyConnectedCommponentUsingKosarajusAlgoHelper(vertex, visitedVertexMap, False, stack);

        sccVertexMap = {};
        visitedVertexMap = {};
        for vertex in graph.vertexMap.values():
            visitedVertexMap[vertex] = False;

        while stack.getSize() > 0:
            vertex = stack.pop();
            if not visitedVertexMap[vertex]:
                tempStack = StackUsingLinkedList();
                DFSApplicationUtil.stronglyConnectedCommponentUsingKosarajusAlgoHelper(vertex, visitedVertexMap, True, tempStack);
                tempStack.push(vertex);
                sccVertexMap[vertex] = tempStack;
                connectedComponentCount += 1;

        print("\nTotal Strongly Connected Components are : " + str(connectedComponentCount));
        iLoop = 1;
        for key in sccVertexMap.keys():
            stack = sccVertexMap[key];
            print("Strongly Connected Component Number : " + str(iLoop) + ", Vertices are : ");
            while stack.getSize() > 0:
                print(stack.pop());
            print("\n");

    def iterativeDeepeningDFS(self, graph):
        print()

if __name__ == '__main__':
#     Test Case 1(Directed Graph), Topological Sort Using Khan's Algo
    g = DirectedGraph();
    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
 
    g.addEdge("V2", "V3", "E1");
    
    g.addEdge("V3", "V1", "E2");
    
    g.addEdge("V4", "V0", "E3");
    g.addEdge("V4", "V1", "E4");
 
    g.addEdge("V5", "V0", "E5");
    g.addEdge("V5", "V2", "E6");
 
    obj = DFSApplicationDirectedGraph();
    obj.topologicalSortUsingKhanAlgo(g);
    obj.topologicalSortUsingDFS(g);

#     Test Case 2(Directed Graph), Check if Given Graph is Strongly Connected
    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    
    g.addEdge("V1", "V2", "E1");
    
    g.addEdge("V2", "V3", "E2");
    
    g.addEdge("V3", "V4", "E3");
    g.addEdge("V3", "V5", "E4");
    
    g.addEdge("V4", "V1", "E5");
    
    g.addEdge("V5", "V3", "E6");
    obj = DFSApplicationDirectedGraph();
    obj.checkIfGraphStronglyConnectedUsing2EdgeConnectivity(g);
    obj.checkIfGraphStronglyConnected(g);

#     Test Case 3(Directed Graph), Check If Graph Has a cycle
    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");

    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V4", "E2");

    g.addEdge("V2", "V4", "E3");

    g.addEdge("V3", "V3", "E6");

    g.addEdge("V4", "V1", "E5");
    g.addEdge("V4", "V3", "E4");

    obj = DFSApplicationDirectedGraph();
    print("\n");
    obj.checkForCycleInDirectedGraph(g);

#     Test Case 4, Count and Print Strongly Connected Component using Kousraju Algo
    g = DirectedGraph();
    g.addVertex("A");
    g.addVertex("B");
    g.addVertex("C");
    g.addVertex("D");
    g.addVertex("E");
    g.addVertex("F");
    g.addVertex("G");
    g.addVertex("H");
    g.addVertex("I");
    g.addVertex("J");
    g.addVertex("K");

    g.addEdge("A", "B", "E1");
    
    g.addEdge("B", "C", "E2");
    g.addEdge("B", "D", "E3");
    
    g.addEdge("C", "A", "E4");
    
    g.addEdge("D", "E", "E5");
    
    g.addEdge("E", "F", "E6");
    
    g.addEdge("F", "D", "E7");
    
    g.addEdge("G", "F", "E8");
    g.addEdge("G", "H", "E9");
    
    g.addEdge("H", "I", "E10");
    
    g.addEdge("I", "J", "E11");
    
    g.addEdge("J", "G", "E12");
    g.addEdge("J", "K", "E13");
    
    obj = DFSApplicationDirectedGraph();
    print("\n");
    obj.printStronglyConnectedCommponentUsingKosarajusAlgo(g);
    
    
    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
