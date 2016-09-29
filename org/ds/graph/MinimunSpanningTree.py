'''
Created on Aug 14, 2016

@author: Dushyant Sapra
'''
from org.ds.graph.DisjointSet import DisjointSet
from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.tree.BinaryHeap import BinaryHeapUsingArray

class MinimumSpanningTree:
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
            if disjointSet.union(edge.getFromVertex().getName(), edge.getToVertex().getName()):
                mstEdgeList.append(edge);

        print("Minimum Spanning Tree(kruskalsAlgo) Edges  are : ");
        for edge in mstEdgeList:
            print(edge);

    def primsAlgoUsingVertices(self, graph):
        visitedVertexMap = {};
        binaryHeap = BinaryHeapUsingArray("MIN_HEAP");
        vertexEdgeMap = {};
        mstEdgeList = [];

        vertex = graph.getVertexMap().values()[3];

#         visitedVertexMap[vertex] = 1;
        for tempVertex in graph.getVertexMap().values():
            if tempVertex == vertex:
                binaryHeap.insert(tempVertex, 0);
                continue;
            visitedVertexMap[tempVertex] = False;
            binaryHeap.insert(tempVertex, float("inf"));

        while binaryHeap.getHeapSize() > 0:
            vertex = binaryHeap.findMin();
            if vertex in vertexEdgeMap:
                mstEdgeList.append(vertexEdgeMap[vertex]);
                del vertexEdgeMap[vertex];

            for edge in vertex.getEdgeList():
                endVertex = edge.getToVertex() if edge.getFromVertex() == vertex else edge.getFromVertex();

                if visitedVertexMap[endVertex]:
                    continue;

                if binaryHeap.decreasePriority(endVertex, edge.getWeight()):
                    vertexEdgeMap[endVertex] = edge;
            visitedVertexMap[vertex] = True;

        print("Minimum Spanning Tree(Prim'sAlgo) Edges  are : ");
        for edge in mstEdgeList:
            print(edge);

#     Logic : 
#         1. Pick any Vertex and insert it's adjacent edges in to the binary heap.
#         2. Start Iteration on binary heap, and fetch edge with minimum weight
#         3. Check If all both the end point vertices are already visited, if yes skip that edge else find the other end point vertex
#         4. Repeat Step 2&3 on vertex fetched from step 3 until all vertices are visited.

    def primsAlgoUsingEdge(self, graph):
        visitedVertexMap = {};
        binaryHeap = BinaryHeapUsingArray("MIN_HEAP");
        mstEdgeList = [];

        for vertex in graph.getVertexMap().values():
            visitedVertexMap[vertex] = False;

        vertex = graph.getVertexMap().values()[0];

        visitedVertexMap[vertex] = True;

        for edge in vertex.getEdgeList():
            binaryHeap.insert(edge, edge.getWeight());

        while binaryHeap.getHeapSize() > 0:
            edge = binaryHeap.findMin();
            mstEdgeList.append(edge);

            if visitedVertexMap[edge.getFromVertex()] and visitedVertexMap[edge.getToVertex()]:
                continue;

            vertex = edge.getFromVertex() if not visitedVertexMap[edge.getFromVertex()] else edge.getToVertex();

            visitedVertexMap[vertex] = True;

            for tempEdge in vertex.getEdgeList():
#                 This Edge has already been removed from Binary Heap
                if tempEdge == edge:
                    continue;
                if visitedVertexMap[tempEdge.getFromVertex()] and visitedVertexMap[tempEdge.getToVertex()]:
                    binaryHeap.delete(tempEdge);
                else:
                    binaryHeap.insert(tempEdge, tempEdge.getWeight());

        print("Minimum Spanning Tree(Prim'sAlgo) Edges  are : ");
        for edge in mstEdgeList:
            print(edge);

    def primsAlgo(self, graph, algoType="VERTEX"):
        if algoType is "VERTEX":
            self.primsAlgoUsingVertices(graph);
        elif algoType is "EDGE":
            self.primsAlgoUsingEdge(graph);

if __name__ == '__main__':
    g = UnDirectedGraph();
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

    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
    g.addVertex("V8");

    g.addEdge("V1", "V2", "E1", 9);
    g.addEdge("V1", "V3", "E2", 12);

    g.addEdge("V2", "V3", "E3", 8);
    g.addEdge("V2", "V4", "E4", 2);
    g.addEdge("V2", "V8", "E5", 1);

    g.addEdge("V3", "V4", "E6", 7);
    g.addEdge("V3", "V5", "E7", 6);

    g.addEdge("V4", "V5", "E8", 5);
    g.addEdge("V4", "V6", "E9", 13);
    g.addEdge("V4", "V8", "E10", 3);

    g.addEdge("V5", "V7", "E11", 4);

    g.addEdge("V6", "V7", "E12", 10);
    g.addEdge("V6", "V8", "E13", 11);

    mst = MinimumSpanningTree();
    mst.kruskalsAlgo(g);
    mst.primsAlgo(g);
