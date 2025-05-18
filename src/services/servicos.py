from datetime import datetime
import requests


dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

def converter_data_para_dia(data_str):
    data_obj = datetime.strptime(data_str, "%Y-%m-%d")
    return dias_semana[data_obj.weekday()]

def obter_previsao_tempo(cidade, estado, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade},{estado},BR&appid={api_key}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    return resposta.json()


def obter_estados():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    resposta = requests.get(url)
    estados = resposta.json()
    estados_ordenados = sorted(estados, key=lambda x: x["sigla"])
    return estados_ordenados


def obter_cidades(uf):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    resposta = requests.get(url)
    cidades = resposta.json()
    cidades_ordenadas = sorted([cidade["nome"] for cidade in cidades])
    return cidades_ordenadas
