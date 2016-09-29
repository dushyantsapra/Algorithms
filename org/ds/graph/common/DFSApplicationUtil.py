'''
Created on Aug 22, 2016

@author: Dushyant Sapra
'''

class DFSApplicationUtil:

    @staticmethod
    def checkIfGraphIs2EdgeConnectedHelper(isDirectedGraph, parentVertex, vertex, arrivalMap, departureMap, bridgeEdgeMap, visitedVertexMap=None, currentCount=0):
        if visitedVertexMap is None:
            visitedVertexMap = {};

        visitedVertexMap[vertex] = 1;
        currentCount += 1;
        arrivalMap[vertex] = currentCount;

        minArrivalTime = currentCount;

#         print("Vertex Name: " + vertex.getName() + ", Arrival Time: " + str(currentCount));

        if isDirectedGraph:
            for tempVertex in vertex.getOutVerticesList():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                    if tempVertex is not parentVertex:
                        minArrivalTime = arrivalMap[tempVertex] if arrivalMap[tempVertex] < minArrivalTime else minArrivalTime;
                    continue;

                currentCount, tempMinArrivalTime = DFSApplicationUtil.checkIfGraphIs2EdgeConnectedHelper(isDirectedGraph, vertex, tempVertex, arrivalMap, departureMap, bridgeEdgeMap, visitedVertexMap, currentCount);
                minArrivalTime = tempMinArrivalTime if tempMinArrivalTime < minArrivalTime else minArrivalTime;
        else:
            for tempVertex in vertex.getAdjacentVertex():
                if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] > 0:
                    if tempVertex != parentVertex:
                        minArrivalTime = arrivalMap[tempVertex] if arrivalMap[tempVertex] < minArrivalTime else minArrivalTime;
                    continue;
    
                currentCount, tempMinArrivalTime = DFSApplicationUtil.checkIfGraphIs2EdgeConnectedHelper(isDirectedGraph, vertex, tempVertex, arrivalMap, departureMap, bridgeEdgeMap, visitedVertexMap, currentCount);
                minArrivalTime = tempMinArrivalTime if tempMinArrivalTime < minArrivalTime else minArrivalTime;
        currentCount += 1;
        departureMap[vertex] = currentCount;
#         print("Vertex Name: " + vertex.getName() + ", Departure Time: " + str(currentCount));

#         Condition: parentVertex != vertex, TO Check if the processed vertex is not a start Vertex. Same can be checked as "arrivalMap[vertex] != 1"
        if minArrivalTime >= arrivalMap[vertex] and parentVertex != vertex:
            bridgeEdgeMap[parentVertex] = vertex;
        return currentCount, minArrivalTime;

    @staticmethod
    def checkForArticulationPointInGraphHelper(parentVertex, vertex, arrivalMap, departureMap, cutVertexList, visitedVertexMap=None, currentCount=0):
        if visitedVertexMap is None:
            visitedVertexMap = {};

        childrenCount = 0;

        visitedVertexMap[vertex] = True;
        currentCount += 1;
        arrivalMap[vertex] = currentCount;

        minArrivalTime = currentCount;
        
        backEdgeVertexArrivalTime = currentCount;

#         print("Vertex Name: " + vertex.getName() + ", Arrival Time: " + str(currentCount));

        for tempVertex in vertex.getAdjacentVertex():
            if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex]:
                if tempVertex is not parentVertex:
                    backEdgeVertexArrivalTime = arrivalMap[tempVertex] if arrivalMap[tempVertex] < backEdgeVertexArrivalTime else backEdgeVertexArrivalTime;
                continue;

            childrenCount += 1;
            currentCount, tempMinArrivalTime = DFSApplicationUtil.checkForArticulationPointInGraphHelper(vertex, tempVertex, arrivalMap, departureMap, cutVertexList, visitedVertexMap, currentCount);
            minArrivalTime = tempMinArrivalTime if tempMinArrivalTime < minArrivalTime else minArrivalTime;
        currentCount += 1;
        departureMap[vertex] = currentCount;
