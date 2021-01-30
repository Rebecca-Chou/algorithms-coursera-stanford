import copy
'''
#Q1
#read file
fh = open("clustering1.txt","r")
loe = fh.readlines()
fh.close()

#create graph
graph = {}
for line in loe[1:]:
    node1 = int(line.split()[0])
    node2 = int(line.split()[1])
    dist = int(line.split()[2])
    graph[(node1, node2)] = dist
    
#Kruskul's algo for clustering
G = copy.deepcopy(graph)
num_cluster = 500
leader = list(range(501))
for e in graph:
    edge = min(G, key = G.get) #key
    dist = G.pop(edge)    #value
    leader1 = leader[edge[0]]
    leader2 = leader[edge[1]]
    if leader1 != leader2 and num_cluster > 4:
        num_cluster -= 1
        for i in range(1,501):
            if leader[i] == leader2:
                leader[i] = leader1
    elif leader1 != leader2 and num_cluster == 4:
        answer1 = dist
        break
print(answer1)
'''


#Q2
def create_list_within2(key):
    list_key = []
    for i in range(24):
        k = list(key)
        if k[i] == '0':
            k[i] = '1'
        else:
            k[i] = '0'
        list_key += [int("".join(k),2)]
        for j in range(i+1,24):
            k_ = k.copy()
            if k_[j] == '0':
                k_[j] = '1'
            else:
                k_[j] = '0'
            list_key += [int("".join(k_),2)]
    return list_key

def find(el):
    global union_find
    if union_find[el] == el:
        return el
    elif union_find[union_find[el]] == union_find[el]:
        return union_find[el]
    else:
        new_el = union_find[el]
        while new_el != union_find[new_el]:
            new_el = union_find[new_el]
        union_find[el] = new_el
        return union_find[el]

def merge(el1, el2):
    global union_find
    global rank
    leader1 = find(el1)
    leader2 = find(el2)
    if leader1 != leader2:
        if rank[leader1] < rank[leader2]:
            union_find[leader1] = leader2
        elif rank[leader1] > rank[leader2]:
            union_find[leader2] = leader1
        else:
            union_find[leader2] = leader1
            rank[leader1] += 1
    
#read file
fh = open("clustering_big.txt","r")
loe = fh.readlines()
fh.close()
graph = [line.strip().replace(" ","") for line in loe[1:]]
graph = list(set(graph))
#convert number system
G = [int(line,2) for line in graph]

#Union-Find
union_find = {key: key for key in G}
rank = {key: 0 for key in G}

for i in range(len(graph)):
    for el in create_list_within2(graph[i]):
        if el in union_find:
            merge(G[i],el)
answer2 = len(set([find(x) for x in union_find]))
print(answer2)

