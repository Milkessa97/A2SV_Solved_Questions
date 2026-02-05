class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for path in paths:
            path = path.split()
            root = path[0]
            for fl in path[1:]:
                name,content = fl.split("(")
                store[content].append(root+'/'+name)
        print(store)
        res = []
        for key in store:
            if len(store[key]) > 1:
                res.append(store[key])
        return res