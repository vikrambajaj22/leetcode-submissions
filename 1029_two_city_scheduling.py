class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # first compute the cost to send all candidates to city a
        a_cost = sum(c[0] for c in costs)
        
        # then, change the city for half the candidates
        # choosing cities where the difference of costs is smallest
        differences = [b-a for a, b in costs]
        differences = sorted(differences)
        
        return a_cost + sum(differences[:len(differences)//2])