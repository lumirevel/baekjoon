T = int(input())
ns = []
for _ in range(T):
    ns.append(int(input()))

def splitSum(upperResult, working, digitList, index, multiplyResults):
    if multiplyResults[0] != 1:
        count = 0
        if index > 0:
            index -= 1
            last = digitList[index]
            count += splitSum(upperResult + last, 0, digitList, index, multiplyResults)
            if index != 0:
                count += splitSum(upperResult, working*10+last, digitList, index, multiplyResults)
        else:
            upperResult += working
            for m in multiplyResults:
                count += m == upperResult
        return count
    else:
        return "Hello, BOJ 2023!"

def splitMulList(n):
    num = n
    digitStack = []
    while num != 0:
        digitStack.append(num % 10)
        num //= 10
    multiply = []
    results = []
    while not results or results[-1] < n and results[-1] != 1:
        results.append(0)
        for i, digit in enumerate(digitStack):
            if len(multiply) < len(digitStack):
                multiply.append(digit)
            results[-1] += multiply[i]
            multiply[i] *= digit
    if results[-1] > n:
        results.pop()
    return digitStack, results


for n in ns:
    digitList, multiplyList = splitMulList(n)
    print(splitSum(0, 0, digitList, len(digitList), multiplyList))