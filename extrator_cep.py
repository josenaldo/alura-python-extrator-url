endereco = 'Rua das Flores, 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23448-120'

import re

# 5 dígitos + hífen + 3 dígitos
padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)