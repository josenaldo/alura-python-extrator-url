url = 'http://www.bytebank.com/cambio'

mensagem = f'f-string em variável: {url}'
print(mensagem)

print(f'f-string direto no print: {url}')

try:
    raise ValueError(f'f-string direto no ValueError: {url}')
except ValueError as error:
    print(error)

try:
    nova_mensagem = f'f-string em variável passada ao ValueError: {url}'
    raise ValueError(nova_mensagem)
except ValueError as error:
    print(error)

raise ValueError(f'f-string direto no ValueError: {url}')