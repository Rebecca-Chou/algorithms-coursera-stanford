def read_file(file_name):
    numbers = []
    with open(file_name,'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip("\n")
            numbers.append(int(line))
    return numbers

def quick_sort(arr,l,r,kind):
    if r-l>0:
        pivot = choose_pivot(arr,l,r,kind)
        i = l + 1
        j = l + 1
        while j <= r:
            if arr[j]<pivot:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i = i + 1
            j = j + 1
        arr[l] = arr[i-1]
        arr[i-1] = pivot
        m = quick_sort(arr,l,i-2,kind)
        n = quick_sort(arr,i,r,kind)
        return m + n + r - l
    return 0

def choose_pivot(arr,l,r,kind):
    if kind == 2:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
    elif kind == 3:
        middle = (l + r)//2
        pivot_set = [arr[l],arr[middle],arr[r]]
        pivot_set.sort()
        if arr[l] == pivot_set[1]:
            return choose_pivot(arr,l,r,1)
        elif arr[r] == pivot_set[1]:
            return choose_pivot(arr,l,r,2)
        elif arr[middle] == pivot_set[1]:
            temp = arr[l]
            arr[l] = arr[middle]
            arr[middle] = temp
            
    return arr[l]
            
number_arr = read_file("F:\CS\Algorithm\QuickSort.txt")
# print(quick_sort(number_arr,0,len(number_arr)-1,1))
# print(quick_sort(number_arr,0,len(number_arr)-1,2))
print(quick_sort(number_arr,0,len(number_arr)-1,3))
# print(number_arr)

