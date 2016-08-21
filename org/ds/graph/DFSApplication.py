'''
Created on Aug 17, 2016

@author: Dushyant Sapra
'''
from org.ds.graph.common.Edge import Edge
from org.ds.graph.UndirectedGraph import UnDirectedGraph


class DFSApplication:
# Applications for Directed Graph
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
        visitedVertexList.append(vertex);

        for v in vertex.getOutVerticesList():
            if v in visitedVertexList:
                continue;

            self.dfsUsingRecursionHelper(v, visitedVertexList);

    def topologicalSortUsingDFS(self, directedGraph):
        zeroInEdgeVertexList = [];
        topologicalSortedVertexList = [];

        vertexInEdgeListMap = {};

        for vertex in directedGraph.vertexMap.itervalues():
            vertexInEdgeListMap[vertex] = vertex.getInEdgeList();
            if len(vertex.getInEdgeList()) == 0:
                zeroInEdgeVertexList.append(vertex);

        self.dfsUsingRecursionHelper(vertex, []);

    def checkIfGraphStronglyConnected(self):
        print();

    def checkForCycleInGraph(self):
        print();

# Applications for UnDirected Graph

#     Application: Check If G(V, E) are 2 Edge connected
#     Logic:
#     Check for every Bridge Edge in the graph, If graph has a bridge edge then G is not 2 edge connected
#     To check for bridge edge, find the deepest back edge from every vertex, While doing so make sure no tree edge's are included
    
    def checkIfGraphIs2EdgeConnectedHelper(self, parentVertex, vertex, arrivalMap, departureMap, bridgeEdgeMap, visitedVertexMap=None, currentCount=0):
        if visitedVertexMap is None:
            visitedVertexMap = {};

        visitedVertexMap[vertex] = 1;
        currentCount += 1;
        arrivalMap[vertex] = currentCount;

        minArrivalTime = currentCount;

#         print("Vertex Name: " + vertex.getName() + ", Arrival Time: " + str(currentCount));

        for tempVertex in vertex.getAdjacentVertex():
            if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                if tempVertex is not parentVertex:
                    minArrivalTime = arrivalMap[tempVertex] if arrivalMap[tempVertex] < minArrivalTime else minArrivalTime;
                continue;

            currentCount, tempMinArrivalTime = self.checkIfGraphIs2EdgeConnectedHelper(vertex, tempVertex, arrivalMap, departureMap, bridgeEdgeMap, visitedVertexMap, currentCount);
            minArrivalTime = tempMinArrivalTime if tempMinArrivalTime < minArrivalTime else minArrivalTime;
        currentCount += 1;
        departureMap[vertex] = currentCount;
#         print("Vertex Name: " + vertex.getName() + ", Departure Time: " + str(currentCount));
        
#         Condition: arrivalMap[vertex] != 1, TO Check it the processed vertex is not a start Vertex
        if minArrivalTime >= arrivalMap[vertex] and arrivalMap[vertex] != 1:
            bridgeEdgeMap[parentVertex] = vertex;
        return currentCount, minArrivalTime;
    
    def checkIfGraphIs2EdgeConnected(self, graph):
        vertex = graph.vertexMap.values()[0];

        arrivalMap = {};
        departureMap = {};
        bridgeEdgeMap = {};
        self.checkIfGraphIs2EdgeConnectedHelper(vertex, vertex, arrivalMap, departureMap, bridgeEdgeMap, {});
        
        if len(bridgeEdgeMap) == 0:
            print("\nGraph is 2 Edge Connected");
        else:
            print("\nGraph is not 2 Edge Connected");
            print("Bridge Edges are");
            for key, value in bridgeEdgeMap.iteritems():
                print("From Vertex : " + key.getName() + ", To Vertex : " + value.getName());

if __name__ == '__main__':
# #     Test Case 1
#     g = Graph();
#     g.addVertex("V1");
#     g.addVertex("V2");
#     g.addVertex("V3");
#     g.addVertex("V4");
#     g.addVertex("V5");
#     g.addVertex("V6");
#     g.addVertex("V7");
# 
#     g.addEdge("V1", "V2", "E1");
#     g.addEdge("V1", "V3", "E2");
#     g.addEdge("V1", "V4", "E3");
# 
#     g.addEdge("V2", "V5", "E4");
# 
#     g.addEdge("V5", "V6", "E5");
#     g.addEdge("V3", "V6", "E6");
#     g.addEdge("V4", "V6", "E7");
# 
#     g.addEdge("V6", "V7", "E8");
#     
#     obj = DFSApplication();
#     obj.topologicalSortUsingKhanAlgo(g);

    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    
    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V3", "E2");

    g.addEdge("V2", "V3", "E3");
    g.addEdge("V2", "V4", "E4");

    obj = DFSApplication();
    obj.checkIfGraphIs2EdgeConnected(g);
