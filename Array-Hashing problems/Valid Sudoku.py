# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each 3x3 sub-box must contain the digits 1-9 without repetition.



class Solution:
    def isValidSodoku (self, board: list[list[str]]) -> bool:
        res = set()

        for r in range(9):
            for c in range(9):
                val = board [r][c]

                if val == '.':
                    continue

                r_tag = (r,val)
                c_tag = (c,val)
                box_tag = (r//3, c//3, val)

                if r_tag in res or c_tag in res or box_tag in res:
                    return False
                
                res.add(r_tag)
                res.add(c_tag)
                res.add(box_tag)
                
        return True

    



