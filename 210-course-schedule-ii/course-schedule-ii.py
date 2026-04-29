class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [x for x in range(numCourses)]

        count = defaultdict(int)
        graph = defaultdict(list)

        for pre in prerequisites:
            count[pre[0]] += 1
            graph[pre[1]].append(pre[0])

        que = deque([x for x in range(numCourses) if count[x]==0])
        courses = []

        while len(courses) < numCourses:
            if not que:
                return []

            course = que.popleft()
            for key in graph[course]:
                count[key] -= 1
                if count[key] == 0:
                    que.append(key)
                    
            courses.append(course)
        
        return courses
            