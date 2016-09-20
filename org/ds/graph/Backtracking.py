'''
Created on Sep 20, 2016

@author: Dushyant Sapra
'''

from org.ds.graph.UndirectedGraph import UnDirectedGraph


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


    def colorTheVertex(self, vertex, currentColor, parentVertexColor, visitedVertexColorMap):
        for v in vertex.getAdjacentVertex():
            print()

#     Always Start With Color Count 1 
    def mColoringProblemHelper(self, vertex, parentVertexColor, graph, maxColor, visitedVertexColorMap):
        self.colorTheVertex(vertex, 1, parentVertexColor, visitedVertexColorMap);

    def mColoringProblem(self, graph, maxColor):
        visitedVertexColorMap = {}
        sourceVertex = graph.getVertexMap().values([0]);
        visitedVertexColorMap[sourceVertex] = 1;


if __name__ == '__main__':
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

    obj = Backtracking();
    obj.hamiltonianPathOrCircuit(g);


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
