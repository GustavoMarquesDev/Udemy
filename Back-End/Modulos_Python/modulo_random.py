import random

'''
QUEBRA A ALEATORIEDADE DOS NÚMEROS
random.seed(0)
'''
# gera um número aleatório entre 0 e 8 (com passo de 2 em 2)
r_range = random.randrange(0, 8, 2)
# print(r_range)

# gera um número aleatório entre 0 e 8 (sem passo)
r_int = random.randint(0, 8)
# print(r_int)

# gera um número aleatório entre 0 e 8 de ponto flutuante (sem passo)
r_uniform = random.uniform(0, 8)
# print(r_uniform)

nomes = ['Gustavo', 'Pedro', 'Maria', 'Marta']

# embaralha o iteravel original
random.shuffle(nomes)
# print(nomes)

# escolhe 3 nomes aleatoriamente e retorna outro iteravel(não repete valores)
novos_nomes = random.sample(nomes, 3)
# print(novos_nomes)


# escolhe 3 nomes aleatoriamente e retorna outro iteravel(repete valores)
novos_nomes = random.choices(nomes, k=3)
# print(novos_nomes)


# escolhe um nome aleatoriamente do iteravel
print(random.choice(nomes))
