class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0 # means sign not yet found.
        # we don't have to worry about leading zeros because they'll just be n + 0 * 10^x when popping from stack...
        stack = []

        for i in s:
            if i == " ":
                if len(stack) > 0 or sign != 0:
                    break
                continue
            
            if i == "-":
                if sign != 0:
                    break # not allowed to have two signs in string.
                if len(stack) > 0:
                    # not allowed to have sign if we already in the middle of parsing.
                    break
                sign = -1
                continue
            
            if i == "+":
                if sign != 0:
                if len(stack) > 0:
                    break
                sign = 1
                continue
            
            if i.isalpha() or i == ".":
                break

            if i.isdigit():
                stack.append(i)


        if sign == 0:
            sign = 1

        n = 0
        multiplier = 1
        while len(stack) > 0:
            i = stack.pop()
            n += (multiplier * int(i))
            multiplier *= 10
        
        res = n * sign
        if res < (int)(-2 ** 31):
            res = (int)(-2 ** 31)
        if res > (int)((2 ** 31) -1):
            res = (int)((2 ** 31) -1)
        return res 
            
            
            
            


        