#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Variável global para contar comparações
long long comparacoes = 0;

// Função de ordenação
void insertion_sort(int *arr, int n) {
    for (int i = 1; i < n; i++) {
        int chave = arr[i];
        int j = i - 1;

        while (j >= 0) {
            comparacoes++; // comparação: arr[j] > chave
            if (arr[j] > chave) {
                arr[j + 1] = arr[j];
                j--;
            } else {
                break;
            }
        }
        arr[j + 1] = chave;
    }
}

// Leitura de arquivo (pode ficar em utils/ler_arquivo.c depois)
int* ler_arquivo(char *nome_arquivo, int *tamanho) {
    FILE *fp = fopen(nome_arquivo, "r");
    if (!fp) {
        perror("Erro ao abrir arquivo");
        exit(1);
    }

    int capacidade = 1000;
    int *vetor = malloc(sizeof(int) * capacidade);
    int valor, count = 0;

    while (fscanf(fp, "%d", &valor) == 1) {
        if (count >= capacidade) {
            capacidade *= 2;
            vetor = realloc(vetor, sizeof(int) * capacidade);
        }
        vetor[count++] = valor;
    }

    fclose(fp);
    *tamanho = count;
    return vetor;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Uso: %s arquivo_entrada.txt\n", argv[0]);
        return 1;
    }

    int n;
    int *arr = ler_arquivo(argv[1], &n);

    comparacoes = 0;
    clock_t inicio = clock();
    insertion_sort(arr, n);
    clock_t fim = clock();
    printf("Comparacoes: %lld\n", comparacoes);
    printf("Tempo de execucao: %.6f\n", (double)(fim - inicio) / CLOCKS_PER_SEC);
    free(arr);
    return 0;
}
