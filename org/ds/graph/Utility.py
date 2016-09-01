'''
Created on Aug 19, 2016

@author: Dushyant Sapra
'''
from org.ds.graph.DisjointSet import DisjointSet
from org.ds.graph.UndirectedGraph import UnDirectedGraph

class Utility:
    @staticmethod
    def checkForCycleInUnDirectedGraph(graph):
        disjoinSet = DisjointSet();
        for key in graph.vertexMap.iterkeys():
            disjoinSet.makeSet(key);

        for value in graph.edgeMap.itervalues():
            fromParentNode = disjoinSet.findSet(value.getFromVertex().getName());
            toParentNode = disjoinSet.findSet(value.getToVertex().getName());

            if fromParentNode is toParentNode:
                print("Graph Contains A Cycle");
                return False;

            disjoinSet.union(value.getFromVertex().getName(), value.getToVertex().getName());

        print("Graph Doesn't have a Cycle");
        return False;
if __name__ == '__main__':
    # Test Case 2, Checking For Cycle in a graph
    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");

    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V4", "E2");

    g.addEdge("V2", "V5", "E3");
    # g.addEdge("V2", "V3", "E4");

    g.addEdge("V3", "V6", "E5");
    
    g.addEdge("V5", "V6", "E6");

    utility = Utility();

    utility.checkForCycleInUnDirectedGraph(g);