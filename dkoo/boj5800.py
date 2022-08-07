import sys

# 반의 수
K = int(sys.stdin.readline())

for i in range(K):

    a = list(map(int, sys.stdin.readline().split()))
    del a[0] # 첫번째 값 삭제
    a.sort() # 정렬
    Lgap = []
    print('Class', i+1)
    # 큰 차이나는 함수 추가
    for i in range(len(a)-1):
        Lgap.append(a[i+1] - a[i])

    print('Max', str(max(a))+',' ,'Min', str(min(a))+',', 'Largest gap', max(Lgap))