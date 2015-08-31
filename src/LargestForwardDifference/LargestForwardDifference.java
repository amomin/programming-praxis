package LargestForwardDifference;

import java.util.Arrays;

public class LargestForwardDifference {

	public static void main(String[] args) {
		int[] arr = new int[]{4, 2, 1, 5, 3, 9};
		System.out.printf("LFD is: %d "
				+ "\n", lfd(arr));
	}
	
	public static int testPraxis(int[] arr) { return praxissolution(arr);	}	
	public static int testNaive(int[] arr) { return naiveLFD(arr);	}
	public static int testDC(int[] arr) { return divideandconquer(arr); }
	
	public static int lfd(int[] arr) {
		//return naiveLFD(arr);
		return divideandconquer(arr);
	}

	/** Bah, should have got this one
	 *
	 * @param arr
	 * @return the lfd
	 */
	private static int praxissolution(int[] arr) {
		if (arr.length < 2) return 0;
		int lfd = 0;
		int min = arr[0];
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] > min) {
				int curr = arr[i] - min;
				if (curr > lfd) lfd = curr;
			} else {
				min = arr[i];
			}
		}
		return lfd;
	}
	
	private static int divideandconquer(int[] arr) {
		if (arr.length < 2) return 0;
		int minl = arr[0];
		int maxR = arr[0];
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] < minl) minl = arr[i];
			if (arr[i] > maxR) maxR = arr[i];
		}
		int pos1 = Math.max(0, maxR - minl);
		int mid = arr.length/2;
		int pos2 = divideandconquer(Arrays.copyOfRange(arr, 0, mid));
		int pos3 = divideandconquer(Arrays.copyOfRange(arr, mid + 1, arr.length));
		return Math.max(pos1, Math.min(pos2, pos3));
	}
	
	private static int naiveLFD(int[] arr) {
		int lfd = 0;
		int l = 0;
		int r = 0;
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = i + 1; j < arr.length; j ++) {
				int curr = arr[j] - arr[i]; 
				if (curr > lfd) {
					lfd = curr; 
				}
			}
		}
		return lfd;
	}
}
