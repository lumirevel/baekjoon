T = int(input())
ns = []
for _ in range(T):
    ns.append(int(input()))

def splitMulList(n):
    num = n
    sum = 0
    binary = True
    digitStack = []
    multiply = []
    while num != 0:
        digit = num % 10
        digitStack.append(digit)
        multiply.append(digit)
        sum += digit
        if digit != 0 and digit != 1:
            binary = False
        num //= 10
    results = [sum]

    if not binary:
        while not results or results[-1] < n:
            results.append(0)
            for i, digit in enumerate(digitStack):
                multiply[i] *= digit
                results[-1] += multiply[i]

        if results[-1] > n:
            results.pop()
        return digitStack, results
    else:
        return digitStack, [-1]

def splitSumChecker(upperResult, working, digitList, index, multiplyResults):
    if multiplyResults[0] != -1:
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