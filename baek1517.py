from sys import stdin

def answer(nums):
    result = nums.copy()
    swap = 0
    for _ in range(len(result) - 1):
        for i in range(len(result)-1):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                swap += 1
    return swap

N = int(input())
nums = list(map(int,stdin.readline().split(" ")))

print(answer(nums))
# swap의 수

