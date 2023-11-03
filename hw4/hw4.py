#1
print ('Задание 1')
import numpy as np
vector = np.random.randint(1, 10 + 1, size=10)
sorted_vector = np.sort(vector)
print(vector)
print(sorted_vector, "\n")

#2
print ('Задание 2')
import numpy as np
ch_board = np.zeros((8, 8))
ch_board[1::2, ::2] = 1
ch_board[::2, 1::2] = 1
print(ch_board, "\n")

#3
print ('Задание 3')
import numpy as np
matrix1 = np.random.randint(10, size=(8, 4))
matrix2 = np.random.randint(10, size=(4, 2))
result = np.dot(matrix1, matrix2)
print (matrix1)
print (matrix2)
print(result, "\n")

#4
print ('Задание 4')
import numpy as np
A = np.linspace(0.01, 0.99, 10)
print(A, "\n")

#5
print ('Задание 5')
import numpy as np

def matrix(num):
    multipliers = []
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            quotient = num // i
            if i != 1 and quotient != 1:
                multipliers.append((i, quotient))

    if len(multipliers) == 0:
        print(f"Нельзя разбить число {num} на множители без остатка.")
        return

    print(f"Матрицы с размерностью {num}:")
    for m in multipliers:
        rows, cols = m
        matrix = np.zeros((rows, cols))
        print(matrix)

num = int(input("Введите число элементов в матрице: "))
matrix(num)
print('')

#6
print ('Задание 6')
import numpy as np

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_file(self):
        with open(self.file_path, 'r') as file:
            self.data = np.array(file.read().splitlines())

    def search_text(self, pattern):
        matches = []
        for line in self.data:
            if pattern in line:
                matches.append(line)
        return matches

analyzer = DataAnalyzer('data.txt')

analyzer.read_file()

search_pattern = 'test'
found_matches = analyzer.search_text(search_pattern)

print(found_matches, "\n")

#7
# print ('Задание 7')
# import numpy as np
#
# def forward_propagation(A, S, last=False):
#     B = np.random.randn(S, len(A))
#     result = np.dot(B, A.reshape(-1, 1))
#     row_sums = np.sum(result, axis=1)
#     if last == False:
#         result = np.sin(row_sums)
#     else:
#         result = np.maximum(row_sums, 0)
#     return result, B
#
# A1 = np.random.rand(5)
# output1, B1 = forward_propagation(A1, 10)
#
# A2 = output1
# output2, B2 = forward_propagation(A2, 10)
#
# A3 = output2
# output3, B3 = forward_propagation(A3, 5, True)
#
# output3_percent = output3 * 100
# print(output3_percent)
