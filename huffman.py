#Q1 & Q2

#read file
fh = open("huffman.txt","r")
num_list = fh.readlines()
fh.close()
weights = [int(line.strip()) for line in num_list[1:]]
num_ver = 1000

S = {idx: weights[idx] for idx in range(num_ver)}
final_index = 1000
merge_set = [[idx] for idx in range(num_ver)]

#huffman algo
while len(S) > 2:
    ver1 = min(S, key = S.get)
    w1 = S.pop(ver1)
    ver2 = min(S, key = S.get)
    w2 = S.pop(ver2)
    new_weight = w1 + w2
    S[final_index] = new_weight
    final_index += 1
    merge_set.append(merge_set[ver1] + merge_set[ver2])

depth = num_ver * [0]
for m in merge_set:
    for n in m:
        depth[n] += 1

max_depth = max(depth)
min_depth = min(depth)
print(max_depth, min_depth)
