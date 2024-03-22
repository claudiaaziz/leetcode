class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
    




class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = { course: [] for course in range(numCourses) }

        # Add all the courses and their prereq into a hash map.
        for curr, pre in prerequisites:
            course_map[curr].append(pre)
        
        # Keep track of the courses that has been visited.
        visit_set = set()

        def dfs(crs):
            # Base cases
            # Cycle
            if crs in visit_set:
                return False
            # No prereq
            if course_map[crs] == []:
                return True
            
            # Add the course that has prereq to set
            visit_set.add(crs)

            # Go through all the prereqs, make sure there's no cycle or it eventually
            # reaches a no prereq course.
            for pre in course_map[crs]:
                if dfs(pre) == False:
                    return False

            # Backtrack by removing the current course.
            visit_set.remove(crs)

            # Set the current course to [] because we know it works so it will hit
            # the True base case.
            course_map[crs] = []

            return True
        
        # Have to account for disconnected courses.
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True
        
