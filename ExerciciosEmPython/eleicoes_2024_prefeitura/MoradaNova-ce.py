import requests
import json
import pandas as pd

data = requests.get(
    "https://resultados.tse.jus.br/oficial/ele2024/619/dados/ce/ce14753-c0011-e000619-u.json"
)

json_data = json.loads(data.content)
percentual_apuracao = json_data['s']['psi']

candidato = []
partido = []
votos = []
porcentagem = []


for cargo in json_data['carg']:
   for agrupamento in cargo['agr']:
      for partido_info in agrupamento['par']:
         for cand_info in partido_info['cand']:
            candidato.append(cand_info['nm'])
            partido.append(partido_info['sg'])
            votos.append(cand_info['vap'])
            porcentagem.append(cand_info['pvap'])

df_eleicao = pd.DataFrame(list(zip(candidato, partido, votos, porcentagem)), columns = ['Candidato', 'Partido', 'N° de Votos', 'Porcentagem'])

print(f"Percental de apuração: {percentual_apuracao}%")
print(df_eleicao)
