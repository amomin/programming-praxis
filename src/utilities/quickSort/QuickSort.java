package utilities.quickSort;

public class QuickSort {

	private int[] ns;
	
	public QuickSort(int[] arr) {
		this.ns = arr;
	}
	
	public int[] sort() {
		qs(0,this.ns.length-1);
		return ns;
	}

	/** Returns the kth largest element.
	 * Perhaps somewhat confusing because array indices
	 * begin at zero, but here the 0th element of a sorted
	 * matrix corresponds to k=1.
	 * 
	 * @param k
	 * @return
	 */
	public int find(int k) {
		if (k > ns.length) throw new IllegalArgumentException("Argument out of array bounds");
		if (k < 1) throw new IllegalArgumentException("Argument out of array bounds");
		return qf(k-1,0,this.ns.length-1);
	}
	
	private void qs(int lo, int hi) {
		if (lo >= hi) return;
		int l = lo;
		int r = hi;
		while(l < r) {
			while (l < r && ns[l+1] <= ns[l]) {
				swap(l, l+1);
				l++;
			}
			while (l < r && ns[r] > ns[l]) {
				r--;
			}
			if (l != r) {
				swap(l+1,r);
			}
		}
		if (l > lo) qs(lo,l-1);
		if (l < hi) qs(l+1,hi);
	}
	
	private int qf(int k, int lo, int hi) {
		if (lo >= hi) return ns[lo];
		int l = lo;
		int r = hi;
		while(l < r) {
			while (l < r && ns[l+1] <= ns[l]) {
				swap(l, l+1); l++;
			}
			while (l < r && ns[r] > ns[l]) {
				r--;
			}
			if (l != r) {
				swap(l+1,r);
			}
		}
		if (l == k) return ns[k];
		else if (l < k) return qf(k,l+1,hi);
		// else (l > k)
		else return qf(k,lo,l-1);
	}
	
	private void swap(int l, int r) {
		int tmp = ns[l];
		ns[l] = ns[r];
		ns[r] = tmp;
	}
}