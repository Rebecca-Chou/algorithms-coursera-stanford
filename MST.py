#read files
fh = open("edges.txt","r")
lon = fh.readlines()
graph = [{} for i in range(501)]
for line in lon[1:]:
    node1 = int(line.split()[0])
    node2 = int(line.split()[1])
    weight = int(line.split()[2])
    graph[node1][node2] = weight
    graph[node2][node1] = weight

#Prim's algo
X = [1]
T = 0
H = list(range(2,501))
while H:
    new_node = 0
    min_weight = 0
    for node_explored in X:
        for edge in graph[node_explored]:
            if edge in H:
                if new_node == 0 or graph[node_explored][edge] < min_weight:
                    new_node = edge
                    min_weight = graph[node_explored][edge]
    X += [new_node]
    T += min_weight
    H.remove(new_node)

print(T)
