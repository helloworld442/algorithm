n = int(input())
for _ in range(n):
    H,W,N = map(int,input().split())
    몫,나머지 = divmod(N,H)
    if 나머지 == 0:
        print( ( H * 100 ) + 몫 ) 
    else:
        print(( 나머지*100 ) + ( 몫 + 1 ) )