'''
Created on Sep 14, 2016

@author: Dushyant sapra
'''

from org.ds.graph.UndirectedGraph import UnDirectedGraph
from copy import deepcopy
from org.ds.graph.DisjointSet import DisjointSet
from random import randint

class KargersAlgoForMinimumCut:
    def kargersAlgo(self, graph):
        contractedGraph = deepcopy(graph);
        disjointSet = DisjointSet();

        for vertex in graph.getVertexMap().itervalues():
            disjointSet.makeSet(vertex);

        while len(contractedGraph.getVertexMap()) > 2:
            edge = graph.getEdgeMap().values()[randint(0, len(graph.getEdgeMap()))];
            if disjointSet.union(edge.getFromVertex(), edge.getToVertex()):
                print()

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