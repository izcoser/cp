from typing import List
# geometry, easy

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # sort by x and then y, default behavior of .sort, no need for key parameter.
        # now we can iterate in left to right order.
        points.sort()


        # create lower and upper parts of our convex hull
        lower = []

        for p in points:
            lower.append(p)
            while len(lower) >= 3 and cross_product(lower[-3:]) <= 0: # remove middle point if a turn is CW or collinear
                tmp = lower.pop()
                lower.pop()
                lower.append(tmp)
        
        lower.pop()

        upper = []

        for p in reversed(points):
            upper.append(p)
            while len(upper) >= 3 and cross_product(upper[-3:]) <= 0:
                tmp = upper.pop()
                upper.pop()
                upper.append(tmp)

        upper.pop()

        hull = lower + upper
        max_area = 0

        for i in range(len(hull)):
            for j in range(i + 1, len(hull) - 1):
                k = j + 1
                prev_area = 0
            
                while k < len(hull): # for a fixed (i, j), look for k while the triangle area increases (if it starts to decrease, we stop looking)
                    ps = [hull[i], hull[j], hull[k]]
                    area = abs(cross_product(ps))

                    if area <= prev_area:
                        break

                    prev_area = area
                    
                    if area > max_area:
                        max_area = area
                    
                    k += 1
    
        return max_area / 2


def cross_product(points: List[List[int]]) -> float:
    a, b, c = points
    ab = [b[0] - a[0], b[1] - a[1]]
    ac = [c[0] - a[0], c[1] - a[1]]

    return (ab[0] * ac[1]) - (ab[1] * ac[0])

# Notes: according to sources, k doesn't have to be reset for every j, and can be set inside the i loop as k = i + 2.
# But I don't understand that very well, so sticking to my implementation which makes more sense to me.