from Board import Board
from Piece import Piece
import random

#Game Manager class based on EL Tetris AI
class GameManager():
    #Calculate the best move 
    def move(self, working_piece, board, idx, args):
        best = None
        bestScore = None
        workingPiece = working_piece[idx]

        _HEIGHT_WEIGHT = args[0]
        _LINE_WEIGHT = args[1]
        _HOLE_WEIGHT = args[2]
        _BUMP_WEIGHT = args[3]

        rotation_range = 4
        if workingPiece.num/4 == 4:
            rotation_range = 1
        elif int(workingPiece.num/4) == 0 or int(workingPiece.num/4) == 5 \
            or int(workingPiece.num/4) == 6:
            rotation_range = 2

        for rotation in range(rotation_range):
            _piece = workingPiece.clone()
            for i in range(rotation):
                _piece.rotate()

            while _piece.move_left(board.board):
                continue

            while board.valid(_piece):
                _pieceSet = _piece.clone()
                _grid = Board(board)
                _grid.add_piece_to_board(_pieceSet, _pieceSet.get_position())
                score = None
                #If reaches the last element in working_pieces, return the score
                if idx == len(working_piece)-1:
                    sum_height, max, sum_height_modified = _grid.height()
                    line_weight = _LINE_WEIGHT
                    bump_weight = _BUMP_WEIGHT
                    score = _HEIGHT_WEIGHT*sum_height + line_weight * _grid.num_line() + \
                            _HOLE_WEIGHT*_grid.number_of_holes() +  bump_weight*_grid.bumpiness()
                #Else use recursion to get to the last piece 
                else:
                    score, _best = self.move(working_piece, _grid, idx+1, args)
                
                if score == None: score = -1000
                if bestScore == None or score > bestScore:
                    bestScore = score
                    best = _piece.clone()

                _piece.y+=1

        return bestScore, best

    #Process the working pieces
    def process(self, working_piece, board, args):
        piece = working_piece[0]
        score, best_piece = self.move(working_piece, board, 0, args)
        if best_piece == None:
            board.gg()
        try:
          final_index = best_piece.y
          idx = final_index - piece.y
        except Exception:
            return False
        rotation = 0
        while piece.num!=best_piece.num:
            piece.rotate()
            rotation+=1
        board.add_piece_to_board(piece, (final_index, 3))
        board.clear_lines()
        self.command(rotation, idx)
        return True
      
    #Print the command of the move
    def command(self,final_rotation, num_move): 
      self.partial_command.append('N')
      if final_rotation>0:
        self.partial_command.append('C'+str(final_rotation))
      if num_move < 0:
        self.partial_command.append('L'+str(abs(num_move)))
      elif num_move > 0: 
        self.partial_command.append('R'+str(abs(num_move)))
      self.partial_command.append('D20')

    #If fail, try new params
    def reset_args(self):
        HEIGHT_WEIGHT = -4.500158825082766
        LINE_WEIGHT = 3.4181268101392694
        HOLE_WEIGHT = -7.899265427351652
        BUMP_WEIGHT = -3.2178882868487753
        h = HEIGHT_WEIGHT + (random.random() - 0.5)*2 
        l = LINE_WEIGHT + (random.random() - 0.5) *2
        hole = HOLE_WEIGHT + (random.random() - 0.5)*2 
        b = BUMP_WEIGHT + (random.random() - 0.5) *2
        return [h,l,hole,b]

    def run(self):
        board = Board()
        THRESHHOLD = 35
        f = open('sequence.txt', 'r')
        lines = f.readlines()
        l = [int(_) for _ in lines]
      
        back_up = Board(board)
        back_back = Board(board)
        args = self.reset_args()
        curr = 0
        last = 0
        last_last = 0
        final_command = []
        last_command = []
        self.partial_command = []
        fail_time = 0
        step_size = 200
        max_fail = 10

        while True:
            if fail_time==max_fail:
              print('fail time more than {}, rewinding: {}'.format(max_fail, last_last))
              last = last_last
              curr = last_last
              fail_time = 0
              board = Board(back_back)
              back_up = Board(back_back)
              final_command = last_command.copy()
              self.partial_command = []
              args = self.reset_args() 

            if curr%step_size == 0 and curr>last:
              if board.score/curr >= THRESHHOLD or fail_time > max_fail:
                THRESHHOLD=max(40, board.score/curr - 3)
                if fail_time < max_fail: 
                  back_back = Board(back_up)
                fail_time=0   
                back_up = Board(board)
                last_last = last
                last = curr
                last_command = final_command.copy()
                final_command.append(self.partial_command.copy())
                self.partial_command = []
                print('Get This Part Done! ', board.score/curr, ' Continue at: ', curr)
                print('This part args: ', args)
              else:
                fail_time+=1
                put = 0
                if board.score>0:
                  put = board.score/curr
                print('AHH Almost! ', put,' Threshold: ', THRESHHOLD,' restart at: ', last)
                board = Board(back_up)
                print(board.score)
                curr = last
                self.partial_command = []
                args = self.reset_args()  

            i = curr
            if i >= 9999:
                print('Finish!!')
                f = open('result.txt', 'w')
                final_command.append(self.partial_command.copy())
                f.write(str(final_command))
                f.close()
                print(board.score)
                print(final_command)
                return board.score 
                            
            if curr < len(l)-1:
                n = l[curr]
                k = l[curr+1]
                curr+=1
            else:
               print('Finish!!')
               f = open('result.txt', 'w')
               final_command.append(self.partial_command.copy())
               f.write(str(final_command))
               f.close()
               print(board.score)
               print(final_command)
               return board.score

            working_piece = [Piece(n), Piece(k)]

            count = 0
            self.process(working_piece, board, args)

            if board.gg():
                fail_time+=1
                board = Board(back_up)
                print('Fail Attempt at {}! restart at: {}'.format(curr, last))
                curr = last
                self.partial_command = []
                args = self.reset_args()

        return board.score


if __name__ == '__main__':
    GM = GameManager()

    print('Now Starting:')
    score = GM.run()

    print('ALL FINISH')
    