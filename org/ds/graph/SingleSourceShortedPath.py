'''
Created on Sep 2, 2016

@author: Dushyant Sapra
'''

import copy

from org.ds.graph.DirectedGraph import DirectedGraph
from org.ds.graph.GraphMatrixImplementation import GraphMatrixImplementation
from org.ds.graph.TopologicalSort import TopoloicalSort
from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.tree.BinaryHeap import BinaryHeapUsingArray
from org.ds.graph.common.Edge import Edge


class ShortestPath:
    def singleSourceShortedPathUsingDijsktraAlgo(self, graph, graphType="UNDIRECTED", rootVertexName=None, isPrint=True):
        binaryHeap = BinaryHeapUsingArray("MIN_HEAP");

        sourceShortedPathVerticesMap = {};
        sourceShortedPathWeightMap = {};

        if rootVertexName is None:
            rootVertex = graph.getVertexMap().values()[0];
        elif rootVertexName in graph.getVertexMap():
            rootVertex = graph.getVertexMap()[rootVertexName];
        else:
            print("Start Vertex Not Present");
            return False;

        vertex = rootVertex;

        sourceShortedPathVerticesMap[vertex] = [];
        sourceShortedPathWeightMap[vertex] = 0;
        binaryHeap.insert(vertex, 0);

        for tempVertex in graph.getVertexMap().values():
            if tempVertex == vertex:
                continue;

            binaryHeap.insert(tempVertex, float("inf"));
