from sys import stdin
V, E = map(int, stdin.readline().split(" "))
K = int(stdin.readline())
# 먼저 인접 리스트의 형식으로 받아서 겹치는 경로에 대한 최솟값으로 만들어준다.
# 그러고 나서는 knapsack이랑 비슷한 접근인 것 같기도 한데, 확실한 건 DP 문제라는 사실이다. 그리고 여기에 더해 DFS 방식을 활용할 수 있을 것 같다는 생각이 들었다. 생각해보니까 인접 리스트 전처리가 필요없을지도 모르겠다는 생각이 들었다.
# 우선 내 힘으로 풀어보고자 하고 안되면 Dijkstra 알고리즘을 공부하고 풀어봐야겠다.