# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

# criando funções para realizar os comandos:
#função para listar:
def listar(tarefas):
    print(f'\nTAREFAS: ')
    for item in tarefas:
        print(f'\t{item}')

# função para desfazer:
def desfazer(tarefas, naoTarefas):
    if len(tarefas) == 0:
        print(f'\nNada a desfazer\n')
        return
    item_desfeito = tarefas.pop()
    naoTarefas.append(item_desfeito)

# função para refazer:
def refazer(tarefas, naoTarefas):
    if not naoTarefas:
        print(f'\nNada a refazer\n')
        return
    item_devolvido = naoTarefas.pop()
    tarefas.append(item_devolvido)

# Declarar as listas que serão usadas:
    # Criar a lista de tarefas: 
lista_tarefas = []

    # Criar uma lista com os itens desfeitos:
listas_desfeito = []

# iniciando um loop infinito:
while True:
    # introdução do usuario ao sistema;
    print(f'\nComandos: listar, desfazer, refazer')

    # criar uma lista com os possíveis comandos
    comando = ['listar', 'desfazer', 'refazer', 'clear', 'sair']
    
    # Receber o desejo do usuario:
    comando = input('Digite uma tarefa ou comando: ')

    # tratar o que o usuario digitou:
    # verificar se é uma tarefa ou comando
    if comando not in comando:
        lista_tarefas.append(comando)
        # sendo um comando:
    else: 
        #comando listar:
        if comando == comando[0]:
           listar(lista_tarefas)
        # comando desfazer:
        elif comando == comando[1]:
            desfazer(lista_tarefas, listas_desfeito)
        # comando refazer:
        elif comando == comando[2]:
            refazer(lista_tarefas, listas_desfeito)
        # comando clear
        elif comando == comando[3]:
            os.system('clear')
        # comando sair
        elif comando == comando[4]:
            deseja_sair = input('Você deseja sair: [S]im / [N]ão?')
            if deseja_sair.lower() == 's':
                break
            else:
                continue
        else: 
            print('Não sei como chegou aqui!')

CAMINHO_ARQUIVO = 'exercicio20.json'
