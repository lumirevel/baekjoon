# from sys import stdin
#
# N = int(stdin.readline())
#
#
# def validity(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     if x1 == x2:
#         return False
#     elif y1 == y2:
#         return False
#     elif abs(y2 - y1) == abs(x2 - x1):
#         return False
#     else:
#         return True
#
#
# def dfs(visited):
#     sum = 0
#     for j in range(N):
#         now = (len(visited), j)
#
#         valid = True
#         for previous in visited:
#             if not validity(previous, now):
#                 valid = False
#                 break
#
#         if valid:
#             if len(visited) + 1 == N:
#                 sum += 1
#             else:
#                 sum += dfs(visited + [now])
#     return sum
#
# cnt = 0
# for j in range(N):
#     now = (0, j)
#     cnt += dfs([now])
#
# print(cnt)

from sys import stdin
N = int(stdin.readline())


def dfs(visited, row):
	sum = 0
	for j in range(N):
		now = (len(visited), j)

		valid = True
		if row[now[1]]:
			valid = False
		else:
			for p in enumerate(visited):
				if abs(p[1] - now[1]) == abs(p[0] - now[0]):
					valid = False
					break

		if valid:
			if len(visited) + 1 == N:
				sum += 1
				break
			else:
				row[j] = True
				sum += dfs(visited + [j], row)
				row[j] = False
	return sum

if N == 1:
	print(1)
else:
	cnt = 0
	row = {}
	for i in range(N):
		row[i] = False
	for j in range(N):
		now = (0, j)
		row[j] = True
		cnt += dfs([now[1]], row)
		row[j] = False

	print(cnt)


"""# 백준 9663 N-Queen
start = time.time()

def queen(table, n, table_length):
	global count
	for i in range(table_length): # 한 열에 놓을 수 있는 케이스
		if check(table, n, i, table_length) == True: # 놓을 수 있다면
			if n == table_length - 1: # 열의 마지막에 도착했다면
				count += 1  # 카운트 +1하고 반복 break
				break
			table[n][i] = 1 # 테이블에 퀸 놓고 아래에서 재귀 탐색
			dic[i] = 1 # 해당 열에 놓았다고 표시하기
			queen(table, n + 1, table_length)
			table[n][i] = 0 # 재귀 탐색이 끝났으므로 원래대로
			dic[i] = 0 # 열에 놓았다는 표시 지우기

# 테이블 체크 함수
def check(table, n, now, table_length):
	n -= 1 # 이전 줄부터 검사
	if dic[now] == 1: # 같은 라인에 이미 값이 있는지
		return False
	side = 1 # 대각선으로 체크하기 위한 변수
	while 0 <= n: # n-1번째부터 0번째까지 체크
		if (now - side) >= 0 and table[n][now-side] == 1: # 대각선으로 앞쪽
			return False
		if (now + side) < table_length and table[n][now+side] == 1: #대각선으로 뒷쪽
			return False
		n -= 1 # 이전 줄로
		side += 1 # 더 대각선으로
	return True

# 시작
global count
count = 0
table_length = N
# table = [[0] * table_length] * table_length # 엄청난 실수
table = list()
dic = {}
for i in range(table_length):
	table.append([0] * table_length)
	dic[i] = 0

queen(table, 0, table_length)
print(count)
print("time :", time.time() - start)"""