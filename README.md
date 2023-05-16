# validador-de-cpf
Esse código, atualmente, é uma função que valida números de CPF (cadastro de pessoa física).

COMO FUNCIONA:
Ele pode ser usado para validar CPF com entradas de apenas números e também aceita entradas com pontos e traços.
No entando, o valor passado precisa ser uma STRING. Ex: '186.300.470-03' ou '18630047003'.

A passagem de parâmetro pode ser o CPF propriamente dito (aceita 1 único).
Ex: 
cpf = '186.300.470-03'
print(valida_cpf(cpf))

Também pode ser utilizado com um input como parâmetro, e uma variável recebendo o valor. Ex:

situacao = valida_cpf(input('CPF: ')) # aqui o usuário vai digitar o CPF
print(f'Situação: {situacao}')
