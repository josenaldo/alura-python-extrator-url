#  Minha implementação
url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
print(url)

indice_interrogacao= url.index('?')

base = url[0:indice_interrogacao]
query_string = url[indice_interrogacao+1:len(url)]

print(f'Base: {base}')
print(f'Parametros: {query_string}')

parametros_separados = query_string.split('&')
parametros = {}

for param in parametros_separados:
    indice_igual = param.find('=')

    chave = param[:indice_igual]
    valor = param[indice_igual+1:]

    parametros[chave] = valor

print(f'Parametros: {parametros}')