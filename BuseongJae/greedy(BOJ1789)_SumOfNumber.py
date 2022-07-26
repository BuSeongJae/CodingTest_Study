result = int(input())
cnt = 0
i =1
while result > 0:
    result -= i
    i += 1
    cnt += 1
if(result != 0):
    cnt-=1


print(cnt)