import numpy as np

fh = open("g2.txt","r")
lon = fh.readlines()
fh.close()

G = {node:{} for node in range(1,1001)}
for line in lon[1:]:
    node1 = int(line.split()[0])
    node2 = int(line.split()[1])
    weight = int(line.split()[2])
    G[node1][node2] = weight

n = 1000

A = np.zeros([n,n,2])

for i in range(n):
    for j in range(n):
        if i == j:
            A[i,j,0] = 0
        elif j+1 in G[i+1]:
            A[i,j,0] = G[i+1][j+1]
        else:
            A[i,j,0] = np.inf

for k in range(1,n):
    if k%2 == 1:
        k1 = 1
        k2 = 0
    else:
        k1 = 0
        k2 = 1
    for i in range(n):
        for j in range(n):
            case1 = A[i,j,k2]
            case2 = A[i,k,k2] + A[k,j,k2]
            A[i,j,k1] = min(case1,case2)

for i in range(n):
    if A[i,i,1]<0:
        print("negative cycle")
        break

answer = A[:,:,1].min()
print(answer)

