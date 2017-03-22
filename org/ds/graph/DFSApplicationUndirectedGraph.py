'''
Created on Aug 23, 2016

@author: Dushyant Sapra
'''
from org.ds.graph.DisjointSet import DisjointSet
from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.graph.common.DFSApplicationUtil import DFSApplicationUtil


class DFSApplicationUndirectedGraph:
#     Application: Check If G(V, E) are 2 Edge connected
#     Logic:
#     Check for every Bridge Edge in the graph, If graph has a bridge edge then G is not 2 edge connected
#     To check for bridge edge, find the deepest back edge from every vertex, While doing so make sure no tree edge's are included
    def checkIfGraphIs2EdgeConnected(self, graph):
        vertex = list(graph.vertexMap.values())[0];

        arrivalMap = {};
        departureMap = {};
        bridgeEdgeMap = {};
        DFSApplicationUtil.checkIfGraphIs2EdgeConnectedHelper(False, vertex, vertex, arrivalMap, departureMap, bridgeEdgeMap, {});
        
        if len(bridgeEdgeMap) == 0:
            print("\nGraph is 2 Edge Connected");
        else:
            print("\nGraph is not 2 Edge Connected");
            print("Bridge Edges are");
            for key, value in bridgeEdgeMap.items():
                print("From Vertex : " + key.getName() + ", To Vertex : " + value.getName());

#     Assuming Graph is Connected with no connected components. If (V, E) has connected component then check for every vertex which are not visited in single run 
    def checkForArticulationPointInGraph(self, graph, isPrint=True):
        visitedVertexMap = {};

        for v in graph.getVertexMap().values():
            visitedVertexMap[v] = False;

        cutVertexList = [];
        vertex = list(graph.getVertexMap().values())[0];
        
        for vertex in graph.getVertexMap().values():
            if not visitedVertexMap[vertex]:
                DFSApplicationUtil.checkForArticulationPointInGraphHelper(vertex, vertex, {}, {}, cutVertexList, visitedVertexMap);
        
        if isPrint:
            if len(cutVertexList) == 0:
                print("\nNo Articulation Point(Cut Vertex) Exists in Graph");
            else:
                print("\nGraph Contains Articulation Point(Cut Vertex)");
                print("Articulation Point(Cut Vertex) are");
                for vertex in cutVertexList:
                    print(vertex);
        return cutVertexList;
    
    def checkForCycleInUnDirectedGraphUsingDFS(self, graph):
        visitedVertexMap = {};
        isCyclic = False;
        for v in graph.getVertexMap().values():
            visitedVertexMap[v] = 0;
            
        for key in visitedVertexMap.keys():
            if visitedVertexMap[key] == 0:
                isCyclic = DFSApplicationUtil.checkForCycleInGraphUsingDFSHelper(key, key, visitedVertexMap);
                if isCyclic:
                    print("Graph Contains Cycle");
                else:
                    print("Graph is ACyclic");

    def checkForCycleInGraphUsingDisjointSet(self, graph):
        ds = DisjointSet();
        
        for vertex in graph.getVertexMap().values():
            ds.makeSet(vertex);
        
        isCyclePresent = False;
        for edge in graph.getEdgeMap().values():
            if not ds.union(edge.getFromVertex(), edge.getToVertex()):
                isCyclePresent = True;
                break;

        if isCyclePresent:
            print("Graph contains Cycle(Using Disjoint Set's)");
        else:
            print("Graph Doesn't contains Cycle(Using Disjoint Set's)");
    
    def checkForCycleInGraphUsingVertexColor(self, graph):
        visitedVertexColorMap = {};
        
        for vertex in graph.getVertexMap().values():
            visitedVertexColorMap[vertex] = "WHITE";
        
        isCyclePresent = False;
        for vertex in visitedVertexColorMap.keys():
            if visitedVertexColorMap[vertex] is 'WHITE':
                print("\n");
                isCyclePresent = DFSApplicationUtil.checkForCycleInGraphUsingVertexColorHelper(vertex, vertex, visitedVertexColorMap);
                if isCyclePresent:
                    break;
        
        if isCyclePresent:
            print("Graph contains Cycle(Using Vertex Color)");
        else:
            print("Graph Doesn't contains Cycle(Using Vertex Color)");

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
            print("Graph is Not Connected");

    
    def hamiltonianPathOrCircuitHelper(self, graph, startVertex, vertex, visitedVertexMap, hamiltonPath):
        visitedVertexMap[vertex] = True;

        hamiltonPath.append(vertex);

        for v in vertex.getAdjacentVertex():
            if v in visitedVertexMap and visitedVertexMap[v]:
                if startVertex == v and len(visitedVertexMap) == len(graph.getVertexMap()):
                    hamiltonPath.append(v);
                    return True;
                continue;
            else:
                return self.hamiltonianPathOrCircuitHelper(graph, startVertex, v, visitedVertexMap, hamiltonPath);

        return False;

    def hamiltonianPathOrCircuit(self, graph):
        visitedVertexMap = {};

        vertex = list(graph.getVertexMap().values())[0];

        hamiltonPath = []

        isHamilton = self.hamiltonianPathOrCircuitHelper(graph, vertex, vertex, visitedVertexMap, hamiltonPath);

        if isHamilton:
            print("Given Graph contain's Hamiltion Cycle");
            print("Hamiltion Path is : ");
            for v in hamiltonPath:
                print(v);
        else:
            print("Graph is Not Hamiltion");


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
    
    g.addEdge("V4", "V5", "E6");
    
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
#     obj.checkForArticulationPointInGraph(g);
    
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


    g = UnDirectedGraph();
    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");

    g.addEdge("V0", "V1", "E1");
    g.addEdge("V0", "V2", "E2");
    g.addEdge("V0", "V3", "E3");

    g.addEdge("V1", "V2", "E4");

    g.addEdge("V3", "V4", "E5");

    obj = DFSApplicationUndirectedGraph();
    obj.checkForCycleInGraphUsingDisjointSet(g);
    obj.checkForCycleInGraphUsingVertexColor(g);

