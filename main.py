

# Implementação inicial da Alura
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
print(url)

indice_interrogacao = url.find('?')

# quando o primeiro argumento do slice não é passado, o python entende que deve começar na primeira posição
url_base = url[:indice_interrogacao]
print(url_base)  # Vai imprimir “bytebank.com/cambio”

# quando o segundo argumento do slice não é passado, o python entende que pegar até o fim da string
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)