'''
Created on Sep 20, 2016

@author: Dushyant Sapra
'''

from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.queue.Queue import Queue


class Backtracking:
    def checkForPathFromSourceOfMoreThanGivenLengthHelper(self, graph, sourceVertex, length, visitedVertexMap, path):
        visitedVertexMap[sourceVertex] = True;
        path.append(sourceVertex);

        for e in sourceVertex.getEdgeList():
            otherVertex = e.getToVertex() if e.getFromVertex() == sourceVertex else e.getFromVertex();

            if otherVertex in visitedVertexMap and visitedVertexMap[otherVertex]:
                continue;

            if e.getWeight() >= length:
                print("\nFound A path with Extra Length of : " + str((e.getWeight() - length)) + "\n");
                path.append(otherVertex);
                return True;

            if self.checkForPathFromSourceOfMoreThanGivenLengthHelper(graph, otherVertex, length - e.getWeight(), visitedVertexMap, path):
                return True;
        del visitedVertexMap[sourceVertex];
        path.pop();
        return False;

    def checkForPathFromSourceOfMoreThanGivenLength(self, graph, sourceVertexName, length):
        if sourceVertexName not in graph.getVertexMap():
            print("Source Vertex Present In Graph");
            return False;

        sourceVertex = graph.getVertexMap()[sourceVertexName];

        visitedVertexMap = {};
        path = [];

        if self.checkForPathFromSourceOfMoreThanGivenLengthHelper(graph, sourceVertex, length, visitedVertexMap, path):
            print("Graph has a Path of length : " + str(length));

            for vertex in path:
                print(vertex);

    def printAllPathFromSourceToDestinationHelper(self, vertex, endVertex, graph, graphType, visitedVertexMap, path):
        visitedVertexMap[vertex] = True;
        path.append(vertex);

        if vertex == endVertex:
            print("Path is : ");
            for v in path:
                print(v);
            del visitedVertexMap[vertex];
            path.pop();
            return;

        if graphType is "UNDIRECTED":
            for tempVertex in vertex.getAdjacentVertex():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex]:
                    continue;

                self.printAllPathFromSourceToDestinationHelper(tempVertex, endVertex, graph, graphType, visitedVertexMap, path);
            path.pop();
            del visitedVertexMap[vertex];

        if graphType is "DIRECTED":
            for tempVertex in vertex.getOutVerticesList():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex]:
                    continue;

                self.printAllPathFromSourceToDestinationHelper(tempVertex, endVertex, graph, graphType, visitedVertexMap, path);
            path.pop();
            del visitedVertexMap[vertex];

    def printAllPathFromSourceToDestination(self, startVertexName, endVertexName, graph, graphType):
        if startVertexName not in graph.getVertexMap():
            print("Start Vertex Not Present");
            return False;

        if endVertexName not in graph.getVertexMap():
            print("End Vertex Not Present");
            return False;

        vertex = graph.getVertexMap()[startVertexName];
        endVertex = graph.getVertexMap()[endVertexName];
        visitedVertexMap = {};
        path = [];
        self.printAllPathFromSourceToDestinationHelper(vertex, endVertex, graph, graphType, visitedVertexMap, path);

    def colorVertex(self, vertex, parentVertex, maxColor, visitedVertexColorMap):
        purposedColor = 1;
        for tempVertex in vertex.getAdjacentVertex():
            if visitedVertexColorMap[tempVertex] == -1:
                print()

    def mColoringProblemHelper(self, sourceVertex, parentVertex, maxColor, visitedVertexColorMap):
        parentVertexMap = {};

        parentVertexMap[sourceVertex] = sourceVertex;
        visitedVertexColorMap[sourceVertex] = 1;

        visitedVertexQueue = Queue();
        visitedVertexQueue.enQueue(sourceVertex);

        while visitedVertexQueue.getSize() > 0:
            tempVertex = visitedVertexQueue.deQueue();

            if visitedVertexColorMap[tempVertex] == -1:
                self.colorVertex(tempVertex, parentVertexMap[tempVertex], maxColor, visitedVertexColorMap);

            for v in tempVertex.getAdjacentVertex():
                if visitedVertexColorMap[v] == -1:
                    parentVertexMap[v] = tempVertex;
                    visitedVertexQueue.enQueue(v);

    def mColoringProblem(self, graph, maxColor):
        if maxColor < 1:
            print("Can't Be Colored");
            return False;

        visitedVertexColorMap = {};

        for vertex in visitedVertexColorMap.values():
            visitedVertexColorMap[vertex] = -1;

        sourceVertex = list(graph.getVertexMap().values())[0];

        self.mColoringProblemHelper(sourceVertex, sourceVertex, maxColor, visitedVertexColorMap);

if __name__ == '__main__':
    g = UnDirectedGraph();
 
    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
     
    g.addEdge("V0", "V1", "E1");
    g.addEdge("V0", "V2", "E2");
    g.addEdge("V0", "V4", "E3");
    
    g.addEdge("V1", "V2", "E4");
    
    g.addEdge("V2", "V3", "E5");
    g.addEdge("V2", "V5", "E6");
    
    g.addEdge("V3", "V5", "E7");
    
    g.addEdge("V4", "V5", "E8");
    
    obj = Backtracking();
    obj.printAllPathFromSourceToDestination("V0", "V4", g, "UNDIRECTED");
    
    
    
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
    
    obj = Backtracking();
    obj.checkForPathFromSourceOfMoreThanGivenLength(g, "V0", 10);

    
    g = UnDirectedGraph();
    
#     g.addVertex("V0");
#     g.addVertex("V1");
#     g.addVertex("V2");
#     g.addVertex("V3");
#     g.addVertex("V4");
#     g.addVertex("V5");
#     g.addVertex("V6");
#     g.addVertex("V7");
#     g.addVertex("V8");
#     g.addVertex("V9");
#     
#     g.addEdge("V0", "V4", "E1");
#     g.addEdge("V0", "V5", "E2");	
#     g.addEdge("V0", "V9", "E3");
#     
#     g.addEdge("V1", "V3", "E4");
#     g.addEdge("V1", "V7", "E5");
#     g.addEdge("V1", "V9", "E6");
#     
#     g.addEdge("V2", "V4", "E7");    
#     g.addEdge("V2", "V7", "E8");
#     g.addEdge("V2", "V8", "E9");
#     
#     g.addEdge("V3", "V4", "E10");
#     g.addEdge("V3", "V6", "E11");
#     
#     g.addEdge("V5", "V6", "E12");
#     g.addEdge("V5", "V7", "E13");
#     
#     g.addEdge("V6", "V8", "E14");
#     
#     g.addEdge("V8", "V9", "E15");


    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    
    g.addEdge("V0", "V1", "E1");
    g.addEdge("V0", "V2", "E2");    
    g.addEdge("V0", "V3", "E3");
    
    g.addEdge("V1", "V3", "E4");
    g.addEdge("V2", "V3", "E5");
    
    obj = Backtracking();
    obj.mColoringProblem(g, 2);
