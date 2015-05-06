package sorting;

import java.util.Arrays;

public class MergeSort {
	public static int[] mergeSort(int[] array) {
		if (array.length > 1) {
			int[] left = Arrays.copyOfRange(array, 0, array.length / 2);
			int[] right = Arrays.copyOfRange(array, array.length / 2, array.length);
			left = mergeSort(left);
			right = mergeSort(right);
			array = combine(left, right);
		}
		return array;
	}
	
	private static int[] combine(int[] arr1, int[] arr2) {
		//Combine both the sorted arrays
		int index = 0;
		int arr1Index = 0;
		int arr2Index = 0;
		int[] combined = new int[arr1.length + arr2.length];
		
		while (arr1Index < arr1.length && arr2Index < arr2.length) {
			if (arr1[arr1Index] < arr2[arr2Index]) {
				combined[index++] = arr1[arr1Index++];
			}
			else if (arr2[arr2Index] < arr1[arr1Index]) {
				combined[index++] = arr2[arr2Index++];
			}
			else {
				/*Both elements are same*/
				combined[index++] = arr1[arr1Index++];
				combined[index++] = arr2[arr2Index++];
			}
		}
		
		if (arr2Index < arr2.length) {
			/*There is still content in array 2*/
			copy(arr2, combined, arr2Index, index);
		}
		else if (arr1Index < arr1.length) {
			/*There is still content in array 1*/
			copy(arr1, combined, arr1Index, index);
		}
		else {
			/*Both have depleted. Don't do anything.*/
			
		}
		return combined;
	}
	
	private static void copy(int[] source, int[] dest, int sourceOffset, int destOffset) {
		while (sourceOffset < source.length) {
			dest[destOffset++] = source[sourceOffset++];
		}
	}
}
