n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = [0]
B = [0]
for i in range(n):
  A.append(A[i] + a[i])
for i in range(m):
  B.append(B[i] + b[i])

res = 0
j = m

for i in range(n + 1):
  if A[i] > k:
    break
  while ((A[i] + B[j]) > k):
    j -= 1
  res = max(res, i + j)
  
print(res)
