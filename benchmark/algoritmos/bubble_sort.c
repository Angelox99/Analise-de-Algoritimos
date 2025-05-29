#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long comparacoes = 0;

void bubble_sort(int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            comparacoes++;
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

int *ler_arquivo(char *nome_arquivo, int *tamanho) {
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
    bubble_sort(arr, n);
    clock_t fim = clock();
    printf("Comparacoes: %lld\n", comparacoes);
    printf("Tempo de execucao: %.6f\n", (double)(fim - inicio) / CLOCKS_PER_SEC);
    free(arr);
    return 0;
}