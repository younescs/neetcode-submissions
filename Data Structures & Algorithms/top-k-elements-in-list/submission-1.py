class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        elements = [[] for _ in range(len(nums)+ 1)]

        for key, value in count.items():
            elements[value].append(key)

        res = []
        for i in range(len(elements)-1, 0, -1):
            for item in elements[i]:
                res.append(item)
                if len(res) == k:
                    return res