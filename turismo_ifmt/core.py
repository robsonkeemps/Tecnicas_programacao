#TODO:
#Criar esqueleto para dar entrada no ponto turistico;
#Melhorar  read/write

import json
import os
basepath = os.path.dirname(__file__)
filepath = os.path.abspath(os.path.join(basepath, ".", "dados", "base_pontos_turisticos.txt"))

def read():
    with open(filepath, "r") as file:
        return json.loads(file.read())

def write(x):
    with open(filepath,"w") as file:
        try:
            file.write(json.dumps(x))
        except:
            return 0
        else:
            return 1

def update(ponto_turistico):
    x = read()
    y = ponto_turistico
    x['pontos_turisticos'].append(y)
    print(write(x))
        #MELHORAR FUNÇÃO


def delete():
    pass

print(read())
#print(update({"cuiaba1":" cuiaba1 – Um pouco de ar livre no Parque Mãe Bonifácia."}))

#print(update({
#  "cidade": "CUIABA",
##  "descricao": "CAPITAL DO MATO GROSSO",
#    "tipoturismo": "TURISMO DE CULTURA",
#  "pagina": "10"
#}))


