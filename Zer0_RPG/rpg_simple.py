dados_personagens = {
    "jogadores": [
            {"id":1 ,"nome": "guerreiro", "level": 1, "hp": 200, "hp_max": 200, "dano": 15},
            {"id":2, "nome": "mago", "level": 1, "hp": 100, "hp_max": 100, "dano": 30}
        ],
        "inimigos": [
            {"id":1 ,"nome": "goblin", "level": 1, "hp": 100, "hp_max": 100, "dano": 15},
            {"id":2 ,"nome": "bruxa", "level": 1, "hp": 90, "hp_max": 90, "dano": 20}
        ]
    }
jogador = dados_personagens["jogadores"]
inimigo  = dados_personagens["inimigos"]


def exibir_personagens_id(dados_personagens, id_busca):
    for personagem in dados_personagens:
        if personagem["id"] == id_busca :
            exibir_informacoes_personagens(jogador)
        elif personagem["id"] == id_busca:
            exibir_informacoes_personagens(inimigo)
        return
    print("Personagem não encontrado!")

def exibir_informacoes_personagens(dados_personagens):
    for personagem in dados_personagens:
        print(f"Nome: {personagem['nome']} // Level: {personagem['level']} // hp: {personagem['hp']} // dano: {personagem['dano']}")

# exibir_informacoes_personagens(inimigo)
# exibir_informacoes_personagens(jogador)
exibir_personagens_id(jogador, 2)
# exibir_personagens_id(inimigo, 2)



