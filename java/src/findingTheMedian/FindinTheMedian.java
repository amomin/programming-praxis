package findingTheMedian;

import utilities.quickSort.QuickSort;
import java.util.Arrays;

/** I think I'm off by an index in the bucket solution,
 * but I think the quickfind solutions works ok.
 * 
 * @author amomin
 *
 */
public class FindinTheMedian {
	
	/** Using "quick-find" - see utilities.QuickSort
	 * 
	 * @param ns - array of int
	 * @return - the median of ns
	 */
	public static int solution1(int[] ns) {
		int n = ns.length;
		if (n % 2 == 1) {
			return quickfind(ns, (n/2) + 1);
		}
		return (quickfind(ns, 1 + (n-1)/2) + quickfind(ns, 1 + (n/2)))/2;
	}

	/** Taking advantage of the "8-bit" hint - using
	 * a Bucket Sort type of solution.
	 */
	public static int solution2(int[] ns) {
		int[] counters = new int[256];
		boolean even = ns.length % 2 == 0;
		for (int i = 0; i < counters.length; i++) {
			counters[i] = 0;
		}
		for (int i = 0; i < ns.length; i++) {
			counters[ns[i]]++;
		}
		int curr = 0;
		int last = 0;
		int j = 0;
		int cummulative = counters[0];
		while(cummulative < (ns.length+1)/2) {
			j++;
			if (counters[j] != 0) {
				last = curr;
				cummulative += counters[last];
				curr = j;
			}
		}
		if (even) return (curr + last)/2;
		else return last;
	}
	
	/** Returns the kth largest element of ns
	 * - calls utilities.QuickSort.find
	 * 
	 * @param ns - array of int
	 * @param k - int
	 * @return - the kth largest element of ns
	 */
	protected static int quickfind(int[] ns, int k) {
		QuickSort q = new QuickSort(ns);
		return q.find(k);
	}
}
