class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def getSum(current, arr, index):
            if current > target:
                return
                
            if current == target:
                sorted_arr = sorted(arr.copy())
                if sorted_arr not in res:
                    res.append(sorted_arr)
                return

            for i in range(index, len(candidates)):
                arr.append(candidates[i])
                getSum(current + candidates[i], arr, i)
                arr.pop()

        getSum(0, [], 0)
        return res
