class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_of_a = (ay2 - ay1) * (ax2 - ax1)
        area_of_b = (by2 - by1) * (bx2 - bx1)
        
        inter_width  = max(0, min(ax2, bx2) - max(ax1, bx1))
        inter_height = max(0, min(ay2, by2) - max(ay1, by1))

        return area_of_a + area_of_b - inter_height * inter_width
