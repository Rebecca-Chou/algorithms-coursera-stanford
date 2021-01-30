#initialize variables
num_nodes = 875714
graph = [[] for i in range(num_nodes+1)]
graph_rev = [[] for i in range(num_nodes+1)]

#read the file and assign values to graph
f = open("SCC.txt","r")
lines = f.readlines()
f.close()
for l in lines:
    node1 = int(l.split()[0])
    node2 = int(l.split()[1])
    graph[node1] += [node2]
    graph_rev[node2] += [node1]

#iterations for the first pass of depth-first search
stack = []
finish_time = 0
finish_time_dict = {}
explored_nodes = [False]*(num_nodes+1)
explored_nodes[0] = True

for node in range(1+num_nodes):
    stack.append(node)
    while stack:
        v = stack.pop()
        if explored_nodes[v] is False:
            explored_nodes[v] = True
            stack.append(v)
            for w in graph_rev[v]:
                if explored_nodes[w] is False:
                    stack.append(w)
        else:
            if v not in finish_time_dict:
                finish_time_dict[v] = finish_time
                finish_time += 1

#iterations for the second pass of depth-first search
explored_nodes = [False]*(num_nodes+1)
explored_nodes[0] = True
ordered = list(finish_time_dict.keys())
ordered.reverse()
scc_size = []

for node in ordered:
    n = 0
    stack.append(node)
    while stack:
        v = stack.pop()
        if explored_nodes[v] is False:
            n += 1
            explored_nodes[v] = True
            for w in graph[v]:
                stack.append(w)
    scc_size.append(n)

#get final answers
scc_size.sort(reverse = True)
print(scc_size[:5])
