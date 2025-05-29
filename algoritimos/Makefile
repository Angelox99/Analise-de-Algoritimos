CC=gcc
CFLAGS=-O2 -Wall

all: bubble_sort insertion_sort merge_sort quick_sort

bubble_sort: ./bubble_sort.c
	$(CC) $(CFLAGS) -o bubble_sort ./bubble_sort.c

insertion_sort: ./insertion_sort.c
	$(CC) $(CFLAGS) -o insertion_sort ./insertion_sort.c

merge_sort: ./merge_sort.c
	$(CC) $(CFLAGS) -o merge_sort ./merge_sort.c

quick_sort: ./quick_sort.c
	$(CC) $(CFLAGS) -o quick_sort ./quick_sort.c

clean:
	rm -f bubble_sort insertion_sort merge_sort quick_sort
