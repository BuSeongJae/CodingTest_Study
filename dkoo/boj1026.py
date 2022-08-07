import sys

N = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True) # 내림차순
b.sort() # 오름차순

c = 0
sum = 0

# 결과 출력
for i in a:
    sum += i * b[c]
    c += 1

print(sum)