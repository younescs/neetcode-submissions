from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        count_list = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            count_list[value].append(key)

        answer = []
        for i in range(len(count_list)-1, 0, -1):
            for count in count_list[i]:
                answer.append(count)
                if len(answer) == k:
                    return answer
            


        