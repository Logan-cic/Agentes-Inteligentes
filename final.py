from queue import Queue
import time


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
    print("__________________________________________\n")
    print("estado atual\n")
    for x in matriz:
        print(x)
    print()
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
    
    # print(f"O aspirador estava na posição {posicao_atual} e {matriz[posicao_atual[0]][posicao_atual[1]]}. Ação: foi para {acoes}.")
    print(f"O aspirador foi para a posição {posicao_atual}. Ação: foi para {acoes}.")
    print()
    print_matriz(matriz)
    
    return nova_posicao

def bfs(posicao_do_aspirador, matriz):
    fila = Queue()
    fila.put(matriz)
    visitado = {str(matriz): True}
    custo = 0
    inicio = time.time()
    while verifica_se_esta_sujo(matriz):
        estado_atual = fila.get()
        for i in range(len(estado_atual)):
            for j in range(len(estado_atual[i])):
                if estado_atual[i][j] == "sujo":
                    nova_posicao = [i, j]
                    if posicao_do_aspirador[0] == nova_posicao[0] and posicao_do_aspirador[1] < nova_posicao[1]:
                        # move o aspirador para a direita
                        while posicao_do_aspirador != nova_posicao:
                            posicao_do_aspirador = move(posicao_do_aspirador, [posicao_do_aspirador[0], posicao_do_aspirador[1]+1], matriz)
                            custo += 1
                    elif posicao_do_aspirador[0] == nova_posicao[0] and posicao_do_aspirador[1] > nova_posicao[1]:
                        # move o aspirador para a esquerda
                        while posicao_do_aspirador != nova_posicao:
                            posicao_do_aspirador = move(posicao_do_aspirador, [posicao_do_aspirador[0], posicao_do_aspirador[1]-1], matriz)
                            custo += 1
                    elif posicao_do_aspirador[1] == nova_posicao[1] and posicao_do_aspirador[0] < nova_posicao[0]:
                        # move o aspirador para baixo
                        while posicao_do_aspirador != nova_posicao:
                            posicao_do_aspirador = move(posicao_do_aspirador, [posicao_do_aspirador[0]+1, posicao_do_aspirador[1]], matriz)
                            custo += 1
                    elif posicao_do_aspirador[1] == nova_posicao[1] and posicao_do_aspirador[0] > nova_posicao[0]:
                        # move o aspirador para cima
                        while posicao_do_aspirador != nova_posicao:
                            posicao_do_aspirador = move(posicao_do_aspirador, [posicao_do_aspirador[0]-1, posicao_do_aspirador[1]], matriz)
                            custo += 1
                    if str(matriz) not in visitado:
                        fila.put(matriz)
                        visitado[str(matriz)] = True
    
    fim = time.time()
    # print(f"tempo inicial {inicio} e o tempo final {fim}")
    sujos_limpados = custo
    print("medida de desempenho será o tanto de ações realizadas pelo aspirador")
    print(f"o custo para realizar a limpeza foi de {custo}")
    
sujo_posicoes = []
sujos_limpados = 0
ambiente = [
            ["sujo","sujo","limpo"],
            ["limpo","aspirador","sujo"],
            ["sujo","limpo","sujo"]
            ]

for i in range(len(ambiente)):
    for j in range(len(ambiente[i])):
        if ambiente[i][j] == "sujo":
            sujo_posicoes.append([i, j])

posicao_do_aspirador = [1,1]
bfs(posicao_do_aspirador, ambiente)

num_de_sujos_limpados = (len(sujo_posicoes) - sujos_limpados)

print(f"O numero de posições sujas limpadas foi {num_de_sujos_limpados}")