#         print("Vertex Name: " + vertex.getName() + ", Departure Time: " + str(currentCount));
        
        if vertex != parentVertex:
            if childrenCount > 1:
                cutVertexList.append(vertex);
            if minArrivalTime >= arrivalMap[vertex] and childrenCount == 1:
                cutVertexList.append(vertex);
        return currentCount, minArrivalTime if minArrivalTime < backEdgeVertexArrivalTime else backEdgeVertexArrivalTime;

    @staticmethod
    def checkForCycleInGraphUsingDFSHelper(vertex, parentVertex, visitedVertexMap=None):
        if visitedVertexMap is None:
            visitedVertexMap = {};

        visitedVertexMap[vertex] = 1;

        for tempVertex in vertex.getAdjacentVertex():
            if tempVertex in visitedVertexMap and visitedVertexMap[tempVertex] == 0:
                if (DFSApplicationUtil.checkForCycleInGraphUsingDFSHelper(tempVertex, vertex, visitedVertexMap)):
                    return True;
            elif tempVertex in visitedVertexMap and tempVertex is not parentVertex:
                return True;

        return False;

    @staticmethod
    def checkForCycleInDirectedGraphHelper(vertex, stack, visitedVertexMap):
        if visitedVertexMap is None:
            visitedVertexMap = {};

        visitedVertexMap[vertex] = 1;
        stack.push(vertex)
        for tempVertex in vertex.getOutVerticesList():
            if visitedVertexMap[tempVertex] == 0:
                if (DFSApplicationUtil.checkForCycleInDirectedGraphHelper(tempVertex, stack, visitedVertexMap)):
                    return True;
            elif visitedVertexMap[tempVertex] == 1 and stack.contains(tempVertex):
                return True;
        stack.pop();
        return False;
    
    @staticmethod
    def stronglyConnectedCommponentUsingKosarajusAlgoHelper(vertex, visitedVertexMap, isReversed, stack=None):
        visitedVertexMap[vertex] = True;

        if not isReversed:
            for tempVertex in vertex.getOutVerticesList():
                if visitedVertexMap[tempVertex]:
                    continue;
                DFSApplicationUtil.stronglyConnectedCommponentUsingKosarajusAlgoHelper(tempVertex, visitedVertexMap, isReversed, stack);
            stack.push(vertex);
        else:
            for tempVertex in vertex.getInVerticesList():
                if visitedVertexMap[tempVertex]:
                    continue;

                stack.push(tempVertex);
                DFSApplicationUtil.stronglyConnectedCommponentUsingKosarajusAlgoHelper(tempVertex, visitedVertexMap, isReversed, stack);

    @staticmethod
    def stronglyConnectedCommponentUsingTarjansAlgoHelper(vertex, stackVertexMap, arrivalTimeMap, lowTimeMap, sccStack, currentCount=1):
        stackVertexMap[vertex] = True;
        sccStack.push(vertex);

        arrivalTimeMap[vertex] = currentCount;
        lowTimeMap[vertex] = currentCount;

        currentCount += 1;

        for tempVertex in vertex.getOutVerticesList():
            if arrivalTimeMap[tempVertex] == -1:
                DFSApplicationUtil.stronglyConnectedCommponentUsingTarjansAlgoHelper(tempVertex, stackVertexMap, arrivalTimeMap, lowTimeMap, sccStack, currentCount);
                lowTimeMap[vertex] = lowTimeMap[tempVertex] if lowTimeMap[tempVertex] < lowTimeMap[vertex] else lowTimeMap[vertex];
            elif stackVertexMap[tempVertex]:
                lowTimeMap[vertex] = lowTimeMap[tempVertex] if lowTimeMap[tempVertex] < arrivalTimeMap[vertex] else arrivalTimeMap[tempVertex];

        if lowTimeMap[vertex] == arrivalTimeMap[vertex]:
            print("\n");
            while sccStack.getSize() > 0:
                tempVertex = sccStack.pop();
                print(tempVertex);
                stackVertexMap[tempVertex] = False;
                if tempVertex == vertex:
                    break;

    @staticmethod
    def checkForCycleInGraphUsingVertexColorHelper(vertex, parentVertex, visitedVertexColorMap):
        visitedVertexColorMap[vertex] = "GREY";
        print(vertex);
        for tempVertex in vertex.getAdjacentVertex():
            if visitedVertexColorMap[tempVertex] is "WHITE":
                if DFSApplicationUtil.checkForCycleInGraphUsingVertexColorHelper(tempVertex, vertex, visitedVertexColorMap):
                    return True;
            if visitedVertexColorMap[tempVertex] is "GREY" and tempVertex != parentVertex:
                return True;

        visitedVertexColorMap[vertex] = "BLACK";
    
    @staticmethod
    def topologicalSortUsingDFSHelper(vertex, visitedVertexMap, stack):
        visitedVertexMap[vertex] = True;

        for tempVertex in vertex.getOutVerticesList():
            if visitedVertexMap[tempVertex] == True:
                continue;

            DFSApplicationUtil.topologicalSortUsingDFSHelper(tempVertex, visitedVertexMap, stack);

        stack.push(vertex);
