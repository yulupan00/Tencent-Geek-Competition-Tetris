#Board class
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

class Board():
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20
    score = 0

    def __init__(self, *args):
        if len(args) == 0:
            self.board = [[0] * 10 for _ in range(BOARD_HEIGHT)]
        else:
            self.board = [l.copy() for l in args[0].board]

    def add_piece_to_board(self, piece, pos):
        piece.x = pos[1]
        piece.y = pos[0]
        while piece.move_down(self.board):
            continue
        for (x, y) in piece.get_curr_piece():
            self.board[y + piece.x][x + piece.y] = 1

    def clear_lines(self):
        lines_to_clear = [index for index, row in enumerate(
            self.board) if sum(row) == BOARD_WIDTH]
        #Rough estimate of score
        if len(lines_to_clear) == 1:
            self.score += 40
        elif len(lines_to_clear) == 2:
            self.score += 100
        elif len(lines_to_clear) == 3:
            self.score += 300
        elif len(lines_to_clear) == 4:
            self.score += 1200

        if lines_to_clear:
            self.board = [row for idx, row in enumerate(self.board) if idx not in lines_to_clear]
            for _ in lines_to_clear:
                self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])

    def number_of_holes(self):
        holes = 0
        for i in range(10):
            block = False
            for j in range(20):
                if self.board[j][i]!=0:
                    block = True
                elif self.board[j][i] == 0 and block:
                    holes+=1
        return holes

    def col_height(self, j):
        h = 0
        for i in range(20):
            if self.board[i][j] != 0:
                return 20 - i
        return 0

    def bumpiness(self):
        total_bumpiness = 0
        max_bumpiness = 0
        y_store = []
        for col in zip(*self.board):
            i = 0
            while i < BOARD_HEIGHT and col[i] != 1:
                i += 1
            y_store.append(20-i)
        for i in range(len(y_store) - 1):
            bumpiness = abs(y_store[i] - y_store[i+1])
            max_bumpiness = max(bumpiness, max_bumpiness)
            total_bumpiness += abs(y_store[i] - y_store[i+1])
        return total_bumpiness

    def height(self):
        sum_height = 0
        max_height = 0
        min_height = BOARD_HEIGHT

        for col in zip(*self.board):
            i = 0
            while i < BOARD_HEIGHT and col[i] == 0:
                i += 1
            height = BOARD_HEIGHT - i
            sum_height += height
            if height > max_height:
                max_height = height
            elif height < min_height:
                min_height = height
        return sum_height, max_height, min_height

    def is_line(self, i):
        for j in range(10):
            if self.board[i][j] == 0:
                return False
        return True

    def num_line(self):
        count = 0
        for i in range(20):
            if self.is_line(i):
                count += 1
        return count

    def check_collision(self, piece, pos):
        for (x, y) in piece.get_curr_piece():
            x += pos[0]
            y += pos[1]
        if x < 0 or x >= BOARD_WIDTH \
                or y < 0 or y >= BOARD_HEIGHT \
                or self.board[y][x] == 1:
            return True
        return False

    def valid(self, piece):
        for (x, y) in piece.get_curr_piece():
            if piece.y+x>= 10 or piece.y + x < 0 or piece.x + y >= 20:
                return False
            if self.board[piece.x+y][piece.y+x] != 0:
                return False
        return True;

    def gg(self):
        if self.height()[1] >= 17:
            return True
        return False

    def board_stats(self):
        total_bumpiness= self.bumpiness()[0]
        sum_height = self.height()[0]
        return [self.num_line(), self.number_of_holes(), total_bumpiness, sum_height]

    def clone(self):
        return Board(self.board)

    def __str__(self):
        for l in self.board:
            print(l)
