graph = {'A': set(['B', 'C']),
		'B': set(['A', 'D', 'E']),
		'C': set(['A', 'F']),
		'D': set(['B']),
		'E': set(['B', 'F']),
		'F': set(['C', 'E'])}

def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

# def dfs(graph, start, visited=None):
# 	if visited is None:
# 		visited = set()
# 	visited.add(start)
# 	for next in graph[start] - visited:
# 		dfs(graph, next, visited)
# 	return visited

def bfs(graph, start):
	visited, queue = set(), [start]
	print("QUEUE = ", queue,"  Visited = ",visited)
	while queue:
		vertex = queue.pop(0)
		
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
		print("QUEUE = ", queue,"  Visited = ",visited)
	return visited

print ("####DFS####")
print(dfs(graph, 'A'))
print ("####BFS####")
print(bfs(graph, 'A'))