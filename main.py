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

indice_interrogacao = url.find('?')

# quando o primeiro argumento do slice não é passado, o python entende que deve começar na primeira posição
url_base = url[:indice_interrogacao]
print(url_base)  # Vai imprimir “bytebank.com/cambio”

# quando o segundo argumento do slice não é passado, o python entende que pegar até o fim da string
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)
