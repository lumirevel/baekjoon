from sys import stdin
N = int(stdin.readline())
hos = []
for _ in range(N):
    hos.append(tuple(map(int, stdin.readline().split(" "))))
D = int(stdin.readline())
# 특정 구간에 온전한 ho가 몇 개 있는 지를 알아야 함->func으로 만들 것
# 아이디어 1: ho를 반전시키면?(ho에서 철로 선분을 검증하면?) O(n²)이다...
# 아이디어 2: ho가 적용되는 시작점의 범위를 각각 구한다
# -> 이미 있는 시작점을 저장한 set의 항목들을 철로 선분 시작점으로 잡는다
# -> 각 경우의 겹치는 수를 계산하여 max와 비교해 업데이트한다.
# 이 역시 worst가 O(n²)이다...