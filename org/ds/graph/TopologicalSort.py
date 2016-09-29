'''
Created on Sep 27, 2016

@author: Dushyant sapra
'''

from org.ds.graph.DirectedGraph import DirectedGraph
from org.ds.graph.common.DFSApplicationUtil import DFSApplicationUtil
from org.ds.stack.Stack import StackUsingLinkedList


class TopoloicalSort:
    def topologicalSortUsingDFS(self, graph):
        visitedVertexMap = {};
        stack = StackUsingLinkedList();

        for vertex in graph.getVertexMap().values():
            visitedVertexMap[vertex] = False;

        for vertex, value in visitedVertexMap.iteritems():
            if not value:
                DFSApplicationUtil.topologicalSortUsingDFSHelper(vertex, visitedVertexMap, stack); 

        print("Topological Sort Using DFS is : ");
        while stack.getSize() > 0:
            print(stack.pop());

    def topologicalSortUsingKhanAlgo(self, directedGraph):
        zeroInVertexList = [];
        topologicalSortedVertexList = [];

        inVertexCountMap = {};

        for vertex in directedGraph.vertexMap.itervalues():
            inVertexCountMap[vertex] = len(vertex.getInVerticesList());
            if len(vertex.getInVerticesList()) == 0:
                zeroInVertexList.append(vertex);

        while len(zeroInVertexList) > 0:
            vertex = zeroInVertexList.pop(0);
            topologicalSortedVertexList.append(vertex);
            for inVertex in vertex.getOutVerticesList():
                inVertexCountMap[inVertex] = inVertexCountMap[inVertex] - 1;
                if inVertexCountMap[inVertex] == 0:
                    zeroInVertexList.append(inVertex);

        isTrue = True;
        for lt in inVertexCountMap.itervalues():
            if lt > 0:
                isTrue = False;
                break;

        if isTrue:
            print("Topological Sort Using Khan's Algo is : ");
            for v in topologicalSortedVertexList:
                print(v);
        else:
            print("Graph is not a Directed Acyclic Graph");
    
if __name__ == '__main__':
    obj = TopoloicalSort();

    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
 
    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V3", "E2");
    g.addEdge("V1", "V4", "E3");
 
    g.addEdge("V2", "V5", "E4");
 
    g.addEdge("V5", "V6", "E5");
    g.addEdge("V3", "V6", "E6");
    g.addEdge("V4", "V6", "E7");

    g.addEdge("V6", "V7", "E8");    
    
    obj.topologicalSortUsingDFS(g);
    obj.topologicalSortUsingKhanAlgo(g);
    
    g = DirectedGraph();
    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
 
    g.addEdge("V2", "V3", "E1");
    
    g.addEdge("V3", "V1", "E2");
    
    g.addEdge("V4", "V0", "E3");
    g.addEdge("V4", "V1", "E4");
 
    g.addEdge("V5", "V0", "E5");
    g.addEdge("V5", "V2", "E6");
    
    obj.topologicalSortUsingDFS(g);
    obj.topologicalSortUsingKhanAlgo(g);