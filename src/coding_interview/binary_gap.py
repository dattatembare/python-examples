"""
find max gap btween two 1s
25 = 11001 -> 2
32 = 100000 -> 0
15 = 1111 -> 0
1041 = 10000010001 -> 5
"""


def solution(N):
    gap = 0
    if 0 < N < 2147483647:
        bin = format(N, 'b')
        print(bin)
        gap_list = [i for i, c in enumerate(bin) if c == '1']
        print(gap_list)
        if len(gap_list) == len(bin):
            return gap

        for n in range(len(gap_list) - 1):
            val = gap_list[n + 1] - (gap_list[n] + 1)
            if val > gap:
                gap = val
    return gap


print(solution(25))
print(solution(32))
print(solution(15))
print(solution(1041))
