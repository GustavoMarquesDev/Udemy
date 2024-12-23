from itertools import count, combinations, permutations, product

# c1 = count(step=8, start=8)
# r1 = range(8, 100, 8)


# print('count')
# for i in c1:

#     if i > 100:
#         break

#     print(i)

# print()

# print('range')
# for i in r1:
#     print(i)

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print('\n')


pessoas = ['Luiz', 'Otávio', 'Pedro', 'Lucas']

camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino'],
    ['Algodão', 'Poliester']
]

print_iter(combinations(pessoas, 2))  # Não repete a ordem dos elementos
print_iter(permutations(pessoas, 2))  # Repete a ordem dos elementos
print_iter(product(*camisetas))  # Repete a ordem dos elementos
