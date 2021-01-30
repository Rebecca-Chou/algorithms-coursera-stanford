import re

num_nodes = 200
graph = [None] * (num_nodes + 1)
fh = open("dijkstraData.txt","r")
lines = fh.readlines()

for line in lines:
    line_lis = re.split(",|\t", line.strip())
    line_num = [int(el) for el in line_lis]
    list_tuple = []
    for i in range(1,len(line_num),2):
        list_tuple.append(tuple(line_num[i:i+2]))
    graph[line_num[0]] = list_tuple

X = [1]
Y = list(range(2,num_nodes+1))
node_dist_dict = {1:0}

while Y:
    temp = []
    for X_node in X:
        for Y_node in graph[X_node]:
            if Y_node[0] not in X:
                temp.append((Y_node[0],node_dist_dict[X_node]+Y_node[1]))
    shortest = min(temp, key = lambda x:x[1])
    node_dist_dict[shortest[0]] = shortest[1]
    X.append(shortest[0])
    Y.remove(shortest[0])

node_required = [7,37,59,82,99,115,133,165,188,197]
answer = []
for node in node_required:
    if node in node_dist_dict:
        answer.append(node_dist_dict[node])
    else:
        answer.append(1000000)

print(answer)
