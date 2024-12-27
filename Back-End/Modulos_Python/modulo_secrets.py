import secrets
import string as s
from secrets import SystemRandom as Sr

# gera uma senha eleatoria
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

random = secrets.SystemRandom()

random.seed(0)  # nao faz nada aqui

# print(secrets.randbelow(100))

# print(secrets.choice(['a', 'b', 'c']))

r_range = random.randrange(0, 8, 2)
# print(r_range)

r_int = random.randint(0, 8)
# print(r_int)

r_uniform = random.uniform(0, 8)
# print(r_uniform)

nomes = ['Gustavo', 'Pedro', 'Maria', 'Marta']

random.shuffle(nomes)
# print(nomes)

novos_nomes = random.sample(nomes, 3)
# print(novos_nomes)

novos_nomes = random.choices(nomes, k=3)
# print(novos_nomes)

print(random.choice(nomes))
