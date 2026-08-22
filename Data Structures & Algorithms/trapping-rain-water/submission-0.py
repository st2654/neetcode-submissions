class Solution:
    def trap(self, height: List[int]) -> int:
        maxLarr = [0]*len(height)
        maxRarr = [0]*len(height)
        output = [0]*len(height)


        maxL, maxR = 0, 0 
        for i in range(len(height)):
            j = -i-1
            maxLarr[i] = max(maxL, height[i])
            maxRarr[j] = max(maxR, height[j])
            maxL = maxLarr[i]
            maxR = maxRarr[j]
        
        for i in range(len(height)):
            tmp = min(maxLarr[i], maxRarr[i]) - height[i]
            output[i] =  tmp if tmp > 0 else 0
        
        summ = sum(output)

        return summ


