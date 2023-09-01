from random import randint


def valida_cpf(cpf=''):
    from time import sleep
    cpf = cpf.strip()
    primeiro_digito = segundo_digito = 0
    if cpf == '':
        return False
    elif '.' in cpf or '-' in cpf:
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
    if len(cpf) != 11:
        return False
    try:
        int(cpf)
    except (TypeError, ValueError):
        return False
    else:
        try:
            lista = []
            numeros_docpf = {}  # primeiro o peso, depois o número.
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
            cpf = str(cpf)
            if (str(primeiro_digito) == cpf[9]) and (str(segundo_digito) == cpf[10]):
                return True
            else:
                return False
        except Exception as erro:
            return erro.__class__


# Só vai executar esse código abaixo se esse arquivo for executado.
# Sendo assim, a função pode ser utilizada externamente,
if __name__ == '__main__':
    from time import sleep
    lista_de_cpfs = ['397.759.960-74', '42149021064', '12345678911', '', '689.683.960-00', 'abcdefghijk', '20085724041']
    for valor in lista_de_cpfs:
        valor_verificado = valida_cpf(valor)
        print(valor_verificado)
        sleep(0.4)
