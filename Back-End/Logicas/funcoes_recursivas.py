# import sys
# sys.setrecursionlimit(10004)  # Limite de recursividade,


# def recursiva(inicio=0, fim=10):
#     print(inicio, fim)

#     if inicio >= fim:
#         return fim
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0, 20))


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
