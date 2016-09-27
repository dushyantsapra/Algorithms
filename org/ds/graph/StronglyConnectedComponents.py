'''
Created on Sep 27, 2016

@author: Dushyant sapra
'''
from org.ds.graph.DirectedGraph import DirectedGraph
from org.ds.graph.common.DFSApplicationUtil import DFSApplicationUtil
from org.ds.stack.Stack import StackUsingLinkedList


class SCC:
    def kosarajusAlgo(self, graph, isPrint=True):
        connectedComponentCount = 0;

        visitedVertexMap = {};
        for vertex in graph.vertexMap.values():
            visitedVertexMap[vertex] = False;

        stack = StackUsingLinkedList();

        for vertex in graph.getVertexMap().values():
            if not visitedVertexMap[vertex]:
                DFSApplicationUtil.stronglyConnectedCommponentUsingKosarajusAlgoHelper(vertex, visitedVertexMap, False, stack);

        sccVertexMap = {};
        visitedVertexMap = {};
        for vertex in graph.vertexMap.values():
            visitedVertexMap[vertex] = False;

        while stack.getSize() > 0:
            vertex = stack.pop();
            if not visitedVertexMap[vertex]:
                tempStack = StackUsingLinkedList();
                DFSApplicationUtil.stronglyConnectedCommponentUsingKosarajusAlgoHelper(vertex, visitedVertexMap, True, tempStack);
                tempStack.push(vertex);
                sccVertexMap[vertex] = tempStack;
                connectedComponentCount += 1;

        if isPrint:
            print("Total Strongly Connected Components are : " + str(connectedComponentCount));
            iLoop = 1;
            for key in sccVertexMap.keys():
                stack = sccVertexMap[key];
                iLoop += 1;
                print("Strongly Connected Component Number : " + str(iLoop) + ", Vertices are : ");
                while stack.getSize() > 0:
                    print(stack.pop());
                print("\n");

        return sccVertexMap;

    def tarjansAlgo(self, graph, isPrint=True):
        stackVertexMap = {};

        arrivalTimeMap = {};
        for vertex in graph.getVertexMap().itervalues():
            stackVertexMap[vertex] = False;
            arrivalTimeMap[vertex] = -1;
        
        lowTimeMap = {};
        sccStack = StackUsingLinkedList();

        for key, value in arrivalTimeMap.iteritems():
            if value != -1:
                continue;
            else:
                DFSApplicationUtil.stronglyConnectedCommponentUsingTarjansAlgoHelper(key, stackVertexMap, arrivalTimeMap, lowTimeMap, sccStack);

if __name__ == '__main__':
    g = DirectedGraph();
#     g.addVertex("A");
#     g.addVertex("B");
#     g.addVertex("C");
#     g.addVertex("D");
#     g.addVertex("E");
#     g.addVertex("F");
#     g.addVertex("G");
#     g.addVertex("H");
#     g.addVertex("I");
#     g.addVertex("J");
#     g.addVertex("K");
# 
#     g.addEdge("A", "B", "E1");
# 
#     g.addEdge("B", "C", "E2");
#     g.addEdge("B", "D", "E3");
# 
#     g.addEdge("C", "A", "E4");
# 
#     g.addEdge("D", "E", "E5");
# 
#     g.addEdge("E", "F", "E6");
# 
#     g.addEdge("F", "D", "E7");
# 
#     g.addEdge("G", "F", "E8");
#     g.addEdge("G", "H", "E9");
# 
#     g.addEdge("H", "I", "E10");
# 
#     g.addEdge("I", "J", "E11");
# 
#     g.addEdge("J", "G", "E12");
#     g.addEdge("J", "K", "E13");

    g = DirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
    g.addVertex("V8");
    
    g.addEdge("V1", "V2", "E1");
    
    g.addEdge("V2", "V3", "E2");
    
    g.addEdge("V3", "V1", "E3");
    
    g.addEdge("V4", "V2", "E4");
    g.addEdge("V4", "V3", "E5");
    g.addEdge("V4", "V5", "E6");
    
    g.addEdge("V5", "V4", "E7");
    g.addEdge("V5", "V6", "E8");
    
    g.addEdge("V6", "V3", "E9");
    g.addEdge("V6", "V7", "E10");
    
    g.addEdge("V7", "V6", "E11");
    
    g.addEdge("V8", "V5", "E12");
    g.addEdge("V8", "V7", "E13");
    g.addEdge("V8", "V8", "E14");

    obj = SCC();
#     obj.kosarajusAlgo(g);
    obj.tarjansAlgo(g);
