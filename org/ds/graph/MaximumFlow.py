'''
Created on Sep 13, 2016

@author: Dushyant Sapra
'''

from copy import deepcopy

from org.ds.graph.GraphMatrixImplementation import GraphMatrixImplementation
from org.ds.queue.Queue import Queue
from org.ds.stack.Stack import StackUsingLinkedList


class MaximumFlow:
    def fordFulkersonAlgoUsingAdjList(self, graph, sourceVertex, sinkVertex):
        print()

#     Using BFS
    def fordFulkersonAlgoUsingAdjMatrixAndBFSHelper(self, residualGraph, sourceVertexIndex, sinkVertexIndex, parentVertexMap):
        queue = Queue();

        visitedVertexIndexMap = {};

        visitedVertexIndexMap[sourceVertexIndex] = True;
        parentVertexMap[sourceVertexIndex] = -1;

        queue.enQueue(sourceVertexIndex);

        while queue.getSize() > 0:
            iVertex = queue.deQueue();

            for jVertex in range(residualGraph.getVertexCount()):
                if residualGraph.getGraphWeightMatrix()[iVertex][jVertex] > 0 and (jVertex not in visitedVertexIndexMap or not visitedVertexIndexMap[jVertex]):
                    queue.enQueue(jVertex);
                    visitedVertexIndexMap[jVertex] = True;
                    parentVertexMap[jVertex] = iVertex;

                    if jVertex == sinkVertexIndex:
                        return True;
        return False;

    def fordFulkersonAlgoUsingAdjMatrixAndBFS(self, graph, sourceVertexName, sinkVertexName, isPrint=True):
        residualGraph = deepcopy(graph);

        maxFlow = 0;

        sourceVertexIndex = graph.getVertexIndexMap()[sourceVertexName];
        sinkVertexIndex = graph.getVertexIndexMap()[sinkVertexName];

        maxFlowPathStackMap = {};

        parentVertexMap = {};
        parentVertexMap[sourceVertexIndex] = -1;
        while(self.fordFulkersonAlgoUsingAdjMatrixAndBFSHelper(residualGraph, sourceVertexIndex, sinkVertexIndex, parentVertexMap)):
            minFlow = float("inf");
            parentVertexIndex = parentVertexMap[sinkVertexIndex];
            childVertexIndex = sinkVertexIndex;

            pathStack = StackUsingLinkedList();
            pathStack.push(sinkVertexIndex);
            while parentVertexIndex != -1:
                minFlow = min(residualGraph.getGraphWeightMatrix()[parentVertexIndex][childVertexIndex], minFlow);

                pathStack.push(parentVertexIndex);

                childVertexIndex = parentVertexIndex;
                parentVertexIndex = parentVertexMap[parentVertexIndex];

            maxFlow += minFlow;
            maxFlowPathStackMap[len(maxFlowPathStackMap)] = pathStack;

            parentVertexIndex = parentVertexMap[sinkVertexIndex];
            childVertexIndex = sinkVertexIndex;
            while parentVertexIndex != -1:
                residualGraph.getGraphWeightMatrix()[parentVertexIndex][childVertexIndex] -= minFlow;
                residualGraph.getGraphWeightMatrix()[childVertexIndex][parentVertexIndex] += minFlow;

                childVertexIndex = parentVertexIndex;
                parentVertexIndex = parentVertexMap[parentVertexIndex];

            parentVertexMap = {};
            parentVertexMap[sourceVertexIndex] = -1;

        if isPrint:
            print("Max Flow From Given Graph is : " + str(maxFlow));

            for key, stack in maxFlowPathStackMap.items():
                print("Max Flow Path : " + str(key + 1));

                while stack.getSize() > 0:
                    print(stack.pop());

        return maxFlow, maxFlowPathStackMap, residualGraph;

if __name__ == '__main__':
    g = GraphMatrixImplementation(7);

#     Example From Topcoder
    g.addVertex("X0");
    g.addVertex("A1");
    g.addVertex("B2");
    g.addVertex("C3");
    g.addVertex("D4");
    g.addVertex("E5");
    g.addVertex("Y6");

    g.addEdge("X0", "A1", 3);
    g.addEdge("X0", "B2", 1);
    
    g.addEdge("A1", "C3", 3);
    
    g.addEdge("B2", "C3", 5);
    g.addEdge("B2", "D4", 4);
    
    g.addEdge("C3", "Y6", 2);

    g.addEdge("D4", "E5", 2);
    
    g.addEdge("E5", "Y6", 3);
    
    obj = MaximumFlow();
    
    obj.fordFulkersonAlgoUsingAdjMatrixAndBFS(g, "X0", "Y6");
