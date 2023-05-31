n = int(input())
count = 0


# n > 0 
while n > 0:
    if n % 5 == 0:
        count = count + ( n // 5 ) # count 몫만큰 증가
        break
    else:
        n = n - 3 # 남은 설탕 수
        count = count + 1 # count 1증가
if n < 0:
    print(-1)  
else:
    print(count)