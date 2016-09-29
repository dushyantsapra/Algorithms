'''
Created on Sep 19, 2016

@author: Dushyant Sapra
'''

from org.ds.graph.DFSApplicationUndirectedGraph import DFSApplicationUndirectedGraph
from org.ds.graph.DirectedGraph import DirectedGraph
from org.ds.graph.StronglyConnectedComponents import SCC
from org.ds.graph.UndirectedGraph import UnDirectedGraph


class Connectivity:

	def isEulerianForUndirectedGraphHelper(self, startVertex, visitedVertexMap):
		visitedVertexMap[startVertex] = True;

		for v in startVertex.getAdjacentVertex():
			if not visitedVertexMap[v]:
				self.isEulerianForUndirectedGraphHelper(v, visitedVertexMap);

	def isEulerianForUndirectedGraph(self, graph):
		visitedVertexMap = {};

		for v in graph.getVertexMap().itervalues():
			visitedVertexMap[v] = False;

		startVertex = None;
		for v in graph.getVertexMap().itervalues():
			if len(v.getAdjacentVertex()) > 0:
				startVertex = v;
				break;

		if startVertex:
# 			Checking For First Condition i.e Connectivity
			self.isEulerianForUndirectedGraphHelper(startVertex, visitedVertexMap);

			for v in graph.getVertexMap().itervalues():
				if len(v.getAdjacentVertex()) > 0 and not visitedVertexMap[v]:
					print("Graph not a Eulerian(Not Connected)");
					return False;

			oddVertexCount = 0;

			for v in graph.getVertexMap().itervalues():
				if len(v.getAdjacentVertex()) % 2 != 0:	
					oddVertexCount += 1;

			if oddVertexCount > 2:
				print("Graph not a Eulerian");
				return False;
			elif oddVertexCount == 0:
				print("Graph is Eulerian, Contains Eulerian Cycle");
				return True;
# 			We can't have one odd Number vertex, As Total Vertex Degree Count in Undirected Graph is Always Even
			elif oddVertexCount == 2: 
				print("Graph is Semi-Eulerian, Contains Eulerian Path");
				return True;
		else:
			print("Graph is Eulerian(No Edges Present");
			return True;

	def printEulerianPathOrCircuitHelper(self, graph, startVertex, oddVertexList, visitedEdgeMap, eulerianPath):
		eulerianPath.append(startVertex);
		
		for e in startVertex.getEdgeList():
			print

	def printEulerianPathOrCircuit(self, graph):

		startVertex = None;
		oddVertexList = [];
		if self.isEulerianForUndirectedGraph(graph):
			for v in graph.getVertexMap().itervalues():
				if len(v.getAdjacentVertex()) % 2 != 0:
					oddVertexList.append(v);

# 			For Eulerian Graph, We can have 0 or 2 odd Vertex.
			visitedEdgeMap = {};
			
			for e in graph.getEdgeMap().itervalues():
				visitedEdgeMap[e] = False;
			
			if len(oddVertexList) == 0:
				startVertex = graph.getVertexMap().values()[0];
			else:
				startVertex = oddVertexList[0];

	def isEulerianForDirectedGraph(self, graph):
		obj = SCC();

# 		Checking If all Vertices have Zero In and Out Degree.
		if len(graph.getEdgeMap()) == 0:
			print("Graph is Eulerian");
			return True;

		sccVertexMap = obj.kosarajusAlgo(graph, False);

		nonSingleVertexScc = 0;
		for valueStack in sccVertexMap.itervalues():
			if valueStack.getSize() > 1:
				nonSingleVertexScc += 1;

		if nonSingleVertexScc > 1:
			print("Graph is not eulerian");
		else:
			print("Graph is eulerian");

# 	Given an array of strings, find if the strings can be chained to form a circle
	def isStringListFormCycle(self, stringList):
		g = DirectedGraph();

		for index, item in enumerate(stringList):
			g.addEdge(item[0], item[len(item) - 1], "E" + str(index));

		if self.isEulerianForDirectedGraph(g):
			print("Given Array of String can be chained to form a circle");

			print("Chained Cycle would be : ");
		else:
			print("Given Array of String can't be chained to form a circle");

	def checkIfGraphIsBiconnected(self, graph):
		isBiconnected = True;
		cutVertexList = DFSApplicationUndirectedGraph().checkForArticulationPointInGraph(graph, False);
		if len(cutVertexList) == 0:
			visitedVertexMap = graph.dfsUsingRecursion(graph.getVertexMap().keys()[1], False);
			if len(visitedVertexMap) != len(graph.getVertexMap()):
				isBiconnected = False;
			else:
				isBiconnected = False;

		if isBiconnected:
			print("Graph is Biconnected");
		else:
			print("Graph Contains Articulation point OR all Graph is not connected");

if __name__ == '__main__':
	g = UnDirectedGraph()
	g.addVertex("V0");
	g.addVertex("V1");
	g.addVertex("V2");
	g.addVertex("V3");
	g.addVertex("V4");
	
	g.addEdge("V0", "V1", "E1");
	g.addEdge("V0", "V2", "E2");
	g.addEdge("V0", "V3", "E3");
	
	g.addEdge("V2", "V1", "E4");
	g.addEdge("V3", "V4", "E5");
	
	g.addEdge("V4", "V0", "E6");
	
	obj = Connectivity();
	obj.isEulerianForUndirectedGraph(g);
	
	g = DirectedGraph()
	g.addVertex("V0");
	g.addVertex("V1");
	g.addVertex("V2");
	g.addVertex("V3");
	g.addVertex("V4");
	
	g.addEdge("V0", "V1", "E1");
	g.addEdge("V0", "V3", "E2");

	g.addEdge("V1", "V2", "E3");
	g.addEdge("V2", "V0", "E4");

	g.addEdge("V3", "V4", "E5");

	g.addEdge("V4", "V0", "E6");

	obj = Connectivity();
	obj.isEulerianForDirectedGraph(g);
	
	obj = Connectivity();
# 	obj.isStringListFormCycle(["for", "geek", "rig", "kaf"]);
# 	obj.isStringListFormCycle(["aaa"]);
	obj.isStringListFormCycle(["aaa", "bbb"]);
	

	g = UnDirectedGraph();
	g.addVertex("V1");
	g.addVertex("V2");
	g.addVertex("V3");
	g.addVertex("V4");
	g.addVertex("V5");

	g.addEdge("V1", "V2", "E1");
	g.addEdge("V1", "V5", "E2");

	g.addEdge("V2", "V3", "E3");
	g.addEdge("V2", "V5", "E4");

	g.addEdge("V3", "V4", "E5");
	
	g.addEdge("V4", "V5", "E6");
	
	print("\n");
	obj = Connectivity();
	obj.checkIfGraphIsBiconnected(g);