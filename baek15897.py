n = int(input())

count = n
now = float('inf')
step = None
i = 1
while True:
    now = (n-1) // i
    if step is not None:
        count += (i-1) * (step-now)
    if i <= now:
        count += now
    if i >= now:
        break
    step = now
    i += 1

print(count)
