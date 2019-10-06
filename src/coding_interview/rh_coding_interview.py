"""
Find small +ve number which is not exist in list
Ex. [1, 3, 6, 4, 1, 2] -> 5
    [1, 2, 3] -> 4
    [-1, -3] -> 1
"""


def solution(A: list):
    A.sort()
    if A[-1] <= 0:
        return 1
    if len(A) == 1:
        return A[0] + 1 if A[0] > 0 else 1
    for n in A:
        if not binary_search(A, n + 1):
            return n + 1


def binary_search(A: list, n: int):
    first = 0
    last = len(A) - 1

    while first <= last:
        middle = (first + last) // 2
        if n == A[middle]:
            return True
        elif n < A[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False


print(solution([1, 3, 6, 4, 1, 2]))  # 5
print(solution([1, 2, 3]))  # 4
print(solution([-1, -3]))  # 1
print(solution([1]))  # 2
