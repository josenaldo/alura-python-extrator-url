import re


class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.parametros = self.__parse_parametros()

    def __str__(self):
        return self.url

    # noinspection PyMethodMayBeStatic
    def sanitiza_url(self, url):
        if not url:
            raise ValueError("A URL está Vazia")
        else:
            return url.strip()

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está Vazia")

        padrao = '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio'
        padrao_url = re.compile(padrao)
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError(f"A URL {self.url} não é válida")

    def __parse_parametros(self):
        url_parametros = self.get_url_parametros()
        parametros_separados = url_parametros.split('&')
        parametros = {}

        for param in parametros_separados:
            indice_igual = param.find('=')

            chave = param[:indice_igual]
            valor = param[indice_igual + 1:]

            parametros[chave] = valor

        return parametros

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:len(self.url)]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        if(parametro_busca in self.parametros):
            return self.parametros[parametro_busca]
        else:
            return None


nova_url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(nova_url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

url_validas = [
    'bytebank.com/cambio',
    'bytebank.com.br/cambio',
    'www.bytebank.com/cambio',
    'www.bytebank.com.br/cambio',
    'http://www.bytebank.com/cambio',
    'http://www.bytebank.com.br/cambio',
    'https://www.bytebank.com/cambio',
    'https://www.bytebank.com.br/cambio',
]

url_invalidas = [
    'https://bytebank/cambio',
    'ht:bytebank.naoexiste/cambio',
    'http://bytebank.naoexiste/cambio',
]

for valida in url_validas:
    try:
        extrator = ExtratorURL(valida)
        print(f'Url válida: {extrator}')
    except ValueError as error:
        print(f'Erro corretamente encontrado: {error}')

for invalida in url_invalidas:
    try:
        extrator = ExtratorURL(invalida)
        print(f'Essa URL não deveria ser impressa: {extrator}')
    except ValueError as error:
        print(f'Erro corretamente encontrado: {error}')
