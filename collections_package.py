import collections

### Most common elements in an iterable (collections.Counter)

A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
print(A)  # Counter({3: 4, 1: 2, 2: 2, 4: 1, 5: 1, 6: 1, 7: 1})
print(A.most_common(1))  # [(3, 4)]
print(A.most_common(3))  # [(3, 4), (1, 2), (2, 2)]

# Double-ended queue (collections.deque)
Q = collections.deque()
Q.append(1)
Q.appendleft(2)
Q.extend([3, 4])
Q.extendleft([5, 6])
print(Q)
# deque([6, 5, 2, 1, 3, 4])
print(Q.pop())  # 4
print(Q)  # [6, 5, 2, 1, 3]
print(Q.popleft())  # 6
print(Q)  # deque([5, 2, 1, 3])
Q.rotate(3)
print(Q)  # deque([2, 1, 3, 5])
Q.rotate(-3)
print(Q)  # deque([5, 2, 1, 3])
