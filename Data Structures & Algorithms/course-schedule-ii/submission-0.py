from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # Build graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Start with courses that have no prerequisites
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            # Remove this course as a prerequisite
            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Cycle exists if we couldn't take every course
        if len(order) != numCourses:
            return []

        return order