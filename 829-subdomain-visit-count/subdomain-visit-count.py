class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)
        for domain in cpdomains:
            freq, dom = domain.split()
            d = dom.split(".")
            for idx in range(len(d)):
                address = '.'.join(s for s in d[idx:])
                count[address] += int(freq)
        res = []
        for key in count.keys():
            res.append(str(count[key])+" "+key)
        return res
                
