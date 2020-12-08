class Solution:
    def sortArrayByParity(self, A):
        result = []

        for num in A:
            result.append(num) if num % 2 else result.insert(0, num)

        return result
