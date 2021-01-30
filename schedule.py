import copy

#read file
fh = open("jobs.txt","r")
lon = fh.readlines()
fh.close()
jobs = []
for line in lon[1:]:
    job = [int(el) for el in line.strip().split()]
    jobs.append(job)

#Q1
jobs1 = copy.deepcopy(jobs)
jobs1.sort(key = lambda x:x[0], reverse = True)
jobs1.sort(key = lambda x:x[0]-x[1], reverse =  True)
completion_time = 0
answer1 = 0
for j in jobs1:
    completion_time += j[1]
    answer1 += j[0] * completion_time

print(answer1)

#Q2
jobs2 = copy.deepcopy(jobs)
jobs2.sort(key = lambda x:x[0]/x[1], reverse = True)
completion_time = 0
answer2 = 0
for j in jobs2:
    completion_time += j[1]
    answer2 += j[0] * completion_time

print(answer2)
