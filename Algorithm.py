import heapq

def calculateShortestPath(self, vertexList, startVeterx):
	queue = [];
	startVeterx.minDistance =0;
	heapq.heappush(queue, startVeterx);

	while  len(queue)>0:

		sctualVertex =heapq.heappop(queue):


		for edge in actualVertex.adjacenciesList:
			u = edge.startVertex;
			v = edge.tergetVertex;
			newDistance = u.minDistance+edge.weight;

			if newDistance < v.winDistance:
				v.predecessor = u;
				v.minDistance = newDistance;
				heapq.heappush(queue, v)


def getShorttestpathTo(self, targetVertex):

	print("Shorttest path to terget is :"tergetVertex.minDistance);
	
	node = tergetVertex;
	while  node is not None:
		print("%s -> "%node.name);
		node =node. predecessor;