#             Check For this Condition
            sourceShortedPathWeightMap[tempVertex] = 0;
            sourceShortedPathVerticesMap[tempVertex] = [];

        while binaryHeap.getHeapSize() > 0:
            vertex = binaryHeap.findMin();
            sourceShortedPathVerticesMap[vertex].append(vertex);
            if graphType is "UNDIRECTED":
                for edge in vertex.getEdgeList():
                    endVertex = edge.getToVertex() if edge.getFromVertex() == vertex else edge.getFromVertex();
    
                    if binaryHeap.decreasePriority(endVertex, sourceShortedPathWeightMap[vertex] + edge.getWeight()):
                        sourceShortedPathWeightMap[endVertex] = sourceShortedPathWeightMap[vertex] + edge.getWeight();
                        sourceShortedPathVerticesMap[endVertex] = copy.deepcopy(sourceShortedPathVerticesMap[vertex]);
            elif graphType is "DIRECTED":
                for edge in vertex.getOutEdgeList():
                    endVertex = edge.getToVertex() if edge.getFromVertex() == vertex else edge.getFromVertex();

                    if binaryHeap.decreasePriority(endVertex, sourceShortedPathWeightMap[vertex] + edge.getWeight()):
                        sourceShortedPathWeightMap[endVertex] = sourceShortedPathWeightMap[vertex] + edge.getWeight();
                        sourceShortedPathVerticesMap[endVertex] = copy.deepcopy(sourceShortedPathVerticesMap[vertex])

        if isPrint:
            print("Dijsktra Algo Single Source Shortest Path");
            for key, value in sourceShortedPathWeightMap.iteritems():
                print("Source Vertex : " + rootVertex.getName() + ", To Vertex : " + key.getName() + ", with length : " + str(value) + " and path is : ");
    
                for vertex in sourceShortedPathVerticesMap[key]:
                    print(vertex.getName());
        return sourceShortedPathWeightMap;

    def relax(self, sourceDistanceMap, sourceShortedPathParentMap, edge):
        newDistance = sourceDistanceMap[edge.getFromVertex()] + edge.getWeight()
        if sourceDistanceMap[edge.getToVertex()] > newDistance:
            sourceDistanceMap[edge.getToVertex()] = newDistance;
            sourceShortedPathParentMap[edge.getToVertex()] = edge.getFromVertex();

    def singleSourceShortedPathUsingBellmanFordAlgo(self, graph, rootVertexName=None, isPrint=True):
        sourceDistanceMap = {};
        sourceShortedPathParentMap = {};

        if rootVertexName is None:
            rootVertex = graph.getVertexMap().values()[0];
        elif rootVertexName in graph.getVertexMap():
            rootVertex = graph.getVertexMap()[rootVertexName];
        else:
            print("Start Vertex Not Present");
            return False;
        vertex = rootVertex;

        sourceDistanceMap[vertex] = 0;

        for tempVertex in graph.getVertexMap().values():
            if tempVertex == vertex:
                continue;

            sourceDistanceMap[tempVertex] = float("inf");
            sourceShortedPathParentMap[tempVertex] = None;

        for iLoop in range(1, len(graph.getVertexMap())):
            iLoop += 1;

            for edge in graph.getEdgeMap().values():
                self.relax(sourceDistanceMap, sourceShortedPathParentMap, edge);

        isNegativeCycle = False;
        for edge in graph.getEdgeMap().values():
            if sourceDistanceMap[edge.getToVertex()] > sourceDistanceMap[edge.getFromVertex()] + edge.getWeight():
                print("\nGraph contains -ve Edge cycle(Using Bellman Ford Algo)");
                isNegativeCycle = True;
                sourceDistanceMap = {};
                break;

        if not isNegativeCycle and isPrint:
            print("\nVertex Distance From Source(Using Bellman Ford Algo)");
            for key, value in sourceDistanceMap.iteritems():
                print(key.getName(), str(value));

        return sourceDistanceMap;

    def allPairShortedPathUsingFloydWarshalls(self, graph):
        dist = [[0 for y in range(graph.getVertexCount())] for x in range(graph.getVertexCount())];

        for iLoop in range(graph.getVertexCount()):
            for jLoop in range(graph.getVertexCount()):
                if iLoop == jLoop:
                    continue;
                elif graph.getGraphWeightMatrix()[iLoop][jLoop] != 0:
                    dist[iLoop][jLoop] = graph.getGraphWeightMatrix()[iLoop][jLoop];
                else:
                    dist[iLoop][jLoop] = float("inf");

        for KLoop in range(graph.getVertexCount()):
            for iLoop in range(graph.getVertexCount()):
                for jLoop in range(graph.getVertexCount()):
                    if dist[iLoop][jLoop] > dist[iLoop][KLoop] + dist[KLoop][jLoop]:
                        dist[iLoop][jLoop] = dist[iLoop][KLoop] + dist[KLoop][jLoop];

        print("Floyd Warshalls Algo For All Pair Shortest Path");
        for iLoop in range(graph.getVertexCount()):
            for jLoop in range(graph.getVertexCount()):
                print("Source Vertex : " + graph.getIndexVertexMap()[iLoop] + ", To Vertex : " + graph.getIndexVertexMap()[jLoop] + ", with length : " + str(dist[iLoop][jLoop]));
            print("\n");

    def allPairShortedPathUsingJohnsonsAlgo(self, graph):
        graph.addVertex("S");

        iLoop = 1;
        for vertexName in graph.getVertexMap().iterkeys():
            graph.addEdge("S", vertexName, "S" + str(iLoop), 0);
            iLoop += 1;

        sourceDistanceMap = self.singleSourceShortedPathUsingBellmanFordAlgo(graph, "S", False);

        graph.removeVertex("S");

        if len(sourceDistanceMap) > 0:
            for edge in graph.getEdgeMap().itervalues():
                edge.setWeight(edge.getWeight() + sourceDistanceMap[edge.getFromVertex()] - sourceDistanceMap[edge.getToVertex()]);
        else:
            return False;

        allPairShortestPathMap = {};

        for vertex in graph.getVertexMap().itervalues():
            allPairShortestPathMap[vertex] = self.singleSourceShortedPathUsingDijsktraAlgo(graph, "DIRECTED", vertex.getName(), False);

        print("\nJohnsons Algo");
        for rootVertex, sourceShortedPathWeightMap in allPairShortestPathMap.iteritems():
            for key, value in sourceShortedPathWeightMap.iteritems():
                print("Source Vertex : " + rootVertex.getName() + ", To Vertex : " + key.getName() + ", with length : " + str(value));
            print("\n");
            
    def singleSourceShortedPathInDAG(self, graph, rootVertexName=None, isPrint=True):
        rootVertex = None;
        if rootVertexName is None:
            rootVertex = graph.getVertexMap().values()[0];
        elif rootVertexName in graph.getVertexMap():
            rootVertex = graph.getVertexMap()[rootVertexName];
        else:
            print("Start Vertex Not Present");
            return False;

        sourceVertex = graph.getVertexMap().values()[0];

        distanceMap = {};
        
        stack = TopoloicalSort().topologicalSortUsingDFS(graph);

        fromVertex = stack.pop();
        
        while stack.getSize() > 0:
            toVertex = stack.pop();
            
            for edge in fromVertex.listOutEdges():
                if edge.getToVertex() == toVertex:
                    print()
                    
