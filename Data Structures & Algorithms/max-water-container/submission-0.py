class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i, j = 0, len(heights) -1

        while i < j:
            length = j-i
            height = min(heights[i], heights[j])
            area = max(length*height, area)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return area


