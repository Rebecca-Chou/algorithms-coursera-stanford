import heapq

fh = open("Median.txt","r")
lines = fh.readlines()
fh.close()
num_list = [int(el) for el in lines]

heap_low = []
heap_high = []
median = []

heapq.heapify(heap_low)
heapq.heapify(heap_high)
heap_high.append(num_list[0])
median.append(num_list[0])

for num in num_list[1:]:
    if num > heap_high[0]:
        heapq.heappush(heap_high,num)
    else:
        heapq.heappush(heap_low,-num)

    dif = len(heap_high)-len(heap_low)
    if dif > 1:
        temp = heapq.heappop(heap_high)
        heapq.heappush(heap_low,-temp)
    elif dif < -1:
        temp = heapq.heappop(heap_low)
        heapq.heappush(heap_high,-temp)

    if len(heap_high)>len(heap_low):
        median.append(heap_high[0])
    else:
        median.append(-heap_low[0])

print(sum(median) % 10000)
