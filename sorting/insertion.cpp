/*
  INSERTION SORT:
  author: Suresh Sarda

  Insertion sort looks somewhat like Bubble Sort but instead of putting larger numbers in the end, Insertion Sort inserts numbers at their
  position and thus creating a array from smaller number to larger number.

  Intution:
  We start at the second element (array  of one number is sorted in iteself) and insert it at its position. So now we have an array of 2 numbers, sorted. Next we move to third element and insert it at its right position, and so on.

*/

#include<stdio.h>

void printArray(int * arrayToPrint, int size);
void insertionSort(int *array, int size);

int main() {
  int array[] = {3, 5, 6, 1, 4, 6, 7, 9, 10, 8};

  printArray(array, 10);
  insertionSort(array, 10);
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
