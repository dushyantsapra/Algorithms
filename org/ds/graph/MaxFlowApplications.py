'''
Created on Sep 13, 2016

@author: Dushyant Sapra
'''

from org.ds.graph.MaximumFlow import MaximumFlow
from org.ds.graph.GraphMatrixImplementation import GraphMatrixImplementation

class MaxFlowApplication:
    def countDisjointPathsUsingAdjMatrixGraph(self, graph, sourceVertexName, sinkVertexName):
        maxFlowObj = MaximumFlow();

        disjointPathCount, pathMap, residualGraph = maxFlowObj.fordFulkersonAlgoUsingAdjMatrixAndBFS(graph, sourceVertexName, sinkVertexName, False);

        print("Disjoint Path For Given Graph is : " + str(disjointPathCount));

        for key, stack in pathMap.iteritems():
            print("Disjoint Path : " + str(key + 1));

            while stack.getSize() > 0:
                print(stack.pop());

    def findMinCutHelper(self, residualGraph, index, visitedVertexList):
#         print(residualGraph.getIndexVertexMap()[index]);

        visitedVertexList[index] = True;

        for iLoop in range(residualGraph.getVertexCount()):
            if (residualGraph.getGraphWeightMatrix()[index][iLoop] > 0) and not visitedVertexList[iLoop]:
                self.findMinCutHelper(residualGraph, iLoop, visitedVertexList);

    def findMinCut(self, graph, sourceVertexName, sinkVertexName):
        maxFlowObj = MaximumFlow();

        maxFlow, pathMap, residualGraph = maxFlowObj.fordFulkersonAlgoUsingAdjMatrixAndBFS(graph, sourceVertexName, sinkVertexName, False);

        visitedVertexList = [False] * (graph.getVertexCount());
        self.findMinCutHelper(residualGraph, graph.getVertexIndexMap()[sourceVertexName], visitedVertexList);
 
        if maxFlow > 0:
            print("Min Cut in Given Graph is : ");
            for iLoop in range(residualGraph.getVertexCount()):
                for jLoop in range(residualGraph.getVertexCount()):
                    if visitedVertexList[iLoop] and not visitedVertexList[jLoop] and graph.getGraphMatrix()[iLoop][jLoop] == 1:
                        print("From Vertex : " + graph.getIndexVertexMap()[iLoop] + ", To Vertex : " + graph.getIndexVertexMap()[jLoop] + ", with Weight : " + str(graph.getGraphWeightMatrix()[iLoop][jLoop]));
        else:
            print("No Min Cut Present");

    
    def maximumBipartiteMappingUsingDFSHelper(self, graph, iIndex, mbmMap):
        print()
            
#     Also Known ad Kho Kho Approach
#     Example Would be of Applicants and Jobs
    def maximumBipartiteMappingUsingDFS(self, graph):
        mbmMap = {};
        for iIndex in range(graph.getVertexCount()):
            self.maximumBipartiteMappingUsingDFSHelper(graph, iIndex, mbmMap);

if __name__ == '__main__':
    g = GraphMatrixImplementation(8);
 
    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
 
    g.addEdge("V0", "V1", 1);
    g.addEdge("V0", "V2", 1);
    g.addEdge("V0", "V3", 1);
 
    g.addEdge("V1", "V2", 1);
 
    g.addEdge("V2", "V3", 1);
    g.addEdge("V2", "V6", 1);
 
    g.addEdge("V3", "V6", 1);
 
    g.addEdge("V4", "V2", 1);
    g.addEdge("V4", "V7", 1);
 
    g.addEdge("V5", "V1", 1);
    g.addEdge("V5", "V4", 1);
    g.addEdge("V5", "V7", 1);
 
    g.addEdge("V6", "V5", 1);
    g.addEdge("V6", "V7", 1);
 
    obj = MaxFlowApplication();
    obj.countDisjointPathsUsingAdjMatrixGraph(g, "V0", "V7");
    
    
    g = GraphMatrixImplementation(6);

    g.addVertex("V0");
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");

    g.addEdge("V0", "V1", 16);
    g.addEdge("V0", "V2", 13);

    g.addEdge("V1", "V2", 10);
    g.addEdge("V1", "V3", 12);

    g.addEdge("V2", "V1", 4);
    g.addEdge("V2", "V4", 14);
    
    g.addEdge("V3", "V2", 9);
    g.addEdge("V3", "V5", 20);
    
    g.addEdge("V4", "V3", 7);
    g.addEdge("V4", "V5", 4);

    obj = MaxFlowApplication();
    obj.findMinCut(g, "V0", "V5");


    g = GraphMatrixImplementation(9);
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
    g.addVertex("V8");
    g.addVertex("V9");

    g.addEdge("V1", "V6", 1);
    g.addEdge("V1", "V7", 1);

    g.addEdge("V2", "V6", 1);

    g.addEdge("V3", "V7", 1);
    g.addEdge("V3", "V9", 1);

    g.addEdge("V4", "V7", 1);

    g.addEdge("V5", "V8", 1);
    g.addEdge("V5", "V9", 1);