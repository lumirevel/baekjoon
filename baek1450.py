from sys import stdin

N, C = map(int, stdin.readline().split(" "))
nums = list(map(int, stdin.readline().split(" ")))

front_sum = [None for _ in range(2**(N//2))]
rear_sum = [None for _ in range(2**(N-N//2))]
sort_of_rear_sum = set()
rear_sum_count = dict()#[0 for _ in range(15*10**9+1)]


def binary_search_under(sorted_lst, a):
    def binary_search_under_unit(sorted_lst, start_index, end_index, a):
        if start_index == end_index:
            if sorted_lst[start_index] <= a:
                return start_index
        elif end_index - start_index == 1:
            if sorted_lst[start_index] <= a < sorted_lst[end_index]:
                return start_index
            elif sorted_lst[end_index] <= a:
                return end_index
        else:
            middle_index = (start_index + end_index) // 2
            if a < sorted_lst[middle_index]:
                return binary_search_under_unit(sorted_lst, start_index, middle_index, a)
            elif a > sorted_lst[middle_index]:
                return binary_search_under_unit(sorted_lst, middle_index, end_index, a)
            else:
                return middle_index
    return binary_search_under_unit(sorted_lst, 0, len(sorted_lst)-1, a)


for i in range(2**(N//2)):
    if i == 0:
        front_sum[i] = 0
    else:
        q = i
        n = -1
        while q:
            n += 1
            q //= 2
        front_sum[i] = front_sum[i-2**n] + nums[n]
for i in range(2**(N-N//2)):
    if i == 0:
        rear_sum[i] = 0
        #rear_sum_count[i] = 1
    else:
        q = i
        n = -1
        while q:
            n += 1
            q //= 2
        rear_sum[i] = rear_sum[i-2**n] + nums[N//2+n]
        sort_of_rear_sum.add(rear_sum[i])
        if not rear_sum[i] in rear_sum_count:
            rear_sum_count[rear_sum[i]] = 0
        rear_sum_count[rear_sum[i]] += 1

sorted_sort_of_rear_sum = sorted(list(sort_of_rear_sum))
cumul_sum_count = []
now_sum = 0
for v in sorted_sort_of_rear_sum:
    now_sum += rear_sum_count[v]
    cumul_sum_count.append(now_sum)

count_sum = 0
for v in front_sum:
    if v <= C:
        count_sum += 1  # 공집합 처리
        complement_weight = C-v
        under_max_index = binary_search_under(sorted_sort_of_rear_sum, complement_weight)
        if isinstance(under_max_index, int):
            count_sum += cumul_sum_count[under_max_index]
print(count_sum)
