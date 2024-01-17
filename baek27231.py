T = int(input())
ns = []
for _ in range(T):
    ns.append(int(input()))

def splitMulList(n):
    num = n
    digitStack = []
    while num != 0:
        digitStack.append(num % 10)
        num //= 10
    multiply = []
    results = []
    while not results or results[-1] < n and not (len(results) >= 2 and results[-1] == results[-2]):
        results.append(0)
        for i, digit in enumerate(digitStack):
            if len(multiply) < len(digitStack):
                multiply.append(digit)
            results[-1] += multiply[i]
            multiply[i] *= digit
    if results[-1] > n or (len(results) >= 2 and results[-1] == results[-2]):
        results.pop()
    return digitStack, results

def splitSumChecker(upperResult, working, digitList, index, multiplyResults):
    if multiplyResults[0] != 1:
        count = 0
        if index > 0:
            index -= 1
            last = digitList[index]
            count += splitSumChecker(upperResult + working, last, digitList, index, multiplyResults) # 앞에 + 추가
            if working != 0:
                count += splitSumChecker(upperResult, working * 10 + last, digitList, index, multiplyResults) # 앞에 + 추가 안 함
        else:
            upperResult += working
            i = 0
            while i < len(multiplyResults):
                if multiplyResults[i] == upperResult:
                    count += 1
                    multiplyResults[i] = 0
                i += 1
        return count
    else:
        return "Hello, BOJ 2023!"


for n in ns:
    digitList, multiplyList = splitMulList(n)
    print(splitSumChecker(0, 0, digitList, len(digitList), multiplyList))