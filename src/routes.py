from src import app, API_KEY
from flask import jsonify, render_template, request
from src.services.servicos import converter_data_para_dia, obter_previsao_tempo, obter_estados, obter_cidades


@app.route("/", methods=["GET"])
def index():
    estados = obter_estados()
    return render_template("index.html", estados=estados)
    
@app.route("/api/cidades/<uf>")
def api_cidades(uf):
    cidades = obter_cidades(uf)
    return jsonify(cidades)


@app.route("/previsao", methods=["POST"])
def previsao():
    estado = request.form["estado"]
    cidade = request.form["cidade"]
    dados = obter_previsao_tempo(cidade, estado, API_KEY)
    
    if dados.get("cod") != "200":
        return "Erro ao obter dados. Verifique cidade e estado."

    dias = {}
    for item in dados["list"]:
        data = item["dt_txt"].split()[0]
        if data not in dias:
            dias[data] = []
        dias[data].append(item)

    previsoes = []
    for dia, entradas in dias.items():
        dia_semana = converter_data_para_dia(dia)
        temp_min = min(e["main"]["temp_min"] for e in entradas)
        temp_max = max(e["main"]["temp_max"] for e in entradas)
        umidade = entradas[0]["main"]["humidity"]
        clima = entradas[0]["weather"][0]["description"]
        vento = entradas[0]["wind"]["speed"]
        chuva = entradas[0].get("rain", {}).get("3h", 0.0)
        
        previsoes.append({
            "data": dia,
            "dia_semana": dia_semana,
            "temp_min": round(temp_min, 1),
            "temp_max": round(temp_max, 1),
            "umidade": umidade,
            "clima": clima.capitalize(),
            "vento": vento,
            "chuva": chuva
        })
  
    return render_template("previsao.html", cidade=cidade, estado=estado, previsoes=previsoes)