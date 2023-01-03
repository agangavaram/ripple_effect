from game import RippleEffect

class RippleEffectSolver:
    def __init__(self, ripple: RippleEffect):
        self.ripple = ripple
        self.n = self.ripple.n
    
    def is_valid(self, val, r, c):
        g = self.ripple.coord_to_group[(r, c)]
        
        # check if the value is already in the group
        if val in self.ripple.groups_to_vals[g]:
            return False
        
        # check if the value is not already within the "ripple" from current pos
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(1, val + 1):
            for d in directions:
                x = r + d[0] * i
                y = c + d[1] * i
                if x >= 0 and y >= 0 and x < len(self.ripple.board) and y < len(self.ripple.board[0]):
                    if val == self.ripple.board[x][y]:
                        return False
        
        return True
    
    def solve(self):
        def dfs(r, c):
            if r == self.n - 1 and c == self.n:
                return True
            elif c == self.n:
                c = 0
                r += 1
            
            if self.ripple.board[r][c] != 0:
                return dfs(r, c + 1)
            
            group = self.ripple.coord_to_group[(r, c)]
            max_val = self.ripple.groups_to_max_value[group]
            for v in range(1, max_val + 1):
                if not self.is_valid(v, r, c):
                    continue
                self.ripple.insert(r, c, v)
            
                if dfs(r, c + 1):
                    return True
                
                self.ripple.remove(r, c, v)
            
            return False
        
        dfs(0, 0)






