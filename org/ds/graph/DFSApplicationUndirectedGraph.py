'''
Created on Aug 23, 2016

@author: Dushyant Sapra
'''
from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.graph.common.DFSApplicationUtil import DFSApplicationUtil

class DFSApplicationUndirectedGraph:
#     Application: Check If G(V, E) are 2 Edge connected
#     Logic:
#     Check for every Bridge Edge in the graph, If graph has a bridge edge then G is not 2 edge connected
#     To check for bridge edge, find the deepest back edge from every vertex, While doing so make sure no tree edge's are included
    def checkIfGraphIs2EdgeConnected(self, graph):
        vertex = graph.vertexMap.values()[0];

        arrivalMap = {};
        departureMap = {};
        bridgeEdgeMap = {};
        DFSApplicationUtil.checkIfGraphIs2EdgeConnectedHelper(False, vertex, vertex, arrivalMap, departureMap, bridgeEdgeMap, {});
        
        if len(bridgeEdgeMap) == 0:
            print("\nGraph is 2 Edge Connected");
        else:
            print("\nGraph is not 2 Edge Connected");
            print("Bridge Edges are");
            for key, value in bridgeEdgeMap.iteritems():
                print("From Vertex : " + key.getName() + ", To Vertex : " + value.getName());

#     Assuming Graph is Connected with no connected components. If (V, E) has connected component then check for every vertex which are not visited in single run 
    def checkForArticulationPointInGraph(self, graph):
        visitedVertexMap = {};

        cutVertexList = [];
        vertex = graph.getVertexMap().values()[0];
        DFSApplicationUtil.checkForArticulationPointInGraphHelper(vertex, vertex, {}, {}, cutVertexList, visitedVertexMap);
        
        if len(cutVertexList) == 0:
            print("\nNo Articulation Point(Cut Vertex) Exists in Graph");
        else:
            print("\nGraph Contains Articulation Point(Cut Vertex)");
            print("Articulation Point(Cut Vertex) are");
            for vertex in cutVertexList:
                print(vertex);

    def checkForCycleInUnDirectedGraphUsingDFS(self, graph):
        visitedVertexMap = {};
        isCyclic = False;
        for v in graph.getVertexMap().values():
            visitedVertexMap[v] = 0;
            
        for key in visitedVertexMap.iterkeys():
            if visitedVertexMap[key] == 0:
                isCyclic = DFSApplicationUtil.checkForCycleInGraphUsingDFSHelper(key, key, visitedVertexMap);
                if isCyclic:
                    print("Graph Contains Cycle");
                else:
                    print("Graph is ACyclic");

#     To check for Cycle at every Vertex
    def checkForCycleInGraphUsing2EdgeConnected(self, graph):
        vertex = graph.vertexMap.values()[0];

        arrivalMap = {};
        departureMap = {};
        bridgeEdgeMap = {};
#         DFSApplicationUtil.checkIfGraphIs2EdgeConnectedHelper(vertex, vertex, arrivalMap, departureMap, bridgeEdgeMap, {});

        if len(bridgeEdgeMap) == 0:
            print("\nGraph Has A Cycle");
        else:
            print("\nGraph Doesn't Have A Cycle");

#     Logic: Do BFS From any arbitrary vertex, if DFS visits all the vertices then G(V, E) is connected
    def checkIfUnDirectedGraphIsConnected(self, graph):
        visitedVertexMap = graph.dfsUsingRecursion(graph.getVertexMap().keys()[0]);

        if len(visitedVertexMap) == len(graph.getVertexMap()):
            print("Graph is Connected");
        else:
            print("Graph is Not Connected")
            
if __name__ == '__main__':
#     Test Case 2(Undirected Graph), CHeck if Graph is 2 Edge Connected and check for Articulation Point(Cut Vertex) in Graph
    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");

    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V5", "E2");
 
    g.addEdge("V2", "V3", "E3");
    g.addEdge("V2", "V5", "E4");
     
    g.addEdge("V3", "V4", "E5");
    
#     g.addVertex("V1");
#     g.addVertex("V2");
#     g.addVertex("V3");
#     g.addVertex("V4");
#     g.addVertex("V5");
#     g.addVertex("V6");
#     g.addVertex("V7");
#     g.addEdge("V1", "V2", "E1");
#     g.addEdge("V1", "V3", "E2");
#     
#     g.addEdge("V2", "V3", "E3");
#     
#     g.addEdge("V3", "V4", "E4");
#     g.addEdge("V3", "V5", "E5");
#     g.addEdge("V3", "V7", "E6");
#     
#     g.addEdge("V5", "V6", "E7");
#     g.addEdge("V6", "V7", "E8");
    
    obj = DFSApplicationUndirectedGraph();
    obj.checkIfGraphIs2EdgeConnected(g);
    obj.checkForArticulationPointInGraph(g);

#     Test Case 3(Undirected Graph), Check If Graph is Connected
#     g = UnDirectedGraph();
#     g.addVertex("V1");
#     g.addVertex("V2");
#     g.addVertex("V3");
#     
#     g.addEdge("V1", "V2", "E1");
#     g.addEdge("V1", "V3", "E2");
# 
#     g.addEdge("V2", "V3", "E3");
#     obj = DFSApplicationUndirectedGraph();
#     obj.checkIfUnDirectedGraphIsConnected(g);
    
#     Test Case 5(Undirected Graph), Check If Graph Has a cycle
#     g = UnDirectedGraph();
#     g.addVertex("V1");
#     g.addVertex("V2");
#     g.addVertex("V3");
#     g.addVertex("V4");
#     g.addVertex("V5");
#     g.addVertex("V6");
#     
#     g.addEdge("V1", "V2", "E1");
#     g.addEdge("V1", "V5", "E2");
#     
#     g.addEdge("V2", "V3", "E3");
#     g.addEdge("V2", "V5", "E4");
#     
#     g.addEdge("V3", "V4", "E5");
#     g.addEdge("V3", "V6", "E6");
# 
#     obj = DFSApplicationUndirectedGraph();
#     obj.checkForCycleInGraphUsing2EdgeConnected(g);
#     obj.checkForCycleInUnDirectedGraphUsingDFS(g);
