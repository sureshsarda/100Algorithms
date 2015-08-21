package sorting;

import java.util.Random;

public class SortingSimulator {
	public static void main(String[] args) {

		int array[] = new int[10000000];
		floodArray(array);
		
		System.out.println("Original Sequence:");
		printArray(array);

		long start = System.currentTimeMillis();
		array = MergeSort.mergeSort(array);
		long end = System.currentTimeMillis();

		System.out.println("Sorted Sequence:");
		printArray(array);
		
		System.out.printf("%8d , %d\n", array.length, end - start);

	}

	private static void printArray(int[] array) {
		for (int i = 0; i < array.length; i++) {
			System.out.println(array[i]);
		}
	}

	private static void floodArray(int[] array) {
		Random r = new Random();

		for (int i = 0; i < array.length; i++) {
			Double rand = Math.abs(r.nextGaussian());
			array[i] = (int) (rand * 1000);
		}
	}
}
