def valida_cpf(cpf=''):
    from time import sleep
    cpf = cpf.strip()
    primeiro_digito = segundo_digito = 0
    if cpf == '':
        print('CPF não informado')
    elif '.' in cpf or '-' in cpf:
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
    if len(cpf) == 11:
        print('Deixa eu verificar...')
        sleep(1)
    else:
        print('O CPF não tem 11 números.')
    try:
        int(cpf)
    except (TypeError, ValueError):
        print('Erro no tipo ou valor.')
    except Exception as causa:
        print(f'A causa do erro foi {causa.__cause__}')
    else:
        try:
            lista = []
            numeros_docpf = {} # primeiro o peso, depois o número.
            pos = 0
            # compondo o dicionario
            for c in range(10, 1, -1):
                numeros_docpf[c] = str(cpf)[pos]
                pos += 1
            lista.append(numeros_docpf.copy())
            # percorrendo o dicionário dentro da lista
            for k, v in lista[0].items():
                primeiro_digito = primeiro_digito + (k * int(v))
            primeiro_digito %= 11
            if primeiro_digito < 2:
                primeiro_digito = 0
            else:
                primeiro_digito = 11 - primeiro_digito
            numeros_docpf.clear()
            pos = 0
            # compondo outro dicionário
            for c in range(11, 1, -1):
                numeros_docpf[c] = str(cpf)[pos]
                pos += 1
            lista.append(numeros_docpf)
            # percorrendo o outro dicionário dentro da lista.
            for k, v in lista[1].items():
                segundo_digito = segundo_digito + (k * int(v))
            segundo_digito %= 11
            if segundo_digito < 2:
                segundo_digito = 0
            else:
                segundo_digito = 11 - segundo_digito
            print(f'O primeiro digito é ou deveria ser {primeiro_digito} e o segundo {segundo_digito}')
            cpf = str(cpf)
            if (str(primeiro_digito) == cpf[9]) and (str(segundo_digito) == cpf[10]):
                return True
            else:
                return False
        except Exception as erro:
            return erro.__class__


situacao = valida_cpf(input('CPF: '))
print(f'Situação: {situacao}')
print('-'*40)

# from random import randint
# Gera um possível número de CPF aleatório, para testar.
'''aleatorio = randint(10000000000, 99999999999)
print(aleatorio)
print(valida_cpf(str(aleatorio)))'''
