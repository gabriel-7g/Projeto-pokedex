import requests

pokeapi = "https://pokeapi.co/api/v2/pokemon/"

def buscar_pokemon(pokemon):
    url = f"{pokeapi}{pokemon.lower()}"  # Converte o nome para minúsculas
    resposta = requests.get(url)

    if resposta.status_code == 200:  
        dados = resposta.json()

        habilidades = [habilidade["ability"]["name"] for habilidade in dados["abilities"]]

        return dados["name"], habilidades 

nome_pokemon = input("Digite o nome do Pokémon: ")
nome, habilidades = buscar_pokemon(nome_pokemon)


if nome != "Pokémon não encontrado":
    print("Nome do Pokémon:", nome) 
    print("Habilidades:", ", ".join(habilidades))
else:
    print("Pokémon não encontrado")
