from sys import stdin
from copy import deepcopy as copy
L, U = map(int, stdin.readline().split(" "))


def sum_all_digit(L:int, U:int) -> int:
    """
    L부터 U까지의 모든 수의 모든 자리의 숫자를 더한 값을 출력함
    :param L: 시작값
    :param U: 끝값
    :return: L부터 U까지의 모든 수의 모든 자리의 숫자를 더한 값
    """
    def digitize_10(Q: int) -> list[int]:
        """
        Q를 십진 체계에 따라 list로 만들어 특정 자리의 숫자에 접근할 수 있도록 함
        :param Q: 정수
        :return: Q를 자릿수마다 자른 list
        """
        digits = []
        while Q:
            digits.append(Q % 10)
            Q //= 10
        return digits
    def digit_2_int(digits: list[int]) -> int:
        """
        십진 체계에 따라 list로 만들어진 digits list를 다시 int로 바꿔줌
        :param digits: 정수를 자릿수마다 자른 list
        :return: digits에 해당하는 정수
        """
        Q = 0
        digit_count = 1
        for v in digits:
            Q += v * digit_count
            digit_count *= 10
        return Q
    def cumul_sum(s, e):
        return (e*(e+1)-s*(s-1))//2
    def sum_all_digit_unit(S:list[int], E:list[int]) -> tuple[int, int]:
        """
        sum_all_digit의 unit. 재귀적인 방법으로 L부터 U까지의 모든 수의 모든 자리의 숫자를 더하기 위해 사용됨
        :param S: 시작값
        :param E: 끝값
        :return: S와 E 사이의 수의 갯수와 모든 자리의 숫자를 더한 값
        """
        S, E = copy(S), copy(E)
        digits_sum, count = 0, 0
        if len(S) == len(E):
            overlab_sum = 0
            while len(S) and S[-1] == E[-1]:
                overlab_sum += (S.pop() + E.pop()) // 2
            if overlab_sum:
                child = sum_all_digit_unit(S, E)

                digits_sum += overlab_sum * child[0] + child[1]
                count += child[0]
            else:
                if len(S) == 0:
                    count += 1
                elif len(S) == 1:
                    digits_sum += cumul_sum(S[-1], E[-1])
                    count += E[-1]-S[-1]+1
                else:
                    S_now, E_now = S.pop(), E.pop()
                    if E_now - S_now == 1:
                        value_front = sum_all_digit_unit(S, [9 for _ in range(len(S))])
                        value_end = sum_all_digit_unit([0 for _ in range(len(E))], E)

                        digits_sum += S_now * value_front[0] + value_front[1] + E_now * value_end[0] + value_end[1]
                        count += value_front[0] + value_end[0]
                    else:
                        value_front = sum_all_digit_unit(S, [9 for _ in range(len(S))])
                        value_end = sum_all_digit_unit([0 for _ in range(len(E))], E)

                        digits_sum += S_now * value_front[0] + value_front[1]\
                               + cumul_sum(S_now+1, E_now-1) * 10 ** len(S) + (E_now - S_now - 1) * len(S) * 45 * 10 ** (len(S)-1)\
                               + E_now * value_end[0] + value_end[1]
                        count += value_front[0] + (E_now-S_now-1) * 10**len(S) + value_end[0]
        else:
            for i in range(len(S) + 1, len(E) - 1+1):
                digits_sum += 45 * 10**(i-1)
                digits_sum += (i-1) * 45 * 9 * 10**(i-2)
                count += 10**i
            value_front = sum_all_digit_unit(S, [9 for _ in range(len(S))])
            value_end = sum_all_digit_unit([1 if i == len(E) - 1 else 0 for i in range(len(E))], E)
            digits_sum += value_front[1] + value_end[1]
            count += value_front[0] + value_end[0]
        return (count, digits_sum)
    return sum_all_digit_unit(digitize_10(L), digitize_10(U))[1]


print(sum_all_digit(L, U))
