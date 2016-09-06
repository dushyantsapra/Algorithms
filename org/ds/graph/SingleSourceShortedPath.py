'''
Created on Sep 2, 2016

@author: Dushyant Sapra
'''

import copy

from org.ds.graph.DirectedGraph import DirectedGraph
from org.ds.graph.GraphMatrixImplementation import GraphMatrixImplementation
from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.tree.BinaryHeap import BinaryHeapUsingArray


class ShortestPath:
    def dijsktraAlgo(self, graph, graphType="UNDIRECTED"):
        binaryHeap = BinaryHeapUsingArray("MIN_HEAP");

        sourceShortedPathVerticesMap = {};
        sourceShortedPathWeightMap = {};

        rootVertex = graph.getVertexMap().values()[0];
        vertex = rootVertex;

        sourceShortedPathVerticesMap[vertex] = [];
        sourceShortedPathWeightMap[vertex] = 0;
        binaryHeap.insert(vertex, 0);

        for tempVertex in graph.getVertexMap().values():
            if tempVertex == vertex:
                continue;

            binaryHeap.insert(tempVertex, float("inf"));
#             Check For this Condition
            sourceShortedPathWeightMap[vertex] = 0;
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

        for key, value in sourceShortedPathWeightMap.iteritems():
            print("Source Vertex : " + rootVertex.getName() + ", To Vertex : " + key.getName() + ", with length : " + str(value) + " and path is : ");

            for vertex in sourceShortedPathVerticesMap[key]:
                print(vertex.getName()); 

    def relax(self, sourceDistanceMap, sourceShortedPathParentMap, edge):
        newDistance = sourceDistanceMap[edge.getFromVertex()] + edge.getWeight()
        if sourceDistanceMap[edge.getToVertex()] > newDistance:
            sourceDistanceMap[edge.getToVertex()] = newDistance;
            sourceShortedPathParentMap[edge.getToVertex()] = edge.getFromVertex();

    def bellmanFordAlgo(self, graph):
        sourceDistanceMap = {};
        sourceShortedPathParentMap = {};
    
        rootVertex = graph.getVertexMap().values()[0];
        vertex = rootVertex;

        sourceDistanceMap[vertex] = 0;
    
        for tempVertex in graph.getVertexMap().values():
            if tempVertex == vertex:
                continue;
    
            sourceDistanceMap[tempVertex] = float("inf");
            sourceShortedPathParentMap[vertex] = None;
    
        for iLoop in range(1, len(graph.getVertexMap())):
            iLoop += 1;
    
            for edge in graph.getEdgeMap().values():
                self.relax(sourceDistanceMap, sourceShortedPathParentMap, edge);
    
        isNegativeCycle = False;
        for edge in graph.getEdgeMap().values():
            if sourceDistanceMap[edge.getToVertex()] > sourceDistanceMap[edge.getFromVertex()] + edge.getWeight():
                print("Graph contains -ve Edge cycle");
                isNegativeCycle = True;
                break;
    
        if not isNegativeCycle:
            print("Vertex        Distance From Source");
            for key, value in sourceDistanceMap.iteritems():
                print(key.getName(), str(value));

    def floydWarshalls(self, graph):
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
    sp.dijsktraAlgo(g);
    
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
    sp.bellmanFordAlgo(g);
    
    g = GraphMatrixImplementation(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(0, 3);
    
    print("\n");
    for iLoop in range(len(g)):
        for jLoop in range(len(g[iLoop])):
            print(g[iLoop][jLoop]);
        print("\n");
