import re

endereco = 'Rua das Flores, 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23448-120'

# 5 dígitos + hífen + 3 dígitos
padrao = re.compile('[0123456789]{5}[-]{0,1}[0123456789]{3}')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)