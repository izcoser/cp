from typing import List
# geometry, easy
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prev_slope = None

        for i in range(len(coordinates) - 1):
            a, b = coordinates[i], coordinates[i + 1]
            dy = b[1] - a[1]
            dx = b[0] - a[0]

            if dx == 0:
                slope = 'inf'
            else:
                slope = dy / dx
            
            if prev_slope != None and slope != prev_slope:
                return False
            
            prev_slope = slope
        
        return True
    
    def checkStraightLineCrossProduct(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        dx0 = x1 - x0
        dy0 = y1 - y0

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]

            dx = x - x0
            dy = y - y0

            if dx0 * dy - dy0 * dx != 0:
                return False

        return True