import os
os.system('cls' if os.name == 'nt' else 'clear')

class RippleEffect:
    def __init__(self, n, groups):
        # validate groups
        self.filled = 0
        self.board = [[0 for i in range(n)] for i in range(n)]
        self.groups = groups

        self.n = n

        self.coord_to_group = {}
        self.groups_to_max_value = {}
        self.groups_to_vals = {}
        for i, group in enumerate(groups):
            for coord in group:
                self.coord_to_group[coord] = i
            self.groups_to_vals[i] = set()
            self.groups_to_max_value[i] = len(group)

    
    def insert(self, r, c, v):
        g = self.coord_to_group[(r, c)]
        if self.board[r][c] == 0:
            self.filled += 1  
        self.board[r][c] = v
        self.groups_to_vals[g].add(v)
    
    def remove(self, r, c, v):
        if self.board[r][c] == 0:
            return
        self.filled -= 1
        g = self.coord_to_group[(r, c)]
        self.groups_to_vals[g].remove(v)
        self.board[r][c] = 0



        
    def solved(self):
        if self.filled != len(self.board)**2:
            return False

        for i, group in enumerate(self.groups):
            max_val = self.groups_to_max_value[i]
            group_set = set()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for r,c in group:
                if self.board[r][c] == 0:
                    continue
                if self.board[r][c] in group_set or self.board[r][c] > max_val:
                    return False
                group_set.add(self.board[r][c])
                for i in range(1, self.board[r][c] + 1):
                    for d in directions:
                        x = r + d[0] * i
                        y = c + d[1] * i
                        if x > 0 and y > 0 and x < len(self.board) and y < len(self.board[0]):
                            if self.board[r][c] == self.board[x][y]:
                                return False

        return True



    def run(self):
        print("Welcome to Ripple Effect!")

        while(not self.solved()):
            print(self)
            print(f"\033[38;5;7mAbove is the current board. What's your next move? ")
            r,c,v = input("r c v: ").split(" ")
            self.insert(int(r), int(c), int(v))

            os.system('cls' if os.name == 'nt' else 'clear')
        print("Solved!")
        print(self)

    
    def __str__(self) -> str:
        return '\n'.join(['\t'.join([f'\033[38;5;{self.coord_to_group[(row, cell)]}m' + str(self.board[row][cell]) for cell in range(len(self.board[row]))]) for row in range(len(self.board))])


