'''
Created on Aug 17, 2016

@author: Dushyant Sapra
'''

from org.ds.graph.DirectedGraph import DirectedGraph
from org.ds.graph.GraphMatrixImplementation import GraphMatrixImplementation
from org.ds.graph.common.DFSApplicationUtil import DFSApplicationUtil
from org.ds.stack.Stack import StackUsingLinkedList

class DFSApplicationDirectedGraph:
    def checkIfGraphStronglyConnected(self, graph):
        visitedVertexMap = graph.dfsUsingRecursion(list(graph.getVertexMap().keys())[0], False, False);

        if len(visitedVertexMap) != len(graph.getVertexMap()):
            print("Graph is Not Strongly Connected");
            return

        visitedVertexMap = graph.dfsUsingRecursion(list(graph.getVertexMap().keys())[0], True, False);

        if len(visitedVertexMap) == len(graph.getVertexMap()):
            print("Graph is Strongly Connected");
        else:
            print("Graph is Not Strongly Connected");

    def checkIfGraphStronglyConnectedUsing2EdgeConnectivity(self, graph):
        vertex = list(graph.vertexMap.values())[0];

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
        vertex = list(graph.getVertexMap().values())[0];

        if(DFSApplicationUtil.checkForCycleInDirectedGraphHelper(vertex, stack, visitedVertexMap)):
            print("Directed Graph has a Cycle");
        else:
            print("Directed Graph is ACyclic");  

    def transitiveClosureOfGraphUsingDFSHelper(self, parentIndex, index, graph, visitedVertexList, transitiveClosureMatrix):
        visitedVertexList[index] = True;
        transitiveClosureMatrix[parentIndex][index] = 1;
        for iLoop in range(graph.getVertexCount()):
            if graph.getGraphMatrix()[index][iLoop] == 1 and not visitedVertexList[iLoop]:
                self.transitiveClosureOfGraphUsingDFSHelper(parentIndex, iLoop, graph, visitedVertexList, transitiveClosureMatrix);

#     Given a directed graph, find out if a vertex v is reachable from another vertex u for all vertex pairs (u, v) in the given graph. Here reachable mean that there is a path from vertex u to v. The reach-ability matrix is called transitive closure of a graph.
    def transitiveClosureOfGraphUsingDFS(self, graph):
        transitiveClosureMatrix = [[0 for jLoop in range(graph.getVertexCount())] for iLoop in range(graph.getVertexCount())];

        for iLoop in range(graph.getVertexCount()):
            visitedVertexList = [False] * (graph.getVertexCount());
            self.transitiveClosureOfGraphUsingDFSHelper(iLoop, iLoop, graph, visitedVertexList, transitiveClosureMatrix);

        for iLoop in range(graph.getVertexCount()):
            fromVertex = graph.getIndexVertexMap()[iLoop];
            for jLoop in range(graph.getVertexCount()):
                subString = "Available" if transitiveClosureMatrix[iLoop][jLoop] else "Not Available";
                print("Path From Vertex " + fromVertex + " To Vertex " + graph.getIndexVertexMap()[jLoop] + " is : " + subString);
            print("\n");

if __name__ == '__main__':
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
    
    g = GraphMatrixImplementation(4);
    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    
    g.addEdge("V0", "V1");
    g.addEdge("V0", "V2");
    
    g.addEdge("V1", "V2");
    
    g.addEdge("V2", "V0");
    g.addEdge("V2", "V3");
    
    g.addEdge("V3", "V3");
    
    obj = DFSApplicationDirectedGraph();
    print("\n");
    obj.transitiveClosureOfGraphUsingDFS(g);
