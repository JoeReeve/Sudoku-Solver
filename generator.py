import random

# https://www.geeksforgeeks.org/program-sudoku-generator/

class Board:
    n = 9
    SRN = 3
    K = 17
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self):
        self.fill_values()
        self.print_sudoku()


    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.SRN)
        self.remove_digits()

    def fill_diagonal(self):
        for i in range(0, self.n):
            self.fill_box(i,i)
            i += self.SRN

    def fill_box(self, row, col):
        for i in range(0,self.SRN):
            for j in range(0,self.SRN):
                num = random.randint(1,9)
                while not self.unused_in_box(row,col,num):
                    self.board[row+i][col+j] = num

    def unused_in_box(self, row_start, col_start, num):
        for i in range(0,self.SRN):
            for j in range(0,self.SRN):
                if self.board[row_start+i][col_start+j] == num:
                    return False
        return True

    def check_if_safe(self, i, j, num): 
        return (self.unused_in_row(i, num) and
                self.unused_in_col(j, num) and 
                self.unused_in_box(i - i % self.SRN, j- j % self.SRN, num))

    def unused_in_row(self, i, num):
        for j in range(0,self.n):
            if self.board[i][j] == num:
                return False
        return True

    def unused_in_col(self, j, num):
        for i in range(0,self.n):
            if self.board[i][j] == num:
                return False
        return True

    def fill_remaining(self, i, j):
        if j>=self.n and i<self.n-1:
            i = i + 1
            j = 0
        if i >= self.n and j >= self.n:
            return True
        if i < self.SRN:
            if j < self.SRN:
                j = self.SRN
        elif i < self.n - self.SRN:
            if j == int((i/self.SRN)*self.SRN):
                j = j + self.SRN
        else:
            if j == self.n - self.SRN:
                i = i + 1
                j = 0
                if i >= self.n:
                    return True
        
        for num in range(1,self.n+1):
            if self.check_if_safe(i,j,num):
                self.board[i][j] = num
                if self.fill_remaining(i, j+1):
                    return True
                self.board[i][j] = 0
        return False

    def remove_digits(self):
        count = self.K
        while count != 0:
            cell_id = random.randint(1, self.n * self.n)
            i = int(cell_id / self.n)
            j = int(cell_id % self.n)
            if j != 0:
                j = j - 1
            
            if self.board[i][j] != 0:
                count = count - 1
                self.board[i][j] = 0

    def print_sudoku(self):
        for i in range(0,self.n):
            for j in range(0,self.n):
                print(self.board[i][j] + " ")
            print()
        print()

    ##def main(self):
    #    sudoku = Board()

  
    ##if __name__ == "__main__":
     #   main()

sudoku = Board()



