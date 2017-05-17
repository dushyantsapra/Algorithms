'''
Created on Apr 26, 2017

@author: xdussap
'''
from _datetime import datetime
from os.path import os


def computeHCF(x, y):
    hcf = 0;
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

class UnDirectedGraph:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount;
        self.vertexMap = [[] for _ in range(vertexCount + 1)];

    def bfs(self, currentrootvertex, choiceMap):
        undiscoveredvertexqueue = [currentrootvertex];

        visitedVertexMap = {};
        visitedVertexMap[currentrootvertex] = True;

        totalTrueguesses = 0;
        while len(undiscoveredvertexqueue) > 0:
            currentrootvertex = undiscoveredvertexqueue.pop(0);
            flag = False;
            if currentrootvertex in choiceMap:
                flag = True;
            for cvertex in self.vertexMap[currentrootvertex]:
                if cvertex in visitedVertexMap:
                    continue;

                if flag:
                    if cvertex in choiceMap[currentrootvertex]:
                        totalTrueguesses += 1;

                undiscoveredvertexqueue.append(cvertex)

                visitedVertexMap[cvertex] = True;

        return totalTrueguesses;

class Vertex:
    def __init__(self, value):
        self.value = value;
        self.parent = value;

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.value;

    def __str__(self):
        return "Vertex : {}, Parent : {}".format(self.value, self.parent);

    def setParent(self, parent):
        self.parent = parent;

    def getParent(self):
        return self.parent;

def calculatecorrectGuesse(vertexMap, choiceMap):
    correctGuessecount = 0;
    for vertexName, vertex in choiceMap.items():
        if vertexName in vertexMap:
            v1 = vertexMap[vertexName];
            p1 = v1.getParent();
            
            p2 = vertex.getParent();
            
            if p1 == p2:
                correctGuessecount += 1;
    return correctGuessecount

def rearrangeVertexMap(vertexMap, vertexName, parentName):
    vertex = vertexMap[vertexName]
    
    if vertex.getParent() == vertexName:
        vertex.setParent(parentName);
        return;
    
    currentParent = vertex.getParent();
    vertex.setParent(parentName);
    
    rearrangeVertexMap(vertexMap, currentParent, vertexName);

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testCount = int(inputfile.readline().strip());

    for _ in range(testCount):
        vertexCount = int(inputfile.readline().strip());
        
        vertexMap = {};
        for vertexName in range(1, vertexCount + 1):
            vertexMap[vertexName] = Vertex(vertexName);

        print(datetime.now());
        graph = UnDirectedGraph(vertexCount);

        for _ in range(vertexCount - 1):
            v1, v2 = list(map(int, inputfile.readline().strip().split(" ")));
            v1, v2 = (v1, v2) if v1 < v2 else (v2, v1);

            vertex = vertexMap[v2];
            vertex.setParent(v1);

#         print(vertexMap)

        g, k = list(map(int, inputfile.readline().strip().split(" ")));

        choiceMap = {};
        for _ in range(g):
            v1, v2 = list(map(int, inputfile.readline().strip().split(" ")));
            vertex = Vertex(v2);
            vertex.setParent(v1);
            choiceMap[v2] = vertex;

        print(datetime.now());

        totalcorrectGuessecount = 0;
        correctGuessecount = calculatecorrectGuesse(vertexMap, choiceMap);
        if correctGuessecount >= k:
            totalcorrectGuessecount += 1;
        
        print(datetime.now());

        for cvertex in range(2, vertexCount + 1):
            rearrangeVertexMap(vertexMap, cvertex, cvertex);
            
            correctGuessecount = calculatecorrectGuesse(vertexMap, choiceMap);
            if correctGuessecount >= k:
                totalcorrectGuessecount += 1;
        
        print(datetime.now());
        print(totalcorrectGuessecount)
    
        if totalcorrectGuessecount == 0:
            vertexCount = 1;
        else:
            hcf = computeHCF(totalcorrectGuessecount, vertexCount)
             
            while hcf > 1:
                totalcorrectGuessecount = int(totalcorrectGuessecount / hcf);
                vertexCount = int(vertexCount / hcf); 
                hcf = computeHCF(totalcorrectGuessecount, vertexCount)
         
        print("{}/{}".format(totalcorrectGuessecount, vertexCount))
            
        
#         print(choiceMap)

#         trueguessesNodesize = 0;
#         print("1 {} ".format(datetime.now()));
#         for cvertex in range(1, vertexCount + 1):
#             trueguesses = graph.bfs(cvertex, choiceMap);
#             if trueguesses >= k:
#                 trueguessesNodesize += 1;
#         print("2 {} ".format(datetime.now()));
# #         print(trueguessesNodesize)
# 
#         if trueguessesNodesize == 0:
#             trueguessesNodesize = 0;
#             vertexCount = 1;
#         else:
#             hcf = computeHCF(trueguessesNodesize, vertexCount)
#             
#             while hcf > 1:
#                 trueguessesNodesize = int(trueguessesNodesize / hcf);
#                 vertexCount = int(vertexCount / hcf); 
#                 hcf = computeHCF(trueguessesNodesize, vertexCount)
#         
#         print("{}/{}".format(trueguessesNodesize, vertexCount))



