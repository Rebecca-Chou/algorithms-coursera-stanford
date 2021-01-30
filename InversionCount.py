def readFile(file_name):
    numbers = []
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip("\n")
            numbers.append(int(line))
    return numbers


def SortAndCount(l,left,right):
    if(left<right):
        m = (right+left)//2
        x = SortAndCount(l,left,m)
        y = SortAndCount(l,m+1,right)
        z = CountSplitInv(l,left,m,right)
        return x + y + z
    return 0


def CountSplitInv(l,left,m,right):
    i=0
    j=0
    k=left
    inv=0

    left_arr = l[left:m+1]
    right_arr = l[m+1:right+1]

    while(i<len(left_arr) and j<len(right_arr)):
        if(left_arr[i]<=right_arr[j]):
            l[k] = left_arr[i]
            k = k+1
            i = i+1
        else:
            l[k] = right_arr[j]
            k = k+1
            j = j+1
            inv = inv+len(left_arr)-i

    while(i<len(left_arr)):
        l[k] = left_arr[i]
        k = k+1
        i = i+1
    while(j<len(right_arr)):
        l[k] = right_arr[j]
        j = j+1
        k = k+1
    return inv


numbers = readFile("F:\CS\Algorithm\IntegerArray.txt")
n = SortAndCount(numbers,0,len(numbers)-1)
print(n)
print(numbers)
