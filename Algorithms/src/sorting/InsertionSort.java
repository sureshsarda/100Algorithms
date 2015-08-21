package sorting;

import java.util.Arrays;

public class InsertionSort {
	public static int[] insertionSort(int[] array) {
		int[] arrayCopy = Arrays.copyOf(array, array.length);
		for (int i = 1; i < arrayCopy.length; i++) {

			int current = arrayCopy[i];

			int j = i - 1;
			while (j >= 0 && arrayCopy[j] > current) {
				arrayCopy[j + 1] = arrayCopy[j];
				j--;
			}
			arrayCopy[j + 1] = current;
		}
		return arrayCopy;
	}
}
