from random import randint

lista_npc_randon = []

def Criar_monstro():
    level = randint(1, 10)

    novo_npc = {
        "nome" : f"Monstro #{level}",
        "level" : level,
        "hp" : 100 * level,
        "dano" : 20 * level
        }
    lista_npc_randon.append(novo_npc)

def gerar_monstro(n_monstro):

    for x in range(n_monstro):
        Criar_monstro()


jogador = [
    {"nome": "guerreiro", "level": 1, "hp": 200, "hp_max": 200, "dano": 15},
    {"nome": "mago", "level": 1, "hp": 100, "hp_max": 100, "dano": 30}
]
npcs = [
    {"nome" : "goblin", "level" : 1, "hp": 100, "hp_max": 100, "dano": 15},
    {"nome" : "bruxa", "level" : 1, "hp": 90, "hp_max": 90, "dano": 20}
]

def Exibir_npcs(npcs):
    for npc in npcs:
        print(f"Nome: {npc['nome']} // Level: {npc['level']} // hp: {npc['hp']} // dano: {npc['dano']}")

def Exibir_player(jogador):
    for jog in jogador:
        # print(jog["nome"], jog["level"], jog["hp"], jog["dano"]) # posição
        print(f"Nome: {jog['nome']} // Level: {jog['level']} // hp: {jog['hp']} // dano: {jog['dano']}")


gerar_monstro(2)
def Mostrar_monstro():
    for npc in lista_npc_randon:
        print(f"Nome: {npc['nome']} // Level: {npc['level']} // hp: {npc['hp']} // dano: {npc['dano']}")

Mostrar_monstro()
# Exibir_npcs(npcs)
# Exibir_player(jogador)



