class Solution:
    def checkIfExist(self, arr) -> bool:
        for number in arr:
            if number and number * 2 in arr or not number and arr.count(0) > 1:
                return True
        return False
