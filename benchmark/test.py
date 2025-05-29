from benchmark import Benchmark
import pandas as pd
from tqdm import tqdm
import os

# Configurações
algoritmos = ['bubble_sort', 'insertion_sort', 'merge_sort', 'quick_sort']
entradas = [
    'entrada_50_decrescente.txt',
    'entrada_50_ordenado.txt',
    'entrada_50_random.txt',
    'entrada_100_decrescente.txt',
    'entrada_100_ordenado.txt',
    'entrada_100_random.txt',
    'entrada_500_decrescente.txt',
    'entrada_500_ordenado.txt',
    'entrada_500_random.txt',
    'entrada_1000_decrescente.txt',
    'entrada_1000_ordenado.txt',
    'entrada_1000_random.txt',
    'entrada_5000_decrescente.txt',
    'entrada_5000_ordenado.txt',
    'entrada_5000_random.txt',
    'entrada_10000_decrescente.txt',
    'entrada_10000_ordenado.txt',
    'entrada_10000_random.txt',
    'entrada_15000_decrescente.txt',
    'entrada_15000_ordenado.txt',
    'entrada_15000_random.txt',
    'entrada_20000_decrescente.txt',
    'entrada_20000_ordenado.txt',
    'entrada_20000_random.txt',
    'entrada_25000_decrescente.txt',
    'entrada_25000_ordenado.txt',
    'entrada_25000_random.txt',
    'entrada_50000_decrescente.txt',
    'entrada_50000_ordenado.txt',
    'entrada_50000_random.txt',
    'entrada_75000_decrescente.txt',
    'entrada_75000_ordenado.txt',
    'entrada_75000_random.txt',
    'entrada_100000_decrescente.txt',
    'entrada_100000_ordenado.txt',
    'entrada_100000_random.txt',
    'entrada_150000_decrescente.txt',
    'entrada_150000_ordenado.txt',
    'entrada_150000_random.txt',
    'entrada_200000_decrescente.txt',
    'entrada_200000_ordenado.txt',
    'entrada_200000_random.txt',
    'entrada_250000_decrescente.txt',
    'entrada_250000_ordenado.txt',
    'entrada_250000_random.txt',
    'entrada_500000_decrescente.txt',
    'entrada_500000_ordenado.txt',
    'entrada_500000_random.txt',
    'entrada_750000_decrescente.txt',
    'entrada_750000_ordenado.txt',
    'entrada_750000_random.txt',
    'entrada_1000000_decrescente.txt',
    'entrada_1000000_ordenado.txt',
    'entrada_1000000_random.txt'
]

entradas_curtas = [
    'entrada_50_decrescente.txt',
    'entrada_50_ordenado.txt',
    'entrada_50_random.txt',
    'entrada_100_decrescente.txt',
    'entrada_100_ordenado.txt',
    'entrada_100_random.txt',]

# Inicializar Benchmark
benchmark = Benchmark(
    bin_dir="./algoritmos",
    entrada_dir="./entradas",
)

# Coletar Resultados
resultados = []
os.makedirs("./resultados", exist_ok=True)
csv_path = "./resultados/resultados.csv"

# Calcular total de iterações
total = len(algoritmos) * len(entradas)

# Loop com Barra de Progresso
print("Iniciando Benchmark...")
with tqdm(total=total, desc="Benchmark Progress", unit="test") as pbar:
    for algoritmo in algoritmos:
        for entrada in entradas:
            #print(f" Executando {algoritmo} com {entrada}")
            resultado = benchmark.run_test(
                algoritmo=algoritmo,
                arquivo_entrada=entrada,
            )
            if resultado:
                resultados.append(resultado)
                df = pd.DataFrame(resultados)
                df.to_csv(csv_path, index=False)
            pbar.update(1)

print("Benchmark concluído!")
print(f" CSV salvo em {csv_path}")
