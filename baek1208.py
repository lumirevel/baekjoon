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
        rear_sum_count[i] += 1
    else:
        q = i
        n = -1
        while q:
            n += 1
            q //= 2
        rear_sum[i] = rear_sum[i - 2 ** n] + nums[N // 2 + n]
        rear_sum_count[rear_sum[i] + 20 * 100000] = rear_sum_count[rear_sum[i - 2 ** n] + 20 * 100000]

count_sum = 0
for v in front_sum:
    count_sum += rear_sum_count[S-v]
print(count_sum)