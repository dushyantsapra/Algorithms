'''
Created on Aug 17, 2016

@author: Dushyant Sapra
'''
# For Undirected Graph Only


from org.ds.graph.UndirectedGraph import UnDirectedGraph
from org.ds.queue.Queue import Queue

class BFSApplication:
#     Logic
#     G is bipartite if and only if a partition of V(vertices) into U and W such that V=U union W and U intersection W is Null. i.e every edge has one end point in U and the other in W.
#     Logic: Start a BFS starting from any arbitrary vertex, If there is an edge from with in the same level then G is not bipartite.
#     Assumption: suppose graph is a connected graph having connected component count 1.
#     Proof: Do BFS and store Level Number with Every Vertex and check if both the end point of a edge have same Level, then G is not bipartite.
    
#     Logic For Assigning Level number to every Vertex: Every Direct Child Vertex from Parent have 1 large level to parent vertex
    def checkIfGraphIsBipartite(self, graph):
        vertex = graph.getVertexMap().values()[0];

        queue = Queue();
        vertexLevelMap = {};

        queue.enQueue(vertex);
        vertexLevelMap[vertex] = 1;

        while queue.getSize() > 0:
            v = queue.deQueue();
            print(v.getName());

            if len(v.getAdjacentVertex()) > 0:
                for tempVertex in v.getAdjacentVertex():
                    if tempVertex in vertexLevelMap:
                        continue;

                    vertexLevelMap[tempVertex] = vertexLevelMap[v] + 1;
                    queue.enQueue(tempVertex);

                for edge in v.getEdgeList():
                    if edge.getFromVertex() not in vertexLevelMap or edge.getToVertex() not in vertexLevelMap:
                        continue;

                    if vertexLevelMap[edge.getFromVertex()] == vertexLevelMap[edge.getToVertex()]:
                        print("Graph has a Cycle having odd number of edges OR edge in same Level");
                        print("From Vertex " + edge.getFromVertex().getName() + " To Vertex " + edge.getToVertex().getName()); 
                        return;

#     Logic: Do BFS From any arbitrary vertex, if BFS visits all the vertices then G(V, E) is connected
    def checkIfGraphIsConnected(self, graph):
        visitedVertexMap = {};
        graph.bfs(graph.getVertexMap().keys()[0], visitedVertexMap);

        if len(visitedVertexMap) == len(graph.getVertexMap()):
            print("Graph is Connected");
        else:
            print("Graph is Not Connected");

    def countAndPrintconnectedComponents(self, graph):
        visitedVertexMap = {};
        counter = 0;
        for key, value in graph.vertexMap.iteritems():
            visitedVertexMap[value] = 0;

        for key, value in visitedVertexMap.iteritems():
            if value == 0:
                counter += 1;
                print("Connected Component Number " + str(counter) + " Vertices are:");
#                 graph.bfs(key.getName(), visitedVertexMap);
                graph.dfsUsingStack(key.getName(), visitedVertexMap);
            else:
                continue;

        print("Total Connected Components are : %d", counter);

if __name__ == '__main__':
    """# Test Case 2, Check if Graph is Bipartite
    g = UnDirectedGraph();
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
    
    obj = BFSApplication();
    obj.checkIfGraphIsBipartite(g);"""
    
    """# Test Case 2, Checking For Connected Component's in a graph
    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");
    g.addVertex("V4");
    g.addVertex("V5");
    g.addVertex("V6");
    g.addVertex("V7");
    g.addVertex("V8");
    g.addVertex("V9");
    g.addVertex("V10");
    g.addVertex("V11");
    g.addVertex("V12");
    g.addVertex("V13");
    g.addVertex("V14");
    
    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V5", "E2");
    g.addEdge("V2", "V3", "E3");
    g.addEdge("V3", "V4", "E4");
    g.addEdge("V4", "V5", "E5");
    
    g.addEdge("V6", "V7", "E6");
    g.addEdge("V6", "V8", "E7");
    g.addEdge("V7", "V8", "E8");
    
    g.addEdge("V9", "V10", "E9");
    g.addEdge("V9", "V12", "E10");
    g.addEdge("V10", "V11", "E11");
    g.addEdge("V11", "V12", "E12");
    
    obj = BFSApplication();
    obj.countAndPrintconnectedComponents(g);"""
    
#     Test Case 3, Check If Graph is connected
    g = UnDirectedGraph();
    g.addVertex("V1");
    g.addVertex("V2");
    g.addVertex("V3");


    g.addEdge("V1", "V2", "E1");
    g.addEdge("V1", "V2", "E2");
    g.addEdge("V2", "V3", "E3");
    
    obj = BFSApplication();
    obj.checkIfGraphIsConnected(g);