class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_neg = False
        num = 0

        if len(s) == 0:
            return num
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            else:
                break

        if i == len(s):
            return num

        if not s[i].isdigit() and s[i] not in ['+', '-']:
            return num
        elif s[i] in ['+', '-']:
            if s[i] == '-':
                is_neg = True
            if i+1 < len(s) and s[i+1].isdigit():
                num_start = i+1
            else:
                return num
        else:
            num_start = i

        num = ''
        while num_start < len(s):
            if s[num_start].isdigit():
                num += s[num_start]
                num_start += 1
            else:
                break

        n = 0
        for i in range(len(num)):
            n += 10**(len(num)-1-i)*int(num[i])

        if is_neg and n > 2**31:
            n = 2**31
        elif not is_neg and n > 2**31 - 1:
            n = 2**31 - 1

        if is_neg:
            return -n
        else:
            return n
