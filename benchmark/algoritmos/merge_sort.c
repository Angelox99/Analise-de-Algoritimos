#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long comparacoes = 0;

// Função auxiliar para mesclar dois subarrays
void merge(int *arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    int *L = malloc(sizeof(int) * n1);
    int *R = malloc(sizeof(int) * n2);

    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        comparacoes++;
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }

    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    free(L);
    free(R);
}

// Versão iterativa (bottom-up) do Merge Sort
void merge_sort(int *arr, int n) {
    for (int curr_size = 1; curr_size < n; curr_size *= 2) {
        for (int left_start = 0; left_start < n - 1; left_start += 2 * curr_size) {
            int mid = left_start + curr_size - 1;
            int right_end = (left_start + 2 * curr_size - 1 < n - 1) ? (left_start + 2 * curr_size - 1) : (n - 1);

            if (mid < right_end)
                merge(arr, left_start, mid, right_end);
        }
    }
}

// Leitura do arquivo
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
    merge_sort(arr, n);
    clock_t fim = clock();
    printf("Comparacoes: %lld\n", comparacoes);
    printf("Tempo de execucao: %.6f\n", (double)(fim - inicio) / CLOCKS_PER_SEC);
    free(arr);
    return 0;
}