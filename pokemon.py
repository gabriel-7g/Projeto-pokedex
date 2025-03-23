from flask import Flask, render_template, request
import requests

app = Flask(__name__)

pokeapi = "https://pokeapi.co/api/v2/pokemon/"

def buscar_pokemon(pokemon):
    url = f"{pokeapi}{pokemon.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        nome = dados["name"].capitalize()
        habilidades = [habilidade["ability"]["name"].capitalize() for habilidade in dados["abilities"]]
        imagem = dados["sprites"]["front_default"]
        return nome, habilidades, imagem
    else:
        return None, None, None

@app.route("/", methods=["GET", "POST"])
def index():
    nome = None
    habilidades = None
    imagem = None

    if request.method == "POST":
        nome_pokemon = request.form["pokemon"]
        nome, habilidades, imagem = buscar_pokemon(nome_pokemon)

    return render_template("index.html", nome=nome, habilidades=habilidades, imagem=imagem)

if __name__ == "__main__":
    app.run(debug=True)
