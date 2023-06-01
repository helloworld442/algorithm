M,N = map(int,input().split())
ptr = 0
prime = [None] * N

prime[ptr] = 2
ptr += 1
# for 데이터 in 데이터들:
for n in range(3,N+1,2):
    i = 0
    while prime[i] * prime[i] <= n:
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
for i in range(ptr):
    if prime[i] >= M:
        print(prime[i])