#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long comparacoes = 0;

// Função para trocar dois elementos
void trocar(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Particionamento (pivô na última posição)
int particionar(int *arr, int baixo, int alto) {
    int pivo = arr[alto];
    int i = baixo - 1;

    for (int j = baixo; j < alto; j++) {
        comparacoes++;
        if (arr[j] <= pivo) {
            i++;
            trocar(&arr[i], &arr[j]);
        }
    }
    trocar(&arr[i + 1], &arr[alto]);
    return i + 1;
}

// Quick Sort iterativo com pilha do tamanho correto
void quick_sort(int *arr, int baixo, int alto) {
    int tamanho = alto - baixo + 1;
    int *pilha = malloc(sizeof(int) * 2 * tamanho); // Pilha com o dobro do tamanho

    int topo = -1;
    pilha[++topo] = baixo;
    pilha[++topo] = alto;

    while (topo >= 1) {
        alto = pilha[topo--];
        baixo = pilha[topo--];

        int pi = particionar(arr, baixo, alto);

        if (pi - 1 > baixo) {
            pilha[++topo] = baixo;
            pilha[++topo] = pi - 1;
        }
        if (pi + 1 < alto) {
            pilha[++topo] = pi + 1;
            pilha[++topo] = alto;
        }
    }
    free(pilha);
}

// Leitura de arquivo
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
    quick_sort(arr, 0, n - 1);
    clock_t fim = clock();
    printf("Comparacoes: %lld\n", comparacoes);
    printf("Tempo de execucao: %.6f\n", (double)(fim - inicio) / CLOCKS_PER_SEC);

    free(arr);
    return 0;
}