import numpy as np
#Q1
data = np.loadtxt("knapsack1.txt").astype(int)
W = data[0,0]
n = data[0,1]
v = data[1:,0]
s = data[1:,1]

A = np.zeros([n+1,W+1],int)

for i in range(1,n+1):
    for j in range(W+1):
        case1 = A[i-1,j]
        case2 = A[i-1,j-s[i-1]]+v[i-1]
        if j < s[i-1]:
            A[i,j] = case1
        else:
            A[i,j] = max(case1,case2)
answer1 = A[n,W]
print(answer1)

#Q2
data = np.loadtxt("knapsack_big.txt").astype(int)
W = data[0,0]
n = data[0,1]
v = data[1:,0]
s = data[1:,1]

A_idx = [[n,W]]
A = {(n,W):0}

length = 0
sol = A_idx[0]

while length < len(A_idx):
    (n,c) = sol
    (sol_1, sol_2) = [n-1, c], [n-1, c-s[n-1]]
    if n >= 1:
        if tuple(sol_1) not in A:
            A_idx.append(sol_1)
            A[tuple(sol_1)] = 0
        if c-s[n-1] >= 0:
            if tuple(sol_2) not in A:
                A_idx.append(sol_2)
                A[tuple(sol_2)] = 0
    sol = A_idx[length]
    length += 1

for i in range(len(A_idx)-1, -1, -1):
    (n, c) = A_idx[i]
    if n == 0: continue
    if c-s[n-1] < 0:
        A[(n,c)] = A[(n-1,c)]
    else:
        case1 = A[(n-1,c)]
        case2 = A[(n-1, c-s[n-1])] + v[n-1]
        A[(n,c)] = max(case1, case2)

answer2 = A[(n,W)]
print(answer2)
