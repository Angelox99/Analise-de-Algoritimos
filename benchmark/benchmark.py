import subprocess
import psutil
import os
import logging
import platform
import re

# Configuração de logging
logging.basicConfig(
    filename='benchmark.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Benchmark:
    def __init__(self, bin_dir, entrada_dir):
        self.bin_dir = bin_dir
        self.entrada_dir = entrada_dir
        self.processador = platform.uname().processor

    def run_test(self, algoritmo, arquivo_entrada, num_execucoes=13):
        bin_path = os.path.join(self.bin_dir, algoritmo)

        if not os.path.exists(bin_path):
            logging.error(f"❌ Binário não encontrado: {bin_path}")
            raise FileNotFoundError(f"❌ Binário não encontrado: {bin_path}")

        entrada_path = os.path.join(self.entrada_dir, arquivo_entrada)
        tamanho_entrada = self._extrair_tamanho_entrada(arquivo_entrada)

        tempos = []
        mem_medias = []
        mem_maximas = []
        mem_minimas = []
        cpu_medias = []
        comparacoes = []

        for execucao in range(1, num_execucoes + 1):
            logging.info(f"➡️ Executando {algoritmo} | Entrada: {arquivo_entrada} | Execução: {execucao}")

            process = subprocess.Popen(
                [bin_path, entrada_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            pid = process.pid
            proc = psutil.Process(pid)

            memoria_usos = []
            cpu_usos = []

            while process.poll() is None:
                if not proc.is_running():
                    logging.warning(f"⚠️ Processo {pid} terminou antes da coleta.")
                    break

                try:
                    mem_info = proc.memory_info().rss / (1024 * 1024)
                    cpu = proc.cpu_percent(interval=0.1)
                    memoria_usos.append(mem_info)
                    cpu_usos.append(cpu)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    break

            stdout, stderr = process.communicate()

            comparacoes_valor, tempo_execucao = self._extrair_resultados(stdout)
            if stderr:
                logging.warning(f"⚠️ STDERR capturado na execução {execucao}: {stderr.strip()}")

            tempos.append(tempo_execucao if tempo_execucao is not None else 0)
            mem_medias.append(sum(memoria_usos) / len(memoria_usos) if memoria_usos else 0)
            mem_maximas.append(max(memoria_usos) if memoria_usos else 0)
            mem_minimas.append(min(memoria_usos) if memoria_usos else 0)
            cpu_medias.append(sum(cpu_usos) / len(cpu_usos) if cpu_usos else 0)
            comparacoes.append(comparacoes_valor if comparacoes_valor is not None else 0)

        resultado = {
            "algoritmo": algoritmo,
            "entrada": arquivo_entrada,
            "tamanho_entrada": tamanho_entrada,
            "num_execucoes": num_execucoes,
            "tempo_execucao_medio_s": f"{sum(tempos) / num_execucoes:.6f}" if tempos else "0.000000",
            "memoria_media_MB": f"{sum(mem_medias) / num_execucoes:.6f}" if mem_medias else "0.000000",
            "memoria_maxima_media_MB": f"{sum(mem_maximas) / num_execucoes:.6f}" if mem_maximas else "0.000000",
            "memoria_minima_media_MB": f"{sum(mem_minimas) / num_execucoes:.6f}" if mem_minimas else "0.000000",
            "cpu_media_percent": f"{sum(cpu_medias) / num_execucoes:.6f}" if cpu_medias else "0.000000",
            "comparacoes_media": f"{sum(comparacoes) / num_execucoes:.6f}" if comparacoes else "0",
            "processador": self.processador,
        }

        logging.info(f"✅ Resultado médio para {algoritmo} | {arquivo_entrada}: {resultado}")
        return resultado

    def _extrair_tamanho_entrada(self, nome_arquivo):
        caminho_arquivo = os.path.join(self.entrada_dir, nome_arquivo)
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                num_linhas = sum(1 for _ in arquivo)
            return num_linhas
        except FileNotFoundError:
            logging.error(f"❌ Arquivo de entrada não encontrado: {caminho_arquivo}")
            return None
        except Exception as e:
            logging.error(f"❌ Erro ao contar linhas do arquivo {nome_arquivo}: {e}")
            return None

    def _extrair_resultados(self, stdout):
        comparacoes = None
        tempo_execucao = None
        linhas = stdout.strip().split("\n")
        for linha in linhas:
            match_comp = re.search(r"Comparacoes?:\s*(\d+)", linha)
            if match_comp:
                comparacoes = int(match_comp.group(1))
            match_tempo = re.search(r"Tempo de execucao:\s*(\d+\.\d{6})", linha)
            if match_tempo:
                tempo_execucao = float(match_tempo.group(1))
        return comparacoes, tempo_execucao