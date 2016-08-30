'''
Created on Aug 17, 2016

@author: Dushyant Sapra
'''
from org.ds.graph.DirectedGraph import DirectedGraph
from org.ds.graph.common.Edge import Edge
from org.ds.graph.common.DFSApplicationUtil import DFSApplicationUtil
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
            for v in topologicalSortedVertexList:
                print(v);
        else:
            print("Graph is not a Directed Acyclic Graph");

    def topologicalSortUsingDFSHelper(self, vertex, visitedVertexList):
        print(vertex.getName());

    def topologicalSortUsingDFS(self, directedGraph):
        print()

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

if __name__ == '__main__':
#     Test Case 1(Directed Graph), Topological Sort Using Khan's Algo
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
    g.addEdge("V1", "V4", "E3");
 
    g.addEdge("V2", "V5", "E4");
 
    g.addEdge("V5", "V6", "E5");
    g.addEdge("V3", "V6", "E6");
    g.addEdge("V4", "V6", "E7");

    g.addEdge("V6", "V7", "E8");

    obj = DFSApplicationDirectedGraph();
    obj.topologicalSortUsingKhanAlgo(g);

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