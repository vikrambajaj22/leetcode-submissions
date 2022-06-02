class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry_one = False
        res = ''
        
        a_len, b_len = len(a), len(b)
        
        if a_len < b_len:
            a = '0' * (b_len - a_len) + a
        if b_len < a_len:
            b = '0' * (a_len - b_len) + b
            
        for i in range(len(a)-1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                if carry_one:
                    res += '1'
                else:
                    carry_one = True
                    res += '0'
            elif (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
                if carry_one:
                    res += '0'
                else:
                    res += '1'
            else:
                if carry_one:
                    res += '1'
                    carry_one = False
                else:
                     res += '0'
                        
        res = ''.join(reversed(res))
        if carry_one: res = '1' + res
        return res