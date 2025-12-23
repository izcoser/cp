# math, easy
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_num_1 = len(num1)
        len_num_2 = len(num2)

        if len_num_1 > len_num_2:
            num2 = ('0' * (len_num_1 - len_num_2)) + num2
            len_num_2 = len_num_1
        elif len_num_2 > len_num_1:
            num1 =  ('0' * (len_num_2 - len_num_1)) + num1
            len_num_1 = len_num_2

        out = ''
        carry = 0
        for i in range(len_num_1 - 1, -1, -1):
            v1, v2 = num1[i], num2[i]
            s = int(v1) + int(v2) + carry

            if s > 9:
                carry = int(str(s)[:-1])
                val = str(s)[-1] 
            else:
                carry = 0
                val = str(s)

            out = val + out

        if carry > 0:
            out = str(carry) + out
        
        return out