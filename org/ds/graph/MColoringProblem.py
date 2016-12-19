'''
Created on Oct 4, 2016

@author: DUshyant Sapra
'''
from org.ds.graph.UndirectedGraph import UnDirectedGraph

class MColoringProblem:
    def canColorVertex(self, vertex, purposedColor, visitedVertexColorMap):
        isSafe = True;

        for tempVertex in vertex.getAdjacentVertex():
            if visitedVertexColorMap[tempVertex] == -1:
                continue;
            elif visitedVertexColorMap[tempVertex] == purposedColor:
                isSafe = False;
                break;
        return isSafe;

    def mColoringProblem(self, graph, maxColor):
        visitedVertexColorMap = {};

        isPossible = False;

        for vertex in graph.getVertexMap().values():
            visitedVertexColorMap[vertex] = -1;

        for vertex in visitedVertexColorMap:
            for iColor in range(1, maxColor + 1):
                if self.canColorVertex(vertex, iColor, visitedVertexColorMap):
                    visitedVertexColorMap[vertex] = iColor;
                    isPossible = True;
                    break;

            if not isPossible:
                print("Graph can't be colored with given Colors");
                return False;
            isPossible = False;

        print("Graph can be colored with given Colors");
        for vertex, color in visitedVertexColorMap.items():
            print("vertex " + vertex.getName() + ", is Colored With " + str(color) + " Color");
            


if __name__ == '__main__':
    g = UnDirectedGraph();
    
    g.addVertex("A");
    g.addVertex("B");
    g.addVertex("C");
    g.addVertex("D");
    g.addVertex("E");
    g.addVertex("F");
    g.addVertex("G");
    g.addVertex("H");
    g.addVertex("I");
    g.addVertex("J");
    
    g.addEdge("A", "C", "E1");
    g.addEdge("A", "F", "E2");
    g.addEdge("A", "D", "E3");
    
    g.addEdge("C", "J", "E4");
    g.addEdge("C", "E", "E5");
    
    g.addEdge("F", "I", "E6");
    g.addEdge("F", "B", "E7");
    
    g.addEdge("J", "H", "E8");
    g.addEdge("J", "B", "E9");
    
    g.addEdge("E", "I", "E10");
    g.addEdge("E", "G", "E11");
    
    g.addEdge("G", "B", "E12");
    g.addEdge("G", "D", "E13");
    
    g.addEdge("H", "I", "E14");
    g.addEdge("H", "D", "E15");
    
    obj = MColoringProblem();
    obj.mColoringProblem(g, 3);
    
    g = UnDirectedGraph();
    g.addVertex("A");
    g.addVertex("B");
    g.addVertex("C");
    g.addVertex("D");
    
    g.addEdge("A", "B", "E1");
    g.addEdge("A", "D", "E2");

    g.addEdge("B", "C", "E3");
    g.addEdge("B", "D", "E4");
    
    g.addEdge("C", "D", "E5");
    
    obj = MColoringProblem();
    print("\n")
    obj.mColoringProblem(g, 3);