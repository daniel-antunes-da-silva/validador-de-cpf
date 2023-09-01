# validador-de-cpf
Esse código é uma função que valida números de CPF (cadastro de pessoa física).

Como funciona?
Ele pode ser usado para validar CPF com entradas de apenas números e também aceita entradas com pontos e traços.
O valor passado precisa ser uma STRING. Ex: '186.300.470-03' ou '18630047003'.

A passagem de parâmetro pode ser o CPF propriamente dito (aceita 1 único).
Ex: 
cpf = '186.300.470-03'
print(valida_cpf(cpf))

Também pode ser utilizado com um input como parâmetro, e uma variável recebendo o valor. Nesse caso, a função tentará transformar para string para que possa ser feita a verificação.
Ex:
situacao = valida_cpf(input('CPF: ')) # aqui o usuário vai digitar o CPF
print(f'Situação: {situacao}')

A função foi atualizada para retornar apenas True ou False. Dessa forma, sempre que houver algum erro no valor passado, retornará como False.

Veja um exemplo de uma lista que foi verificada:

https://github.com/daniel-antunes-da-silva/validador-de-cpf/assets/132831685/a366cd12-0fcc-4d1f-841e-49600698ea25

Perceba que mesmo os valores inválidos são considerados, e os valores de CPF com pontos e traços também são validados.
