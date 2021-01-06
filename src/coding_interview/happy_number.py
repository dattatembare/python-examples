class Solution:
    """
        Find happy numbers -
        1 - True
        5 - 5**2 = 25 = 2**2+5**2 = 4+25 = goes into infinite loop - False
        19 - 1**2 + 9**2 = 82 = 8**2 + 2**2 = 68 = 6**2 + 8**2 = 100 = 1 - True
    """
    def isHappy(self, n: int) -> bool:
        def get_sum(m):
            if m < 4:
                return m
            else:
                total = 0
                for i in str(m):
                    total += int(i) * int(i)
                return total

        num = get_sum(n)
        if num == 1:
            return True
        elif num == 0 or num < 4:
            return False
        else:
            try:
                return self.isHappy(num)
            except RecursionError:
                return False


s = Solution()
print(s.isHappy(19))
print(s.isHappy(9))
print(s.isHappy(5))
print(s.isHappy(2))
# True
# False
# False
# False
