class Graph:
	def __init__ (self, size):
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g) :
	print(' ', end = ' ')
	for v in range(len(g.graph)) :
		print(name_ary[v], end =' ')
	print()
	for row in range(len(g.graph)) :
		print(name_ary[row], end =' ')
		for col in range(len(g.graph)) :
			print(f"{g.graph[row][col]:2d}", end=' ')
		print()
	print()

def find_vertex(g, find_vtx) :
	stack = list()
	visited_ary = list()

	i = 0
	stack.append(i)
	visited_ary.append(i)

	while stack:
		next = None
		for j in range(graph_size):
			if g.graph[i][j] != 0:
				if j in visited_ary:
					pass
				else:
					next = j
					break

		if next is not None:
			i = next
			stack.append(i)
			visited_ary.append(i)
		else:
			i = stack.pop()

	if find_vtx in visited_ary:
		return True
	else :
		return False


g1 = None
name_ary = ['인천', '서울', '강릉', '대전', '광주', '부산']
incheon, seoul, gangneung, daejeon, gwangju, busan = 0, 1, 2, 3, 4, 5


graph_size = 6
g1 = Graph(graph_size)
g1.graph[incheon][seoul] = 10; g1.graph[incheon][gangneung] = 15
g1.graph[seoul][incheon] = 10; g1.graph[seoul][gangneung] = 40; g1.graph[seoul][daejeon] = 11; g1.graph[seoul][gwangju] = 55
g1.graph[gangneung][incheon] = 15; g1.graph[gangneung][seoul] = 40; g1.graph[gangneung][daejeon] = 12
g1.graph[daejeon][seoul] = 11; g1.graph[daejeon][gangneung] = 12; g1.graph[daejeon][gwangju] = 20; g1.graph[daejeon][busan] = 30
g1.graph[gwangju][seoul] = 55; g1.graph[gwangju][daejeon] = 20; g1.graph[gwangju][busan] = 28
g1.graph[busan][daejeon] = 30; g1.graph[busan][gwangju] = 28

print('도시 간 도로 건설을 위한 전체 연결도')
print_graph(g1)

edge_ary = list()
for i in range(graph_size) :
	for k in range(graph_size) :
		if g1.graph[i][k] != 0 :
			edge_ary.append([g1.graph[i][k], i, k])
print(edge_ary)

edge_ary.sort(reverse=True)
print(edge_ary)

new_ary = list()
for i in range(1, len(edge_ary), 2):
	new_ary.append(edge_ary[i])
print(new_ary)

index = 0
while len(new_ary) > graph_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복
	start = new_ary[index][1]
	end = new_ary[index][2]
	save_cost = new_ary[index][0]

	g1.graph[start][end] = 0
	g1.graph[end][start] = 0

	start_reachable = find_vertex(g1, start)
	end_reachable = find_vertex(g1, end)

	if start_reachable and end_reachable :
		del new_ary[index]
	else:
		g1.graph[start][end] = save_cost
		g1.graph[end][start] = save_cost
		index = index + 1

print('최소 비용의 도로 연결도')
print_graph(g1)

total_cost = 0
for i in range(graph_size):
	for k in range(graph_size):
		if g1.graph[i][k] != 0:
			total_cost = total_cost + g1.graph[i][k]

total_cost = total_cost // 2
print(f"최소 비용의 도로 건설 비용 :  {total_cost}")