'''
Created on Sep 2, 2016

@author: Dushyant Sapra
'''

import copy

from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.tree.BinaryHeap import BinaryHeapUsingArray


class ShortestPath:
    def dijsktraAlgo(self, graph):
        visitedVertexMap = {};
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

            visitedVertexMap[tempVertex] = 0;
            binaryHeap.insert(tempVertex, float("inf"));
            sourceShortedPathWeightMap[vertex] = 0;
            sourceShortedPathVerticesMap[tempVertex] = [];

        while binaryHeap.getHeapSize() > 0:
            vertex = binaryHeap.findMin();
            sourceShortedPathVerticesMap[vertex].append(vertex);
            for edge in vertex.getEdgeList():
                endVertex = edge.getToVertex() if edge.getFromVertex() == vertex else edge.getFromVertex();

                if visitedVertexMap[endVertex] == 1:
                    continue;

                if binaryHeap.decreasePriority(endVertex, sourceShortedPathWeightMap[vertex] + edge.getWeight()):
                    sourceShortedPathWeightMap[endVertex] = sourceShortedPathWeightMap[vertex] + edge.getWeight();
                    sourceShortedPathVerticesMap[endVertex] = copy.deepcopy(sourceShortedPathVerticesMap[vertex])
            visitedVertexMap[vertex] = 1;
        
        for key, value in sourceShortedPathWeightMap.iteritems():
            print("Source Vertex : " + rootVertex.getName() + ", To Vertex : " + key.getName() + ", with length : " + str(value) + " and path is : ");
            
            for vertex in sourceShortedPathVerticesMap[key]:
                print(vertex.getName()); 

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
