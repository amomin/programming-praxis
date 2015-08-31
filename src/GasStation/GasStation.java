package GasStation;

public class GasStation {

	public static void main(String[] args) {
		System.out.println("A few test cases");
		int[] gas = {1,2,3,4};
		int[] milesToNext = {4,3,2,1};
		int k = solve(gas, milesToNext);
		System.out.println("Start at station " + k);
		k = solve2(gas, milesToNext);
		System.out.println("Start at station " + k);
		gas = new int[] 		{15, 8, 2 , 6, 18, 9 , 21, 30};
		milesToNext = new int[] {8 , 6, 30, 9, 15, 21, 2 , 18 };
		k = solve(gas, milesToNext);
		System.out.println("Start at station " + k);
		k = solve2(gas, milesToNext);
		System.out.println("Start at station " + k);
		gas = new int[] 		{1, 1, 1, 4};
		milesToNext = new int[] {2, 2, 2, 1};
		k = solve(gas, milesToNext);
		System.out.println("Start at station " + k);
		k = solve2(gas, milesToNext);
		System.out.println("Start at station " + k);
		gas = new int[] 		{1, 1, 1, 1, 1, 4};
		milesToNext = new int[] {2, 2, 2, 2, 2, 1};
		k = solve(gas, milesToNext);
		System.out.println("Start at station " + k);
		k = solve2(gas, milesToNext);
		System.out.println("Start at station " + k);
		gas = new int[] 		{2};
		milesToNext = new int[] {1};
		k = solve(gas, milesToNext);
		System.out.println("Start at station " + k);
		k = solve2(gas, milesToNext);
		System.out.println("Start at station " + k);
		gas = new int[] 		{2, 2};
		milesToNext = new int[] {1, 1};
		k = solve(gas, milesToNext);
		System.out.println("Start at station " + k);
		k = solve2(gas, milesToNext);
		System.out.println("Start at station " + k);
	}

	// Use cummulative sums for a one-pass solution O(1) time and space.
	public static int solve2(int[] gas, int[] milesToNext) {
		int n = gas.length;
		int currcumm = 0;
		int mincumm = 0;
		int idx = -1;
		for (int i = 0; i < n; i++) {
			currcumm += (gas[i] - milesToNext[i]);
			if (currcumm < mincumm) {
				mincumm = currcumm;
				idx = i;
			}
		}
		if (currcumm < 0) return -1;
		return (idx + 1) % n;
	}
	
	// Simplest possible solution, (naively) O(n^2) time and
	// and O(n) space.
	public static int solve(int[] gas, int[] milesToNext) {
		int n = gas.length;
		for (int i = 0; i < n; i++) {
			int inTank = 0;
			int count = 0;
			while(inTank >= 0 && count < n) {
				int idx = (i + count) % n;
				inTank += gas[idx] - milesToNext[idx];
				count++;
			}
			if (count == n && inTank >= 0) return i;
		}
		return -1;
	}
}