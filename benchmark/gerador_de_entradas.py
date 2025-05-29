import os
import random

# ==========================
# Parâmetros de configuração
# ==========================

# Diretório de saída dos arquivos
OUTPUT_DIR = "./entradas"

# Lista dos tamanhos desejados
tamanhos = [
    50, 100, 500, 1000, 5000, 10000, 15000, 20000,25000,50000,75000,
    100000,150000, 200000,250000, 500000,750000, 1000000
]

# Tipos de ordenação
tipos_ordenacao = ["ordenado", "random", "decrescente"]

def gerar_lista(tamanho: int, tipo: str) -> list:
    if tipo == "ordenado":
        return list(range(1, tamanho + 1))
    elif tipo == "random":
        lista = list(range(1, tamanho + 1))
        random.shuffle(lista)
        return lista
    elif tipo == "decrescente":
        return list(range(tamanho, 0, -1))
    else:
        raise ValueError("Tipo de ordenação inválido: " + tipo)

def salvar_arquivo(lista: list, nome_arquivo: str):
    caminho = os.path.join(OUTPUT_DIR, nome_arquivo)
    with open(caminho, "w") as f:
        for numero in lista:
            f.write(f"{numero}\n")
    print(f"Arquivo gerado: {caminho}")

def gerar_arquivos():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for tamanho in tamanhos:
        for tipo in tipos_ordenacao:
            nome_arquivo = f"entrada_{tamanho}_{tipo}.txt"
            lista = gerar_lista(tamanho, tipo)
            salvar_arquivo(lista, nome_arquivo)

if __name__ == "__main__":
    gerar_arquivos()