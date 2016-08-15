'''
Created on Aug 14, 2016

@author: Dushyant Sapra
'''
from org.ds.graph.DisjointSet import DisjointSet
from org.ds.graph.UndirectedGraph import Graph
from org.ds.tree.BinaryHeap import BinaryHeapUsingArray


# A Tree is a connected subgraph without any cycle
# For G(V, E) to be a spanning Tree it should be undirected
# If a tree has all the vertices of a graph and edges 1 less then total vertices then that tree is Spanning Tree, i.e |V| - 1 edges.
# If edge weight are distinct then we will have unique MST(minimum Spanning Tree) else we can have n number of MST with same lenght/weight/
# Number of MST can be n power (n-2), where n is vertices
class MinimumSpanningTree:
#     For Sort Edges Based upon there lenght/weight
#     Iterate over all the sorted Edges
#     Use DisjointSet function
#         i) MakeSet
#         ii) findSet
#         iii) Union
#     If in set ii) we find a edge whose both vertices are in same set then drop that edge and continue, else store that edge

    def getEdgeWeight(self, edge):
        return edge.getWeight();

    def kruskalsAlgo(self, graph):
        sortedEdgeList = [];
        disjointSet = DisjointSet();
        mstEdgeList = [];

        for value in graph.getEdgeMap().itervalues():
            sortedEdgeList.append(value);

        sortedEdgeList = sorted(sortedEdgeList, key=lambda edge: edge.getWeight());

        for key in g.getVertexMap().iterkeys():
            disjointSet.makeSet(key);

        for edge in sortedEdgeList:
            fromParentNode = disjointSet.findSet(edge.getFromVertex().getName());
            toParentNode = disjointSet.findSet(edge.getToVertex().getName());

            if fromParentNode is toParentNode:
                continue;

            mstEdgeList.append(edge);
            disjointSet.union(edge.getFromVertex().getName(), edge.getToVertex().getName());

        print("Minimum Spanning Tree Edges are : ")
        for edge in mstEdgeList:
            print(edge);
        
#     def primsAlgo(self):
        

if __name__ == '__main__':
    g = Graph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    
    g.addEdge("V1", "V2", "E1", 6);
    g.addEdge("V1", "V4", "E2", 2);
    
    g.addEdge("V2", "V5", "E3", 5);
    g.addEdge("V2", "V3", "E4", 1);
     
    g.addEdge("V3", "V6", "E5", 3);
     
    g.addEdge("V5", "V6", "E6", 4);

    mst = MinimumSpanningTree();
#     mst.kruskalsAlgo(g);

    edgeList = [];
    for value in g.getEdgeMap().itervalues():
        edgeList.append(value);
    
    binaryHeapUsingArray = BinaryHeapUsingArray("MIN_HEAP");
    for edge in edgeList:
        binaryHeapUsingArray.insert(edge);

    binaryHeapUsingArray.traverseTree();
