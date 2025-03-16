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

    def addBinaryImproved(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        output = []
        carry = 0

        for i in range(max_len - 1, -1, -1):
            total = carry + int(a[i]) + int(b[i])
            output.append(str(total % 2))
            carry = total // 2

        if carry:
            output.append('1')

        return ''.join(output[::-1])