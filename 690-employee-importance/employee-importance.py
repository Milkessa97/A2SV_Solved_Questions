"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        importance = {}
        for employee in employees:
            graph[(employee.id,employee.importance)].extend(employee.subordinates)
            importance[employee.id] = employee.importance

        total_importance = 0

        def dfs(node):
            nonlocal total_importance
            total_importance += node[1]
            for sub in graph[node]:
                dfs(tuple([sub,importance[sub]]))
            
        for employee in employees:
            if employee.id == id:
                dfs(tuple([employee.id,employee.importance]))
                break
        
        return total_importance