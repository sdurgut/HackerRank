import collections

def breadth_first_search(graph, root): 
	visited, queue = set(), collections.deque([root])
	print (queue)
	while queue:
		print (queue)
		vertex = queue.popleft()
		for neighbour in graph[vertex]: 
			if neighbour not in visited: 
				visited.add(neighbour) 
				queue.append(neighbour) 


if __name__ == '__main__':
	graph = {0: [1, 2], 1: [2], 2: []} 
	breadth_first_search(graph, 0)



