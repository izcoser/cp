class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a

        output = [0] * len(a)
        i = len(a) - 1
        carry = False 
        while i >= 0:
            if (int)(a[i]) + (int)(b[i]) == 0:
                if carry:
                    output[i] = 1
                carry = False

            if (int)(a[i]) + (int)(b[i]) == 1:
                if carry:
                    output[i] = 0
                    carry = True
                else:
                    output[i] = 1
                    carry = False
            
            if (int)(a[i]) + (int)(b[i]) == 2:
                if carry:
                    output[i] = 1
                    carry = True
                else:
                    carry = True
            
            i -= 1
        
        if carry:
            return '1' + ''.join(str(i) for i in output)
        return ''.join(str(i) for i in output)
