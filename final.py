from queue import Queue

def print_matriz(matriz):
    for linha in matriz:
        print(linha)
    print()

def verifica_se_esta_sujo(matriz):
    # Retorna True caso tenha um sujo na matriz 
    for linha in matriz:
        if "sujo" in linha:
            return True
    return False

def move(posicao_atual, nova_posicao, matriz):
    # faz um movimento do aspirador da posicao_atualição atual para uma nova posicao_atualição e limpa o local antigo.
    acoes = " "
    if posicao_atual[0] > nova_posicao[0]:
        acoes = "cima"
    elif posicao_atual[0] < nova_posicao[0]:
        acoes = "baixo"
    elif posicao_atual[1] > nova_posicao[1]:
        acoes = "esquerda"
    elif posicao_atual[1] < nova_posicao[1]:
        acoes = "direita"
    
    matriz[posicao_atual[0]][posicao_atual[1]] = "limpo"
    matriz[nova_posicao[0]][nova_posicao[1]] = "aspirador"
    
    print(f"O aspirador estava na posição {posicao_atual} e {matriz[posicao_atual[0]][posicao_atual[1]]}. Ação: foi para {acoes}.")
    print_matriz(matriz)
    return nova_posicao

def bfs(posicao_do_aspirador, matriz):
    queue = Queue()
    queue.put(matriz)
    visitado = {str(matriz): True}
    
    while verifica_se_esta_sujo(matriz):
        estado_atual = queue.get()
        for i in range(len(estado_atual)):
            for j in range(len(estado_atual[i])):
                if (estado_atual[i][j] == "sujo"):
                    nova_posicao = [i, j]
                    if (posicao_do_aspirador[0] == nova_posicao[0] and posicao_do_aspirador[1] < nova_posicao[1]):
                        # move o aspirador pora direita
                        while (posicao_do_aspirador != nova_posicao):
                            posicao_do_aspirador = move(posicao_do_aspirador, [posicao_do_aspirador[0], posicao_do_aspirador[1]+1], matriz)
                    elif (posicao_do_aspirador[0] == nova_posicao[0] and posicao_do_aspirador[1] > nova_posicao[1]):
                        # move o aspirador para esquerda
                        while (posicao_do_aspirador != nova_posicao):
                            posicao_do_aspirador = move(posicao_do_aspirador, [posicao_do_aspirador[0], posicao_do_aspirador[1]-1], matriz)
                    elif (posicao_do_aspirador[1] == nova_posicao[1] and posicao_do_aspirador[0] < nova_posicao[0]):
                        # move o aspirador para baixo
                        while (posicao_do_aspirador != nova_posicao):
                            posicao_do_aspirador = move(posicao_do_aspirador, [posicao_do_aspirador[0]+1, posicao_do_aspirador[1]], matriz)
                    elif (posicao_do_aspirador[1] == nova_posicao[1] and posicao_do_aspirador[0] > nova_posicao[0]):
                        # move o aspirador para cima
                        while (posicao_do_aspirador != nova_posicao):
                            posicao_do_aspirador = move(posicao_do_aspirador, [posicao_do_aspirador[0]-1, posicao_do_aspirador[1]], matriz)
                    if (str(matriz) not in visitado):
                        queue.put(matriz)
                        visitado[str(matriz)] = True

def get_sujo(matriz):
    sujos = []
    for linha in matriz:
        if "sujo" in linha:
            for elemento in linha:
                if elemento == "sujo":
                    sujos.append(elemento)
    return sujos

ambiente = [
            ["sujo","sujo","limpo"],
            ["limpo","aspirador","sujo"],
            ["sujo","limpo","sujo"]
            ]

sujos = get_sujo(ambiente)
inicio = len(sujos)

posicao_do_aspirador = [1,1]
bfs(posicao_do_aspirador, ambiente)

sujos = get_sujo(ambiente)

desepenho = (inicio / 5) * 100

print(f"desempemho do agente {desepenho}%") 