package MinimumImpossibleSum;

import java.util.Arrays;

public class MinimumImpossibleSum {

	public static void main(String[] args) {
		int[] nums = {1,2,3,4,13};
		//int x = solution1(nums);
		int x = solution2(nums);
		System.out.println(x);
	}

	public static int solution2(int[] nums) {
		Arrays.sort(nums);
		int L = nums.length;
		return solution2(nums, L);
	}
	
	/** Much better.  Runs on -O(n)- edit: O(n log(n)) because
	 * of the sort - although the sort may be reduced to O(n) if
	 * using a counting/radix sort.
	 * 
	 * Programmed recursively but could be done as a loop.
	 * 
	 * @param nums
	 * @param L - list of integers (assumed to be positive)
	 * @return the least integer not representable as a 
	 * sum of the integers in L.
	 */
	private static int solution2(int[] nums, int L) {
		if (L == 1) {
			if (nums[0] == 1) return 2;
			else return 1;
		}
		int M = nums[L-1];
		int x = solution2(Arrays.copyOf(nums, L-1));
		if (x < M) {
			return x;
		} else {
			return x + M;
		}
	}
	/** First answer
	 * 
	 * @param nums
	 * @return
	 */
	public static int solution1(int[] nums) {
		Arrays.sort(nums);
		int total = 0;
		for (int i = 0; i < nums.length; i++) {
			total += nums[i];
		}
		
		boolean[] bools = new boolean[total + 1];
		bools[0] = true;
		
		for (int i = 0;i < total + 1; i++) {
			bools[i] = false;
		}
	
		int minVal = 0;
		for (int i = 0; i < nums.length; i++) {
			for (int j = Math.min(total, 2*nums[i]); j > 0 ; j--) {
				System.out.println(nums[i] + ", " + j);
				if (bools[j]) {
					bools[nums[i] + j] = true;
				} else if (j < nums[i]) {
					minVal = j;
				}
			}
			bools[nums[i]] = true;
			if (minVal > 0) {
				return minVal;
			}
		}
		
		// Should never get here with
		// current implementation
		int x = 1;
		while(bools[x]) {
			//System.out.println("here");
			x++;
		}
		return x;
	}
}