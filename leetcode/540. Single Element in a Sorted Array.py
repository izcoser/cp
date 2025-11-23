from typing import List
class MySolution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l != r:
            mid = (l + r) // 2
            before = mid - 1
            after = mid + 1

            if nums[mid] != nums[after] and nums[mid] != nums[before]:
                return nums[mid]

            if nums[mid] != nums[after]:
                elements_in_left_side = mid - 1 - l
                if elements_in_left_side % 2 == 1:
                    r = mid - 2
                else:
                    l = mid + 1
            
            elif nums[mid] != nums[before]:
                elements_in_left_side = mid - l
                if elements_in_left_side % 2 == 1:
                    r = mid - 1
                else:
                    l = mid + 2

        return nums[l]
    

class NeetCodeSolution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            # Check if nums[m] is the unique element
            if (
                (m - 1 < 0 or nums[m - 1] != nums[m]) and
                (m + 1 == len(nums) or nums[m] != nums[m + 1])
            ):
                return nums[m]

            # Determine how many elements are to the left of the pair
            leftSize = m - 1 if nums[m - 1] == nums[m] else m

            # If left side is odd, the single is in the left half
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1
