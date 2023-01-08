from sys import stdin
N, S = map(int, stdin.readline().split(" "))
nums = list(map(int, stdin.readline().split(" ")))

front_sum = [None for _ in range(2 ** (N // 2))]
rear_sum = [None for _ in range(2 ** (N - N // 2))]
rear_sum_count = [0 for _ in range(2*20*100000+1)]

for i in range(2**(N//2)):
    if i == 0:
        front_sum[i] = 0
    else:
        q = i
        n = -1
        while q:
            n += 1
            q //= 2
        front_sum[i] = front_sum[i - 2 ** n] + nums[n]
for i in range(2**(N-N//2)):
    if i == 0:
        rear_sum[i] = 0
    else:
        q = i
        n = -1
        while q:
            n += 1
            q //= 2
        rear_sum[i] = rear_sum[i - 2 ** n] + nums[N // 2 + n]
        rear_sum_count[rear_sum[i] + 20 * 100000] += 1

count_sum = 0
for i, v in enumerate(front_sum):
    if i != 0 and v == S:# 공집합과 공집합의 결합은 막고 rear의 공집합을 적재적소에 쓴다.
        count_sum += 1
    count_sum += rear_sum_count[S-v+20*100000]
print(count_sum)