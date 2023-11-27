class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        visited = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        def hasCycle(course):
            if visited[course] == 2:
                return False
            if visited[course] == 1:
                return True

            visited[course] = 1

            for prerequisite in graph[course]:
                if hasCycle(prerequisite):
                    return True

            visited[course] = 2
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True
