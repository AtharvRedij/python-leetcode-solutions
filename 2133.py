class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            row_seen = set()
            col_seen = set()

            for j in range(n):
                if matrix[i][j] in row_seen:
                    return False
                else:
                    row_seen.add(matrix[i][j])

                if matrix[j][i] in col_seen:
                    return False
                else:
                    col_seen.add(matrix[j][i])

        return True
