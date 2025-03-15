from funcionario_copy import Funcionario


funcionario = Funcionario('João', 'joao@gmail.com')

funcionario.cadastro_hora('Janeiro', 10)
funcionario.salario_horas['Janeiro'] = 20
funcionario.cadastro_salario_hora('Janeiro', 10)
print(funcionario)
funcionario.calcular_salario('Janeiro')
