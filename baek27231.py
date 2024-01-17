from random import randint as rand

T = int(input())
ns = []
for _ in range(T):
    # ns.append(rand(1,1000))
    ns.append(int(input()))

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

def splitSumChecker(upperResult, working, digitList, index, multiplyResults):
    if multiplyResults[0] != 1:
        count = 0
        if index > 0:
            index -= 1
            last = digitList[index]
            count += splitSumChecker(upperResult + last, None, digitList, index, multiplyResults)
            if index != 0 and working != 0:
                if working is None:
                    working = 0
                count += splitSumChecker(upperResult, working * 10 + last, digitList, index, multiplyResults)
        else:
            for m in multiplyResults:
                count += m == upperResult
        return count
    else:
        return "Hello, BOJ 2023!"


for n in ns:
    digitList, multiplyList = splitMulList(n)
    print(splitSumChecker(0, None, digitList, len(digitList), multiplyList))