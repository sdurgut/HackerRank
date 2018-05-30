import sys
from collections import defaultdict

def load_graph(stream):
    N, M = map(int, stream.readline().split())
    graph = defaultdict(list)
    for i in xrange(M):
        a, b = map(int, stream.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph, N

def calc_distances(graph, N, S):
    dists = defaultdict(lambda: -1)
    dists[S] = 0
    queue = [S]
    while queue:
        v = queue.pop(0)
        for neighbor in graph[v]:
            if dists[neighbor] < 0:
                queue.append(neighbor)
                dists[neighbor] = dists[v] + 6
    print " ".join(str(dists[n]) for n in xrange(1, N+1) if n != S)

if __name__ == '__main__':
    import sys
    T = int(sys.stdin.readline())
    for i in xrange(T):
        graph, N = load_graph(sys.stdin)
        S = int(sys.stdin.readline())
        calc_distances(graph, N, S)





# if __name__ == "__main__":
# 	# q = query
# 	# n = nodes
# 	# m = edges
# 	# u,v edge connects u and v
# 	# s = starting node
# 	q = int(input().strip())
# 	for a0 in range(q):
# 		n, m = input().strip().split(' ')
# 		n, m = [int(n), int(m)]
# 		edgeList = []
# 		for a1 in range(m):
# 			u, v = input().strip().split(' ')
# 			u, v = [int(u), int(v)]
# 			edgeList.append( (int(u),int(v)) )
# 		s = int(input().strip())
# 		myGraph = buildGraph(n,m,edgeList)


