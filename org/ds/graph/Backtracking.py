'''
Created on Sep 15, 2016

@author: Dushyant Sapra
'''

from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.queue.Queue import Queue


class Backtracking:

    def checkForPathMoreThanGivenLength(self, graph, startVertex, length):
        queue = Queue();

        visitedVertexMap = {};

        queue.enQueue(startVertex);
        visitedVertexMap[startVertex] = True;

        currentLength = 0;

        while queue.getSize() > 0:
            vertex = queue.deQueue();

            for edge in vertex.getEdgeList():
                otherVertex = edge.getToVertex() if vertex == edge.getFromVertex() else edge.getFromVertex();

                if otherVertex in visitedVertexMap and not visitedVertexMap[otherVertex]:
                    queue.enQueue(otherVertex);
                    currentLength += edge.getWeight();

    def printAllPathUsingDFSHelper(self, vertex, endVertexName, graph, graphType, visitedVertexMap, path):
        visitedVertexMap[vertex] = True;
        path.append(vertex);
        if graphType is "UNDIRECTED":
            for tempVertex in vertex.getAdjacentVertex():
                if tempVertex in visitedVertexMap and not visitedVertexMap[tempVertex]:
                    self.printAllPathUsingDFSHelper(tempVertex, graph, graphType, visitedVertexMap);
            
        elif graphType is "DIRECTED":
            for tempVertex in vertex.getOutVerticesList():
                if tempVertex in visitedVertexMap and not visitedVertexMap[tempVertex]:
                    self.printAllPathUsingDFSHelper(tempVertex, graph, graphType, visitedVertexMap);

    def printAllPathUsingDFS(self, startVertexName, endVertexName, graph, graphType):
        vertex = graph.getVertexMap()[startVertexName];
        visitedVertexMap = {};
        path = [];
        self.printAllPathUsingDFSHelper(vertex, endVertexName, graph, graphType, visitedVertexMap, path);
        
    def printAllPathUsingBFS(self, graph):
        print()

if __name__ is '__main__':
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

    g.addEdge("V0", "V1", "E1", 4);
    g.addEdge("V0", "V7", "E2", 8);

    g.addEdge("V1", "V2", "E3", 8);
    g.addEdge("V1", "V7", "E4", 11);
   
    g.addEdge("V2", "V3", "E5", 7);
    g.addEdge("V2", "V5", "E6", 4);
    g.addEdge("V2", "V8", "E7", 2);

    g.addEdge("V3", "V4", "E8", 9);
    g.addEdge("V3", "V5", "E9", 14);

    g.addEdge("V4", "V5", "E10", 10);

    g.addEdge("V5", "V6", "E11", 2);

    g.addEdge("V6", "V7", "E12", 1);
    g.addEdge("V6", "V8", "E13", 6);

    g.addEdge("V7", "V8", "E14", 7);
    
    g.dfsUsingRecursion("V0");
