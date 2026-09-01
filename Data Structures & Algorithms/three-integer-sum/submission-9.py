class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        if nums[0] > 0:
            return []
        n = len(nums)

        for i in range(n):
            left = i+1
            right = n - 1
    
            while nums[i] <= 0 and left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        print("Result", result)
        ret = [ [a,b,c] for a,b,c in result]
        return ret
                    
        