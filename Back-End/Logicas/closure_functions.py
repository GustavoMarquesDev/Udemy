
# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar


# s1 = criar_saudacao('Bom dia')
# s2 = criar_saudacao('Boa noite')
# print(s1('João'))
# print(s2('Maria'))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
print(duplicar(10))