if __name__ == '__main__':
    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
    g.addVertex("V8");
    g.addVertex("V9");

    g.addEdge("V1", "V2", "E1", 4);
    g.addEdge("V1", "V8", "E2", 8);

    g.addEdge("V2", "V3", "E3", 8);
    g.addEdge("V2", "V8", "E4", 11);

    g.addEdge("V3", "V4", "E5", 7);
    g.addEdge("V3", "V6", "E6", 4);
    g.addEdge("V3", "V9", "E7", 2);

    g.addEdge("V4", "V5", "E8", 9);
    g.addEdge("V4", "V6", "E9", 14);
    
    g.addEdge("V5", "V6", "E10", 10);

    g.addEdge("V6", "V7", "E11", 2);

    g.addEdge("V7", "V8", "E12", 1);
    g.addEdge("V7", "V9", "E13", 6);
    
    g.addEdge("V8", "V9", "E14", 7);

    sp = ShortestPath();
    sp.singleSourceShortedPathUsingDijsktraAlgo(g);
    
    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    
    g.addEdge("V1", "V2", "E1", -1);
    
    g.addEdge("V2", "V3", "E2", 2);
    g.addEdge("V2", "V4", "E3", 2);
    g.addEdge("V2", "V5", "E4", 3);

    g.addEdge("V3", "V4", "E5", -3);

    g.addEdge("V4", "V2", "E6", 1);
    g.addEdge("V4", "V5", "E7", 5);

    g.addEdge("V5", "V1", "E8", 4);

    sp = ShortestPath();
    sp.singleSourceShortedPathUsingBellmanFordAlgo(g);

    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");

    g.addEdge("V1", "V2", "E1", 0);
    g.addEdge("V1", "V3", "E2", 3);
    g.addEdge("V1", "V4", "E3", 3);

    g.addEdge("V2", "V3", "E4", 0);

    g.addEdge("V3", "V4", "E5", 0);


    sp = ShortestPath();
    sp.singleSourceShortedPathUsingDijsktraAlgo(g, "DIRECTED", "V3");

    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");

    g.addEdge("V1", "V4", "E1", 1);

    g.addEdge("V2", "V1", "E2", 0);
    g.addEdge("V2", "V3", "E3", 0);

    g.addEdge("V3", "V1", "E4", 1);
    g.addEdge("V3", "V4", "E5", 1);

    g.addEdge("V4", "V2", "E6", 0);
    g.addEdge("V4", "V3", "E7", 1);

    sp = ShortestPath();
    sp.singleSourceShortedPathUsingDijsktraAlgo(g, "DIRECTED", "V1");


    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
 
    g.addEdge("V1", "V2", "E1", -5);
    g.addEdge("V1", "V3", "E2", 2);
    g.addEdge("V1", "V4", "E3", 3);
 
    g.addEdge("V2", "V3", "E4", 4);
 
    g.addEdge("V3", "V4", "E5", 1);
     
    sp = ShortestPath();
    sp.allPairShortedPathUsingJohnsonsAlgo(g);
    
    
    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    
    g.addEdge("V1", "V4", "E1", 2);
    
    g.addEdge("V2", "V1", "E2", 6);
    g.addEdge("V2", "V3", "E3", 3);
    
    g.addEdge("V3", "V1", "E4", 4);
    g.addEdge("V3", "V4", "E5", 5);
    
    g.addEdge("V4", "V2", "E6", -7);
    g.addEdge("V4", "V3", "E7", -3);
     
    sp = ShortestPath();
    sp.allPairShortedPathUsingJohnsonsAlgo(g);


    g1 = GraphMatrixImplementation(4);
    g1.addVertex("V1");
    g1.addVertex("V2");
    g1.addVertex("V3");
    g1.addVertex("V4");

    g1.addEdge("V1", "V3", -2);
 
    g1.addEdge("V2", "V1", 4);
    g1.addEdge("V2", "V3", 3);
 
    g1.addEdge("V3", "V4", 2);
 
    g1.addEdge("V4", "V2", -1);

    
#     g1.addEdge("V1", "V2", 5);
# 
#     g1.addEdge("V2", "V3", 3);
#     g1.addEdge("V3", "V4", 1);
# 
#     g1.addEdge("V1", "V4", 10);
    
    sp = ShortestPath();
    sp.allPairShortedPathUsingFloydWarshalls(g1);
