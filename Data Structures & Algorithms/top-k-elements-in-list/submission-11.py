from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # print(count)
        # Bucket

        freq_bucket = [[] for i in range(len(nums) + 1)] 
        # print("freq: ", freq_bucket)
        for n, c in count.items():
            # print(f"n: {n}, c: {c}")
            freq_bucket[c].append(n)
        
        # print("freq: ", freq_bucket)

        # Iterate from back:
        res = []
        i = len(freq_bucket) - 1
        while len(res) < k:
            for num in freq_bucket[i]:
                res.append(num)
            i -= 1
        return res
