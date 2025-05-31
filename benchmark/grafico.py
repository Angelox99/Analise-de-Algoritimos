import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# ==============================
# Leitura dos Dados
# ==============================

# Carregar o CSV de resultados (certifique-se de que o arquivo de resultados está atualizado)
df_arm = pd.read_csv("./resultados/resultados(arm).csv")
df_x86 = pd.read_csv("./resultados/resultados(x86).csv")

# muda o nome do processador
df_arm["processador"] = "arm(M1)"
df_x86["processador"] = "x86(i7-14700KF)"

# Concatenar os DataFrames
df = pd.concat([df_arm, df_x86], ignore_index=True)

# Extração do tipo de entrada (Random, Decrescente, Ordenado)
def extrair_tipo(entrada):
    if "random" in entrada:
        return "Random"
    elif "decrescente" in entrada:
        return "Decrescente"
    elif "ordenado" in entrada:
        return "Ordenado"
    else:
        return "Outro"

df["tipo_entrada"] = df["entrada"].apply(extrair_tipo)


# ==============================
# Função para gerar gráficos
# ==============================

def gerar_grafico(tipo, metric):
    df_filtrado = df[df["tipo_entrada"] == tipo].copy()

    # Garante que a métrica é float (números reais)
    df_filtrado[metric] = pd.to_numeric(df_filtrado[metric], errors="coerce")

    # Adiciona coluna com algoritmo + processador
    df_filtrado["algoritmo_proc"] = df_filtrado["algoritmo"] + " (" + df_filtrado["processador"] + ")"

    # Ordenar por tamanho de entrada
    df_filtrado = df_filtrado.sort_values(by="tamanho_entrada")

    fig = px.line(
        df_filtrado,
        x="tamanho_entrada",
        y=metric,
        color="algoritmo_proc",
        markers=True,
        title=f"{metric} - {tipo}",
        labels={
            "tamanho_entrada": "Tamanho da Entrada",
            metric: f"{metric}",
            "algoritmo_proc": "Algoritmo (Processador)"
        }
    )
    return fig

    # Aumentar a resolução do gráfico definindo largura e altura
    fig.update_layout(
        template="plotly_white",
        width=1700,  # Largura do gráfico (em pixels)
        height=800,  # Altura do gráfico (em pixels)
        title_x=0.5  # Centraliza o título
    )
    
    return fig


# ==============================
# App Dash
# ==============================

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = "Dashboard Benchmark Algoritmos"


# ==============================
# Layout com abas
# ==============================

app.layout = dbc.Container([
    html.H1("Dashboard Benchmark de Algoritmos", className="text-center my-4"),
    dbc.Tabs([
        dbc.Tab(label="Random", children=[
            dcc.Graph(id="grafico-random-tempo"),
            dcc.Graph(id="grafico-random-cpu"),
            dcc.Graph(id="grafico-random-memoria"),
            dcc.Graph(id="grafico-random-num-comp")
        ]),
        dbc.Tab(label="Decrescente", children=[
            dcc.Graph(id="grafico-decrescente-tempo"),
            dcc.Graph(id="grafico-decrescente-cpu"),
            dcc.Graph(id="grafico-decrescente-memoria"),
            dcc.Graph(id="grafico-decrescente-num-comp")
        ]),
        dbc.Tab(label="Ordenado", children=[
            dcc.Graph(id="grafico-ordenado-tempo"),
            dcc.Graph(id="grafico-ordenado-cpu"),
            dcc.Graph(id="grafico-ordenado-memoria"),
            dcc.Graph(id="grafico-ordenado-num-comp")
        ])
    ])
], fluid=True)


# ==============================
# Callbacks para atualizar os gráficos
# ==============================

@app.callback(
    Output("grafico-random-tempo", "figure"),
    Output("grafico-random-cpu", "figure"),
    Output("grafico-random-memoria", "figure"),
    Output("grafico-random-num-comp", "figure"),
    Output("grafico-decrescente-tempo", "figure"),
    Output("grafico-decrescente-cpu", "figure"),
    Output("grafico-decrescente-memoria", "figure"),
    Output("grafico-decrescente-num-comp", "figure"),
    Output("grafico-ordenado-tempo", "figure"),
    Output("grafico-ordenado-cpu", "figure"),
    Output("grafico-ordenado-memoria", "figure"),
    Output("grafico-ordenado-num-comp", "figure"),
    Input("grafico-random-tempo", "id")  # Este é apenas um trigger para a atualização
)
def atualizar_graficos(_):
    # Para cada tipo de entrada, gerar gráficos para cada métrica
    fig_random_tempo = gerar_grafico("Random", "tempo_execucao_medio_s")
    fig_random_cpu = gerar_grafico("Random", "cpu_media_percent")
    fig_random_memoria = gerar_grafico("Random", "memoria_media_MB")
    fig_random_num_iter = gerar_grafico("Random", "comparacoes_media")
    
    fig_decrescente_tempo = gerar_grafico("Decrescente", "tempo_execucao_medio_s")
    fig_decrescente_cpu = gerar_grafico("Decrescente", "cpu_media_percent")
    fig_decrescente_memoria = gerar_grafico("Decrescente", "memoria_media_MB")
    fig_decrescente_num_iter = gerar_grafico("Decrescente", "comparacoes_media")
    
    fig_ordenado_tempo = gerar_grafico("Ordenado", "tempo_execucao_medio_s")
    fig_ordenado_cpu = gerar_grafico("Ordenado", "cpu_media_percent")
    fig_ordenado_memoria = gerar_grafico("Ordenado", "memoria_media_MB")
    fig_ordenado_num_iter = gerar_grafico("Ordenado", "comparacoes_media")
    
    return (fig_random_tempo, fig_random_cpu, fig_random_memoria, fig_random_num_iter,
            fig_decrescente_tempo, fig_decrescente_cpu, fig_decrescente_memoria, fig_decrescente_num_iter,
            fig_ordenado_tempo, fig_ordenado_cpu, fig_ordenado_memoria, fig_ordenado_num_iter)


# ==============================
# Executar App
# ==============================

if __name__ == "__main__":
    app.run(debug=True)