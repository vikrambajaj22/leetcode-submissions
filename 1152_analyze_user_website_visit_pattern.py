class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        tuples = sorted(zip(username, website, timestamp),
                        key=lambda x: x[-1])  # sorted by timestamp

        user_visits = {}  # user : [websites visited]

        for (user, website, _) in tuples:
            if user not in user_visits:
                user_visits[user] = []
            user_visits[user].append(website)

        # get unique 3-website combinations for each user, in order automatically since sorted by timestamp
        # and keep adding them to a global list of all user visit combinations

        # we only consider unique combinations per user because it doesn't matter if the user visited the combination multiple times, it still counts as 1 because we want the number of users who visited each combination, regardless of how many times a certain user visited the combination
        user_visits_combinations = []
        for user in user_visits:
            user_visits_combinations.extend(
                set(combinations(user_visits[user], 3)))

        visit_counts = {}

        for combination in user_visits_combinations:
            if combination not in visit_counts:
                visit_counts[combination] = 1
            else:
                visit_counts[combination] += 1

        max_visits = max(visit_counts.values())
        final = []  # list of all combinations with max_visits

        for combination in visit_counts:
            if visit_counts[combination] == max_visits:
                final.append(combination)

        return sorted(final)[0]  # lexicographical order
