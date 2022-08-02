class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # kahn's algo for topological sort
        # topological sort: in a directed acyclic graph, if there is a directed edge u->v, u must appear before v in the ordering
        # kahn's algo: start with nodes that don't have any dependencies (in-degree=0), then remove those nodes from the graph one by one (add them to the ordering), each time reducing the in-degrees of their neighbors; keep doing this until all the nodes are added to the ordering (graph is empty) or a cycle is detected
        # very good video: https://www.youtube.com/watch?v=cIBFEhD77b4
        
        in_degree = {i: 0 for i in range(numCourses)}  # maps course: num_prereqs
        graph = {i: [] for i in range(numCourses)}  # maps prereq: course-list
        
        for i, j in prerequisites:
            # i is the course, j is the prereq
            in_degree[i] += 1
            graph[j].append(i)  # no need to check for duplicates since (i, j)s are unique
        
        queue = [course for course in in_degree if in_degree[course] == 0]
        topological_sort = []
        
        while queue:
            course = queue.pop(0)
            topological_sort.append(course)
            
            # simulate removal from graph by updating in-degrees of neighbors
            # i.e. of courses that depended on it
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    # if in-degree became 0, add it to the queue
                    queue.append(neighbor)
        
        # checking for cycle
        if len(topological_sort) == numCourses:
            # all courses were finished
            return True
        
        return False
