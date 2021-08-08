import math
TETROMINOS = {
    0: {  # I
        0: [(0, 1), (0, 0), (0, -1), (0, -2)],
        1: [(-1, 0), (0, 0), (1, 0), (2, 0)],
        2: [(0, 1), (0, 0), (0, -1), (0, -2)],
        3: [(-1, 0), (0, 0), (1, 0), (2, 0)],
    },
    1: {  # L
        0: [(0, 0), (0, -1), (0, -2), (1, 0)],
        1: [(0, 0), (0, 1), (1, 0), (2, 0)],
        2: [(-1, 0), (0, 0), (0, 1), (0, 2)],
        3: [(-2, 0), (-1, 0), (0, 0), (0, -1)],
    },
    2: {  # J
        0: [(-1, 0), (0, 0), (0, -1), (0, -2)],
        1: [(0, -1), (0, 0), (1, 0), (2, 0)],
        2: [(1, 0), (0, 0), (0, 1), (0, 2)],
        3: [(-2, 0), (-1, 0), (0, 0), (0, 1)],
    },
    3: {  # T
        0: [(0, 1), (-1, 0), (0, 0), (1, 0)],
        1: [(-1, 0), (0, 0), (0, -1), (0, 1)],
        2: [(0, -1), (-1, 0), (0, 0), (1, 0)],
        3: [(1, 0), (0, 0), (0, -1), (0, 1)],
    },
    4: {  # O
        0: [(0, 0), (0, 1), (1, 1), (1, 0)],
        1: [(0, 0), (0, 1), (1, 1), (1, 0)],
        2: [(0, 0), (0, 1), (1, 1), (1, 0)],
        3: [(0, 0), (0, 1), (1, 1), (1, 0)],
    },
    5: {  # S
        0: [(0, 0), (-1, 0), (0, -1), (1, -1)],
        1: [(-1, 0), (-1, -1), (0, 0), (0, 1)],
        2: [(0, 0), (-1, 0), (0, -1), (1, -1)],
        3: [(-1, 0), (-1, -1), (0, 0), (0, 1)],
    },
    6: {  # Z
        0: [(0, 0), (0, -1), (-1, -1), (1, 0)],
        1: [(-1, 0), (-1, 1), (0, 0), (0, -1)],
        2: [(0, 0), (0, -1), (-1, -1), (1, 0)],
        3: [(-1, 0), (-1, 1), (0, 0), (0, -1)],
    }
}

BOARD_WIDTH = 10
BOARD_HEIGHT = 20


class Piece():
    def __init__(self, num):
        self.num = num
        self.curr_piece = TETROMINOS[int(num/4)][num % 4]
        self.x = 3 #Depth
        self.y = 4 # Width

    def can_move_left(self, grid):
        for (x, y) in self.curr_piece:
            if self.y + x - 1 < 0:
                return False
            if grid[self.x+y][self.y+x-1] != 0:
                return False
        return True

    def move_left(self, grid):
        if self.can_move_left(grid):
            self.y -= 1
            return True
        return False

    def can_move_right(self, grid):
        for (x, y) in self.curr_piece:
            if self.y+x+1 >= 10:
                return False
            if grid[self.x+y][self.y+x+1] != 0:
                return False
        return True

    def move_right(self, grid):
        if self.can_move_right(grid):
            self.y += 1
            return True
        return False

    def can_move_down(self, grid):
        for (x, y) in self.curr_piece:
            if self.x + y + 1 >= 20:
                return False
            if grid[self.x+y+1][self.y+x] != 0:
                return False
        return True

    def move_down(self, grid):
        if self.can_move_down(grid):
            self.x += 1
            return True
        return False

    def rotate(self):
        self.num += 1
        if self.num % 4 == 0:
            self.num -= 4
        self.curr_piece = TETROMINOS[math.floor(self.num/4)][self.num % 4]

    def get_curr_piece(self):
        return self.curr_piece

    def clone(self):
        t = Piece(self.num)
        t.x = self.x
        t.y = self.y
        return t

    def get_position(self):
        return (self.y, self.x)

    def get_str(self):
        for a in self.curr_piece:
            print(a)


if __name__ == '__main__':
    a = Piece(7)
    for i in range(5):
        a.rotate()