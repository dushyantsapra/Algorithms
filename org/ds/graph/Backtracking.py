'''
Created on Sep 20, 2016

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
        
        vertex = graph.getVertexMap().values()[0];
        
        hamiltonPath = []
        
        isHamilton = self.hamiltonianPathOrCircuitHelper(graph, vertex, vertex, visitedVertexMap, hamiltonPath);
        
        if isHamilton:
            print("Given Graph contain's Hamiltion Cycle");
            print("Hamiltion Path is : ");
            for v in hamiltonPath:
                print(v);
        else:
            print("Graph is Not Hamiltion");

if __name__ is '__main__':
    print("asdasda");
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
    
#     g.addEdge("V3", "V4", "E7");
    
    obj = Backtracking();
    obj.hamiltonianPathOrCircuit(g);