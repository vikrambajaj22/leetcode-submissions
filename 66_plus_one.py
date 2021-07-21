class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        solution = []

        last_digit = digits[-1]

        if last_digit <= 8:
            digits[-1] = last_digit + 1
            return digits
        else:
            # last digit was 9
            carry_one = True
            i = len(digits) - 1
            answer = []
            while carry_one and i >= 0:
                if digits[i] == 9:
                    carry_one = True
                    answer.append(0)
                else:
                    digits[i] += 1
                    carry_one = False
                    break
                i -= 1

            if carry_one:
                # reached beggining (i<0) and still carry one, ex. 999
                answer = [1] + answer
            elif i >= 0:
                # no more carry one, might not have reached beginning i.e. i may be >= 0
                answer = digits[:i+1] + answer

            return answer
