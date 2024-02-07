from queue import PriorityQueue

T = int(input())
for _ in range(T):
    M = int(input())
    numList = list(map(int, input().split(" ")))

    print((M + 1) // 2)
    countBuffer = 0
    lower = PriorityQueue()
    upper = PriorityQueue()
    for i, num in enumerate(numList):
        if not lower.queue:
            lower.put((-num, num))
        else:
            if num < lower.queue[0][1]:
                lower.put((-num, num))
            else:
                upper.put((num, num))

            balance = len(upper.queue) - len(lower.queue)
            if abs(balance) == 2:
                if len(lower.queue) < len(upper.queue):
                    key, value = upper.get()
                    lower.put((-value, value))
                else:
                    key, value = lower.get()
                    upper.put((value, value))
        if i % 2 == 0:
            if countBuffer == 10:
                print()
                countBuffer = 0
            if len(lower.queue) < len(upper.queue):
                print(upper.queue[0][1], end=" ")
            else:
                print(lower.queue[0][1], end=" ")
            countBuffer += 1
    print()
