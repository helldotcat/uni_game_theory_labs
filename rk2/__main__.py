import random

# random.seed(4)
random.seed(8)

matrix = []
size = 4

for i in range(size):
    a = [random.randrange(0, 1000) for _ in range(size)]
    matrix.append([x/sum(a) for x in a])

for i in range(size):
    print('[' + ', '.join(['{0:.3f}'.format(x) for x in matrix[i]]) + ']')

# trimmed_matrix = [
#     [0.173, 0.222, 0.075, 0.530],
#     [0.354, 0.428, 0.138, 0.080],
#     [0.064, 0.019, 0.387, 0.530],
#     [0.331, 0.104, 0.289, 0.276],
# ]

trimmed_matrix = [
    [0.117, 0.191, 0.497, 0.195],
    [0.118, 0.181, 0.661, 0.040],
    [0.066, 0.107, 0.193, 0.634],
    [0.288, 0.119, 0.228, 0.365],
]


# x = [5, 14, 1, 8]

x = [3, 14, 7, 5]

# x[0] = 9
# x[1] = 2
# x[3] = 9


print(x)
for i in range(size):
    print(sum([trimmed_matrix[i][j] * x[j] for j in range(size)]))
#
# for j in range(size):
#     col = [trimmed_matrix[i][j] for i in range(size)]
#     print(sum([col[::-1][i] * x[i] for i in range(size)]))
