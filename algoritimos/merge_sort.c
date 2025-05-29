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

// Função recursiva de ordenação
void merge_sort(int *arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        merge_sort(arr, l, m);
        merge_sort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

// Leitura do arquivo (pode ficar em utils/ler_arquivo.c depois)
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

    clock_t inicio = clock();
    comparacoes = 0;

    merge_sort(arr, 0, n - 1);

    clock_t fim = clock();
    double tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;

    printf("Comparacoes: %lld\n", comparacoes);
    printf("Tempo (s): %f\n", tempo);

    free(arr);
    return 0;
}
