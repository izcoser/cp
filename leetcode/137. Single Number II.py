# https://leetcode.com/problems/single-number-ii/description/

from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        for k, v in count.items():
            if v == 1:
                return k

# Approach 2: Bit Manipulation
# Explanation:
# Initialize the variable ans to 0. This variable will store the resulting single number.

# Iterate from i = 0 to i = 31. This loop considers each bit position from the least significant bit (LSB) to the most significant bit (MSB) of a 32-bit integer.

# Inside the loop, initialize a variable sum to 0. This variable will keep track of the number of 1s at the current bit position (i) for all the numbers in the input array.

# Iterate through each number num in the input array:

# Right-shift num by i positions: num >> i. This operation moves the bit at position i to the least significant bit position.
# Perform a bitwise AND with 1: (num >> i) & 1. This extracts the value of the bit at position i from num. If it is 1, the result will be 1; otherwise, it will be 0.
# Add the result of (num >> i) & 1 to sum. This counts the number of 1s at bit position i for all the numbers in the array.
# Take the modulo of sum by 3: sum %= 3. This step is performed to handle the numbers that appear three times. If sum is divisible by 3, it means the bit at position i has a balanced number of 1s. Otherwise, it is an unbalanced line.

# Left-shift the value of sum by i positions: sum << i. This step creates a bitmask pos where only the bit at position i is set to the value of sum. This bitmask identifies the position of the unbalanced line.

# Use the bitwise OR operation with ans and pos: ans |= pos. This sets the corresponding bit in ans to 1 if the bit at position i is part of an unbalanced line.

# After the loop completes, the value stored in ans represents the single number that appears only once in the array.

# The logical thinking behind this approach is to count the number of 1s at each bit position for all the numbers. Since each number appears three times except for the single number, the sum of 1s at each bit position should be divisible by 3 for a balanced line. Any number of 1s that is not divisible by 3 indicates an unbalanced line, which means the single number contributes to that particular bit position.

# By masking the positions of the unbalanced lines with 1s in ans, we effectively isolate the bits that are part of the single number. Finally, the resulting value in ans represents the binary representation of the single number.

# Using the provided example: [1, 1, 1, 2, 2, 2, 5]

# At the LSB (i = 0), the sum of the number of 1s is 3 (balanced line).
# At the second bit (i = 1), the sum of the number of 1s is 4 (unbalanced line, not divisible by 3).
# At the third bit (i = 2), the sum of the number of 1s is 2 (unbalanced line, not divisible by 3).
# At the fourth bit
# (i = 3), the sum of the number of 1s is 1 (balanced line).

# Thus, the resulting binary representation is '0101', which corresponds to the decimal value 5, and that is the single number we are searching for.

# This approach effectively identifies the unbalanced lines and constructs the single number by setting the corresponding bit positions in ans.

# class Solution:
#     def singleNumber(self, nums):
#         ans = 0

#         for i in range(32):
#             bit_sum = 0
#             for num in nums:
#                 # Convert the number to two's complement representation to handle large test case
#                 if num < 0:
#                     num = num & (2**32-1)
#                 bit_sum += (num >> i) & 1
#             bit_sum %= 3
#             ans |= bit_sum << i

#         # Convert the result back to two's complement representation if it's negative to handle large test case
#         if ans >= 2**31:
#             ans -= 2**32

#         return ans


# ################

# Approach 3: Magic:
# Explanation:
# Initialize two variables, ones and twos, to keep track of the count of each bit position.

# ones: Tracks the bits that have appeared once.
# twos: Tracks the bits that have appeared twice.
# Iterate through the array of numbers.

# For each number i in the array:
# Update ones and twos:

# Let's analyze each step of the update process:

# a. ones = (ones ^ i) & (~twos);:

# ones ^ i XORs the current number i with the previous value of ones. This operation toggles the bits that have appeared an odd number of times, keeping the bits that have appeared twice unchanged.
# (~twos) negates the bits in twos, effectively removing the bits that have appeared twice from consideration.
# The & operation ensures that only the bits that have appeared once (after XOR) and not twice (after negating twos) are retained.
# b. twos = (twos ^ i) & (~ones);:

# twos ^ i XORs the current number i with the previous value of twos. This operation toggles the bits that have appeared an even number of times, effectively removing the bits that have appeared twice.
# (~ones) negates the bits in ones, effectively removing the bits that have appeared once from consideration.
# The & operation ensures that only the bits that have appeared twice (after XOR) and not once (after negating ones) are retained.
# After iterating through all the numbers, the value stored in ones will represent the single number that appears only once in the array.

# Let's understand why this approach works:

# The key idea is to use bitwise operations to keep track of the count of each bit position. By doing so, we can identify the bits that have appeared once, twice, or three times.
# When a bit appears for the first time (ones is 0 and the bit is toggled), it is stored in ones.
# When a bit appears for the second time (ones is 1 and the bit is toggled), it is removed from ones and stored in twos.
# When a bit appears for the third time (ones is 0 and the bit is toggled), it is removed from both ones and twos.
# By the end of the iteration, the bits that remain in ones represent the bits of the single number that appeared only once, while the bits in twos represent bits that appeared three times (which is not possible).
# In summary, the algorithm uses bit manipulation to efficiently keep track of the counts of each bit position. By utilizing XOR and AND operations, it can identify the bits of the single number that appears only once in the array while ignoring the bits that appear multiple times.

# class Solution:
#   def singleNumber(self, nums: List[int]) -> int:
#     ones = 0
#     twos = 0

#     for num in nums:
#       ones ^= (num & ~twos)
#       twos ^= (num & ~ones)

#     return ones