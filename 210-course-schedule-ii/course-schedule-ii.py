class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [x for x in range(numCourses)]

        map = defaultdict(int)
        graph = defaultdict(list)
        for pre in prerequisites:
            map[pre[0]] += 1
            graph[pre[1]].append(pre[0])

        que = deque([x for x in range(numCourses) if map[x]==0])
        courses = []
        while len(courses) < numCourses:
            if not que:
                return []
            course = que.popleft()
            for key in graph[course]:
                map[key] -= 1
                if map[key] == 0:
                    que.append(key)
            courses.append(course)
        
        return courses
            