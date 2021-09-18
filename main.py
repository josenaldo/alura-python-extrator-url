#  Minha implementação
url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
print(url)

question_index = url.index('?')

base = url[0:question_index]
parametros = url[question_index+1:len(url)]

print(f'PATH: {base}')
print(f'QUERY: {parametros}')

# Implementação inicial da Alura
url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

url_base = url[0:19]
print(url_base)  # Vai imprimir “bytebank.com/cambio”

url_parametros = url[20:36]
print(url_parametros)
