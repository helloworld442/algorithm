N = int(input())
cnt = 1
다음숫자 = N
while True:
    앞 = 다음숫자 // 10
    뒤 = 다음숫자 % 10 
    앞뒤 = (앞 + 뒤) % 10
    다음숫자 = 뒤*10 + 앞뒤
    if 다음숫자 == N:
        break
    cnt += 1
print(cnt)