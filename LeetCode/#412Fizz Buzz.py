def is_fizz(n):
    return n % 3 == 0
def is_buzz(n):
    return n % 5 == 0

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n + 1):
            if is_fizz(i) and is_buzz(i):
                ans.append("FizzBuzz")
                continue
            if is_fizz(i):
                ans.append("Fizz")
                continue
            if is_buzz(i):
                ans.append("Buzz")
                continue

            ans.append(str(i))
        return ans