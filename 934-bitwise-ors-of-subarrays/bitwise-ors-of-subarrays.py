class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        all_results = set()
        prev_result = set()
        for num in arr:
            curr_result = set()
            curr_result.add(num)

            for prev in prev_result:
                glue = prev | num
                curr_result.add(glue) 

            for curr in curr_result:
                all_results.add(curr)

            prev_result = curr_result
        return len(all_results)