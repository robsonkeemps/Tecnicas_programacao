#Filtrar a busca do item pelo nome do ponto turistico ou outras opções,
import json
import os
from fuzzywuzzy import fuzz
basepath = os.path.dirname(__file__)
filepath = os.path.abspath(os.path.join(basepath, ".", "dados", "base_pontos_turisticos.txt"))
def similar(pergunta):
    ratio = 0
    with open(filepath, "r") as file:
        lista = json.loads(file.read())
        for item in lista["pontos_turisticos"]:
            thisRatio =  fuzz.ratio(pergunta,item)
            if thisRatio > ratio:
                ratio = thisRatio
                resposta = item
    return(resposta)
#Pergunta dos Itens que esta na Base
#similar("igrejas em cuiaba")