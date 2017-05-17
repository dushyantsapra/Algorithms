'''
Created on Jul 9, 2016

@author: sapra
'''
from os.path import os


class UndirectedGraph:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount;
        self.edgeMap = {};
    
if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testcount = int(inputfile.readline().strip());
    for _ in range(testcount):
        vertexCount, edgeCount = list(map(int, inputfile.readline().strip().split(" ")));

        graph = UndirectedGraph(vertexCount);
    
        for _ in range(edgeCount):
            u, v = list(map(int, inputfile.readline().strip().split(" ")));
            if u not in graph.edgeMap:
                graph.edgeMap[u] = set()
    
            if v not in graph.edgeMap:
                graph.edgeMap[v] = set()

            graph.edgeMap[u].add(v)
            graph.edgeMap[v].add(u)

        sVertex = int(inputfile.readline().strip())

        if sVertex not in graph.edgeMap:
            dist = [1] * (vertexCount - 1)
            print(str(dist).replace('[', '').replace(']', '').replace(',', ''))
            continue

        l1 = {};
        for iLoop in range(1, vertexCount + 1):
            if iLoop == sVertex:
                continue
            l1[iLoop] = True;
    
        dist = {sVertex : 0}
        queue = [sVertex];
        visitedMap = {sVertex:True}
        while len(queue) > 0:
            vertex = queue.pop(0)
            l2 = {};
            if vertex in graph.edgeMap:
                for v in graph.edgeMap[vertex]:
                    if v not in visitedMap:
                        del l1[v]
                        l2[v] = True
    
            for v in l1.keys():        
                visitedMap[v] = True;
                queue.append(v);
                dist[v] = dist[vertex] + 1;
            
            l1 = l2;
        for iLoop in range(1, vertexCount + 1):
            if iLoop == sVertex:
                continue
            print(dist[iLoop], end=" ")
        print()
