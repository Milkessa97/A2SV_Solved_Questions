class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        check = []

        for response in responses:
            response = set(response)
            for res in response:
                check.append(res)

        count = Counter(check).most_common()
        max_count = count[0][1]
        word = count[0][0]

        for pair in count:
            if pair[1]==max_count:
                word=min(word,pair[0])

        return word