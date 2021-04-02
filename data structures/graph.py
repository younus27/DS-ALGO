from collections import defaultdict
class Graph:
	def __init__(self): 
		self.graph = defaultdict(list) 

	def addEdge(self,u,v):
		self.graph[u].append(v)
	def get_vertices(self):
		return list(self.graph.keys())

	def find_edges(self):
		edge_name =[]
		for key,value in dict(self.graph).items():
			for item in value:
				if (key,item) not in edge_name:
					edge_name.append((key,item))
		return edge_name

	def display(self):
		print(dict(self.graph))


	def dfs_helper(self,v,visited):
		visited[v]= True
		print(v,end=" ")
		for i in self.graph[v]:
			if visited[i] == False:
				self.dfs_helper(i,visited)
	def dfs(self,v):
		visited = [False]*(len(self.graph))
		self.dfs_helper(v,visited)


	def bfs(self,s):
		visited = [False] * (len(self.graph)) 

		queue=[]

		queue.append(s)
		visited[s] = True

		while queue:
			s= queue.pop(0)
			print (s, end = " ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

# Create the dictionary with graph elements

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0)
g.addEdge(2, 3) 
g.addEdge(3, 3) 

# g = graph()
# print(g.find_edges())
g.dfs(2)