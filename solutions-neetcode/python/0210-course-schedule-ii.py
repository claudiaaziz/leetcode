class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output




class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Add all the courses and their prereq into a hash map.
        course_map = { course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            course_map[course].append(prereq)

        # Keep track of the result, the current path using cycle, and courses that
        # have already been checked using DFS.
        res = []
        cycle = set()
        seen = set()

        def dfs(crs):
            # There's a cycle
            if crs in cycle:
                return False
            # It's already been checked and it works.
            if crs in seen:
                return True

            cycle.add(crs)
            for prereq in course_map[crs]:
                if dfs(prereq) == False:
                    return False

            # Backtrack by removing current course
            cycle.remove(crs)
            # Add current course to seen because it works and current course to 
            # result because all of its prereqs have been recursively added.
            seen.add(crs)
            res.append(crs) 
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return res


        
