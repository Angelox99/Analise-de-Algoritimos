## 📘 Projeto: Benchmark de Algoritmos de Ordenação

Executa benchmarks de algoritmos de ordenação implementados em C, coleta métricas de desempenho e gera gráficos interativos com Dash/Plotly.

---

### ✅ Pré-requisitos

* Python **3.8+**
* GCC (Linux/macOS) ou MinGW (Windows) para compilar os algoritmos em C
* `make` instalado (Linux/macOS) ou equivalente no Windows

---

### 📦 Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Kaioguilherme1/Analise-de-Algoritimos.git
   cd Analise-de-Algoritimos
   ```

2. **Instale as dependências Python:**

   ```bash
   pip install -r requirements.txt
   ```

---

### 🛠️ Compilando os Algoritmos

1. Navegue até a pasta de algoritmos:

   ```bash
   cd algoritmos
   make
   cd ..
   ```

2. **Windows**: Certifique-se de que os executáveis tenham extensão `.exe` (ex: `bubble_sort.exe`).
   Se necessário, edite o arquivo `benchmark/test.py`:

   ```python
   algoritmos = ['bubble_sort.exe', 'insertion_sort.exe', 'merge_sort.exe', 'quick_sort.exe']
   ```

---

### 🚀 Executando o Benchmark

Execute o script de testes:

```bash
python3 benchmark/test.py
```

* Os resultados serão salvos em `./resultados/resultados.csv`.

---

### 📊 Gerando e Visualizando os Gráficos

Execute o script do gráfico:

```bash
python3 benchmark/grafico.py
```

* Acesse via navegador: [http://localhost:8050](http://localhost:8050)

---

### 📝 Observações

* Logs do benchmark: `benchmark.log`
* Arquivos de entrada: pasta `entradas`
* Binários dos algoritmos: pasta `algoritmos`
