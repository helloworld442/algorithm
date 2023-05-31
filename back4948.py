testArr = [0] * 2 + [1] * 246912
for i in range(2,246912):
    if testArr[i]:
        for j in range(i*2,246913,i):
            testArr[j] = 0
while True:
    N = int(input())
    if N == 0:
        break
    print(sum(testArr[N+1:2*N+1]))