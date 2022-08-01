"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return
        new = {node: Node(node.val)}
        queue = [node]
        visited =  set()
        
        while queue:
            curr = queue.pop(0)
            if curr in visited:
                continue
            
            visited.add(curr)
            for n in curr.neighbors:
                if n not in new:
                    new[n] = Node(n.val)
                    queue.append(n)
                # copy over neighbors of curr into new graph
                new[curr].neighbors.append(new[n])
                
        return new[node]
                
        
        