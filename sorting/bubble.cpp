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
  int i = 0;

  // The ligheter numbers bubble up or come in front.
  // So what needs to be done is compare and swap the number to previous number till
  // the number comes to its correct position.
  for (i = 1; i < size; i++) {
    int j = i;
    while(array[j - 1] > array[j]) {
      swap(&array[j], &array[j - 1]);
      j--;
    }
  }
}
