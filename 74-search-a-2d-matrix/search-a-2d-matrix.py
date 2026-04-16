class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:

            md = (start + end) // 2
            if target < matrix[md][0]:
                end = md -1
            elif target > matrix[md][-1]:
                start = md + 1

            else:
                left = 0
                right = len(matrix[0]) - 1

                while left <= right:
                    middle = (left + right) // 2
                    if target < matrix[md][middle]:
                        right = middle - 1
                    elif target > matrix[md][middle]:
                        left = middle + 1
                    else:
                        return True
                break

        return False