class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for num in arr2:
            for i in range(count[num]):
                res.append(num)
        arr1.sort()
        for i in range(len(arr1)):
            if arr1[i] not in arr2:

                res.append(arr1[i])
        return res