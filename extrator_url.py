class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.parametros = self.__parse_parametros()

    # noinspection PyMethodMayBeStatic
    def sanitiza_url(self, url):
        if not url:
            raise ValueError("A URL está Vazia")
        else:
            return url.strip

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está Vazia")

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
        indice_interrogacao = url.find('?')
        url_parametros = url[indice_interrogacao + 1:len(url)]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        if(parametro_busca in self.parametros):
            return self.parametros[parametro_busca]
        else:
            return None


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("coisa")
print(valor_quantidade)
