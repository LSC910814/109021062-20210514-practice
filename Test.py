n = int(input())
1 <= n <= 30
n1 = list(map(int,input().split()))
data = n1
w = 1
ral = 0
for i in range(1, len(data), 2):
    for j in range(i+1, len(data), 2):
        if data[j] < data [i] and ral ==0:
            w += 1
        else:
            ral +=1
print(w)