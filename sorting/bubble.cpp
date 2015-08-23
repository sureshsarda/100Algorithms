/*
  BUBBLE SORT
  author: Suresh Sarda

  Intution:
  The intution for this algorithm is that at every pass, adjacent elements are compared and the elements are swapped, if a swap is required
  FOr example, if we want to sort in ascending order and 2 number are in order of larger and smaller, then a swap is required and we will swap them
  But if the numbers are smaller first and larger later, then we will keep them the way they are.

  If we iterate over it n times, the array will be sorted.
*/

#include<stdio.h>

void printArray(int * arrayToPrint, int size);
void bubbleSort(int * arrayToSort, int size);

int main() {
  int array[] = {3, 5, 6, 1, 4, 6, 7, 9, 10, 8};

  printArray(array, 10);
  bubbleSort(array, 10);
  printArray(array, 10);
  return 0;
}

void printArray(int * array, int size) {
  while (size--) {
    printf("%d ", *array++);
  }
  printf("\n");
}

void swap(int *num1, int *num2) {
  int temp = *num1;
  *num1 = *num2;
  *num2 = temp;
}

void bubbleSort(int *array, int size) {
  int i = 0; //iterations
  int j = 0; //index in array

  for (i = 0; i < size; i++) {
    for (j = 0; j < size - i - 1; j++) {
      if (array[j] > array[j + 1]) {
	swap(&array[j], &array[j + 1]);
      }
    }
  }
}
void insertionSort(int *array, int size) {
  int i = 0;

  for (i = 1; i < size; i++) {
    int j = i;
    while(array[j - 1] > array[j]) {
      swap(&array[j], &array[j - 1]);
      j--;
    }
  }
}

