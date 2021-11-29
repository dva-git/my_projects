class Sudoku:
    def __init__(self, a):
        self.a = a

    def display(self):
        for i in range(len(self.a)):
            if i % 3 == 0 and i != 0:
                print('-----------------------')
            for j in range(len(self.a)):
                if j % 3 == 0 and j != 0:
                    print(' | ', end='')

                if j == 8:
                    print(self.a[i][j])
                else:
                    print(self.a[i][j], end=' ')

    def find_empty(self):
        for i in range(len(self.a)):
            for j in range(len(self.a)):
                if self.a[i][j] == 0:
                    return (i, j)
        return False

    def valid(self, n, pos):
        for i in range(len(self.a)):
            if self.a[pos[0]][i] == n and i != pos[1]:
                return False

        for j in range(len(self.a)):
            if self.a[j][pos[1]] == n and j != pos[0]:
                return False

        for k in range(pos[0] - pos[0] % 3, pos[0] + 2 - pos[0] % 3):
            for p in range(pos[1] - pos[1] % 3, pos[1] + 2 - pos[1] % 3):
                if self.a[k][p] == n and (k, p) != pos:
                    return False
        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
            for i in range(1, 10):
                if self.valid(i, (row, col)):
                    self.a[row][col] = i

                    if self.solve():
                        return True

                    self.a[row][col] = 0

    def check_if_solved(self):
        for i in range(len(self.a)):
            var = set()
            for j in range(len(self.a)):
                var.add(self.a[i][j])
            if len(var) != len(self.a):
                return False

        for i in range(len(self.a)):
            var = set()
            for j in range(len(self.a)):
                var.add(self.a[j][i])
            if len(var) != len(self.a):
                return False
        b = 0
        d = 0
        for i in range(len(self.a)):
            var = set()
            if i % 3 == 0:
                d = b // 9 * 3
            for k in range(d, d + 3):
                for j in range(b % 9, b % 9 + 3):
                    var.add(self.a[k][j])
            if len(var) != len(self.a):
                return False
            b += 3

        return True

    def main(self):
        print('Given Sudoku Board:\n')
        self.display()
        print()
        self.solve()
        print('Solved Sudoku Board:\n')
        self.display()
        print()
        if self.check_if_solved():
            print('Sudoku is solved correct')
        else:
            print('Something went wrong')


if __name__ == '__main__':
    a = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    s = Sudoku(a)
    s.main()





