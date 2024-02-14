# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [tuples[i] for i in range(len(tuples)) if len(tuples[i]) != 0]
#
# print(non_empty_tuples)





# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [i[:-1] + (100,) for i in tuples]
# print(new_tuples)





# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# result = []
# for i in range(len(numbers)):
#     total = sum(numbers[i]) / len(numbers[i])
#     result.append(total)
# print(result)





# a, b, c = int(input()), int(input()), int(input())
# x = (-1 * b) / (2 * a)
# y = (4 * a * c - b ** 2) / (4 * a)
# print((x, y))





# n = int(input())
# result = []
# good = []
#
# for _ in range(n):
#     temp = [i for i in input().split()]
#     result.append(tuple(temp))
#
# for i in range(n):
#     print(*result[i], sep=' ')
#     if int(result[i][1]) > 3:
#         good.append(result[i])
#
# print()
# for i in range(len(good)):
#     print(*good[i], sep=' ')





# n = int(input())
# t1, t2, t3 = 1, 1, 1
# for i in range(n):
#     print(t1, end=' ')
#     t1, t2, t3 = t2, t3, t1 + t2 + t3





# n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
# total = (n - x) + (m - x - y) + (k - y) + x + y + z
# print(total)





# n, m, k = int(input()), int(input()), int(input())
# x, y, z = int(input()), int(input()), int(input())
# t, a = int(input()), int(input())
#
# n_m = n + m - t - x
# m_k = m + k - t - y
# n_k = n + k - t - z
#
# one = (n - n_m - n_k - t) + (m - n_m - m_k - t) + (k - n_k - m_k - t)
# two = n_m + n_k + m_k
# nobody = a - (n - n_m - n_k - t) - (m - n_m - m_k - t) - (k - n_k - m_k - t) - n_m - n_k - m_k - t
#
# print(one, two, nobody, sep='\n')