#     g = UnDirectedGraph();
#     g.addVertex("V0");
#     g.addVertex("V1");
#     g.addVertex("V2");
#     
#     g.addEdge("V0", "V1", "E1");
#     g.addEdge("V1", "V2", "E2");
#     g.addEdge("V2", "V3", "E3");

    g = UnDirectedGraph();
    g.addVertex("V0");
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

    g.addEdge("V0", "V1", "E1");
    g.addEdge("V0", "V6", "E2");

    g.addEdge("V1", "V2", "E3");
    g.addEdge("V1", "V3", "E4");
    g.addEdge("V1", "V5", "E5");

    g.addEdge("V2", "V4", "E6");

    g.addEdge("V3", "V4", "E7");

    g.addEdge("V5", "V6", "E8");
    g.addEdge("V5", "V7", "E9");
    g.addEdge("V5", "V8", "E10");

    g.addEdge("V7", "V8", "E11");

    g.addEdge("V8", "V9", "E12");

    g.addEdge("V10", "V11", "E13");

    print("padpasdpadsp");
    obj = DFSApplicationUndirectedGraph();
    obj.checkForArticulationPointInGraph(g);
    
    
    g = UnDirectedGraph();
 
    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
     
    g.addEdge("V0", "V1", "E1");
    g.addEdge("V0", "V3", "E2");
     
    g.addEdge("V1", "V2", "E3");
    g.addEdge("V1", "V3", "E4");
    g.addEdge("V1", "V4", "E5");
     
    g.addEdge("V2", "V4", "E6");
     
    g.addEdge("V3", "V4", "E7");

    obj = DFSApplicationUndirectedGraph();
    obj.hamiltonianPathOrCircuit(g);