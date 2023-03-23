class Solution:
    def does_col_contains_one(self, mat, col_index):
        second_one_found = False
        for i in range(len(mat)):
            if mat[i][col_index] == 1:
                if second_one_found:
                    return True
                else:
                    second_one_found = True

        return False

    def does_row_contains_one(self, mat, row_index):
        second_one_found = False
        for j in range(len(mat[0])):
            if mat[row_index][j] == 1:
                if second_one_found:
                    return True
                else:
                    second_one_found = True

        return False

    def numSpecial(self, mat: List[List[int]]) -> int:
        sp_pos = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and self.does_row_contains_one(mat, i) is False and self.does_col_contains_one(mat, j) is False:
                    sp_pos += 1

        return sp_pos
