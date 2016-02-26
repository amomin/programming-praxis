package oneSwappableArray;

public class OneSwappableArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] arr;
		arr = new int[] {2 ,1};
		System.out.println(arr.toString() + OneSwappableArray.isOneSwapFromSorted(arr));
	}
	
	public static boolean isOneSwapFromSorted(int[] arr) {
		int n = arr.length - 1;
		int countInversions = 0;
		int posInversion1 = -1;
		int posInversion2 = n + 1;
		for (int i = 0; i < n; i++) {
			if (arr[i + 1] < arr[i]) {
				countInversions++;
				if (countInversions == 1) {
					posInversion1 = i;
				} else if (countInversions == 2) {
					posInversion2 = i + 1;
				} else {
					return false;
				}
			}
		}
		if (countInversions < 1) return false;
		if (countInversions == 1) posInversion2 = posInversion1 + 1;
		// Four cases, posInversion1 ?= 0, posInversion2 ?= n
		boolean inv1Ok, inv2Ok;
		inv2Ok = arr[posInversion1 + 1] >= arr[posInversion2];
		if (posInversion1 > 0)
			inv2Ok = arr[posInversion1 - 1] <= arr[posInversion2];
		inv1Ok = arr[posInversion2 - 1] <= arr[posInversion1];
		if (posInversion2 < n)
			inv2Ok = arr[posInversion2 + 1] >= arr[posInversion1];
		return inv1Ok && inv2Ok;
	}

}
