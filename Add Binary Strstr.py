class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        
        len_a, len_b = len(a), len(b)
        if len_a < len_b:
            a = a + "0" * (len_b - len_a)
        elif len_b < len_a:
            b = b + "0" * (len_a - len_b)
            
        result, carry = [], 0
        for i in range(len(a)):
            sum_ = ord(a[i]) - ord("0") + ord(b[i]) - ord("0") + carry
            carry = sum_// 2
            result.append(str(sum_% 2))
            
        if carry:
            result.append(1)
        return "".join([str(x) for x in result[::-1]])
        
