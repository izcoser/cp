from typing import List

# https://leetcode.com/problems/closest-prime-numbers-in-range/description/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ps = sieve_of_eratosthenes(left, right)

        closest_pair = [-1, -1]
        closest_diff = 0

        if(len(ps) < 2):
            return closest_pair

        for i in range(len(ps) - 1) :
            n2 = ps[i + 1]
            n1 = ps[i]

            diff = n2 - n1
            if(diff < closest_diff or closest_diff == 0):
                closest_diff = diff
                closest_pair = [n1, n2]

                if diff <= 2: # this difference never decreases below 2.
                    return closest_pair
        
        return closest_pair

        

def sieve_of_eratosthenes(left: int, right: int) -> List[int]:
    is_prime = [True] * (right + 1)
    p = 2
    
    while p * p <= right:
        if is_prime[p]:
            for multiple in range(p * p, right + 1, p):
                is_prime[multiple] = False
        p += 1

    primes = [i for i in range(max(2, left), right + 1) if is_prime[i]]
    return primes
