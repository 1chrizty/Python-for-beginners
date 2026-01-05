'''Prime numbers between a series of numbers'''

start = int(input('Enter start:'))
stop = int(input('Enter stop:'))
for i in range(start,stop):
    if i < 2:
        continue
    flag = 0
    for j in range(2,(i//2) + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i,end=' ')