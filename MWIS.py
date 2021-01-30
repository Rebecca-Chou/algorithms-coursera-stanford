#Q3
#read file
fh = open("mwis.txt","r")
num_list = fh.readlines()
w = [int(line.strip()) for line in num_list[1:]]
num_node = 1000
A = (num_node + 1) * [0]
A[1] = w[0]
for i in range(2, num_node+1):
    case1 = A[i-1]
    case2 = A[i-2] + w[i-1]
    A[i] = max(case1, case2)

ver = []
i = num_node
while i >= 1:
    if A[i-1] >= A[i-2] + w[i-1]:
        i -= 1
    else:
        ver.append(i)
        i -= 2
        
verts_q = [1, 2, 3, 4, 17, 117, 517, 997]
answer = str()
for v in verts_q:
    if v in ver:
        answer += '1'
    else:
        answer += '0'

print(answer)
