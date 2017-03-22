'''
Created on Sep 14, 2016

@author: Dushyant sapra
'''

from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.graph.DisjointSet import DisjointSet
from random import randint

class KargersAlgoForMinimumCut:
    def kargersAlgo(self, graph):
        disjointSet = DisjointSet();

        for vertex in graph.getVertexMap().values():
            disjointSet.makeSet(vertex);

        minCutEdges = [];
        vertexCount = len(graph.getVertexMap());

        iValue = 1;

        while vertexCount > 2:
            randonIndex = randint(0, len(graph.getEdgeMap()) - iValue);
            edge = list(graph.getEdgeMap().values())[randonIndex];
            if disjointSet.union(edge.getFromVertex(), edge.getToVertex()):
                vertexCount -= 1;
                iValue += 1;

        for edge in graph.getEdgeMap().values():
            if disjointSet.findSet(edge.getFromVertex()) == disjointSet.findSet(edge.getToVertex()):
                continue;
            else:
                minCutEdges.append(edge);

        if len(minCutEdges) > 0:
            print("Minimum Cut Edge To Disconnect the Graph is : ");
            for edge in minCutEdges:
                print(edge);

if __name__ == '__main__':
    g = UnDirectedGraph();

    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");

    g.addEdge("V0", "V1", "A");
    g.addEdge("V0", "V2", "B");
    g.addEdge("V0", "V3", "C");

    g.addEdge("V1", "V3", "D");

    g.addEdge("V2", "V3", "E");

    obj = KargersAlgoForMinimumCut();
    obj.kargersAlgo(g);
