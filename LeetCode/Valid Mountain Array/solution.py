class Solution:
    def validMountainArray(self, A) -> bool:

        _index_peak = A.index(max(A)) if len(A) else 0

        if not _index_peak or _index_peak is len(A) - 1:
            return False

        '''
            If number i bigger then next number before peek
        '''
        for i, num in enumerate(A[:_index_peak]):
            if num >= A[i + 1]:
                return False

        '''
            If number is bigger then previos number after peek
        '''
        for i, num in enumerate(A[_index_peak + 1:]):
            if num >= A[i + _index_peak]:
                return False

        return True
