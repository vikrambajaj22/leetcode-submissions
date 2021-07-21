class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        else:
            if len(s) == 1:
                return False
            else:
                s_split = list(s)
                g_split = list(goal)

                if s == goal and len(set(s)) < len(s):
                    return True

                count = 0
                indices = []
                for i in range(len(g_split)):
                    if g_split[i] != s_split[i]:
                        count += 1
                        if count > 2:
                            return False
                        indices.append(i)
                if count < 2:
                    return False
                temp = s_split[indices[0]]
                s_split[indices[0]] = s_split[indices[1]]
                s_split[indices[1]] = temp

                return s_split == g_split
