import copy
import random

def karger_min_cut(list_adj,ite):
    list_result = []
    for i in range(ite):
        list_new_adj = copy.deepcopy(list_adj)
        n = karger_al(list_adj)
        list_result.append(n)
        list_adj = list_new_adj
    return min(list_result)

def karger_al(list_adj):
    #当vertex数量大于2
    while len(list_adj)>2:
        row_adj = random.choice(list_adj)
        s = row_adj[0]  #随机选到vertex x
        t = random.choice(row_adj[1:]) # vertex y

        #找到随机选择的node的索引
        st_ind = find_node_index(list_adj,s,t)
        s_ind = st_ind[0]
        t_ind = st_ind[1]

        #把所有y全部改成x
        list_adj[s_ind].extend(list_adj[t_ind])
        for i in range(len(list_adj)):
            list_adj[i] = [s if x==t else x for x in list_adj[i]]

        #把s中self-loop和被替换的t都去掉
        temp = []
        for j in list_adj[s_ind]:
            if j==s and j not in temp:
                temp.append(j)
            elif j!=s:
                temp.append(j)
        list_adj[s_ind] = temp

        #删除t
        del list_adj[t_ind]

    num_cut = len(list_adj[1])-1
    return num_cut

def find_node_index(list_adj,s,t):
    for i in enumerate(list_adj):
        if i[1][0]==s:
            s_index = i[0]
        if i[1][0]==t:
            t_index = i[0]
    index_tuple = (s_index,t_index)
    return index_tuple

f = open('kargerMinCut.txt', 'r')
lines = f.readlines()
f.close()
list_adj = []
for line in lines:
    list_adj.append([int(i) for i in line.split()])
print(karger_min_cut(list_adj,100))    
