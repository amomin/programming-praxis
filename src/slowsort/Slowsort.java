package slowsort;

/** This is great:
 * 
 * The slowsort algorithm is a perfect illustration of the multiply and 
 * surrender paradigm, which is perhaps the single most important paradigm 
 * in the development of reluctant algorithms. The basic multiply and 
 * surrender strategy consists in replacing the problem at hand by two 
 * or more subproblems, each slightly simpler than the original, 
 * and continue multiplying subproblems and subsubproblems recursively in this fashion as 
 * long as possible. At some point the subproblems will all 
 * become so simple that their solution can no longer be postponed, 
 * and we will have to surrender. Experience shows that, 
 * in most cases, by the time this point is 
 * reached the total work will be substantially higher than what could 
 * have been wasted by a more direct approach.
 *
 * To get a firmer grasp of the multiply and surrender method
 * , let us follow the step-by-step development 
 * of the slowsort algorithm. We can decompose the problem of 
 * sorting n numbers Al, A2, …, An in ascending 
 * order into (1) finding the maximum of those 
 * numbers, and (2) sorting the remaining ones. 
 * Subproblem (1) can be further decomposed into (1.1) find the maximum of 
 * the first [n/2] elements, (1.2) find the maximum of the remaining [n/2] 
 * elements, and (1.3) find the largest of those two maxima. Finally, 
 * subproblems (1.1) and (1.2) can be solved by sorting the specified elements and 
 * taking the last element in the result. We have thus 
 * multiplied the original problem into three slightly simpler ones (sort 
 * the first half, sort the second half, sort 
 * all elements but one), plus some overhead processing. We 
 * continue doing this recursively until the lists have at most one 
 * element each, at which point we are forced to surrender.
 * 
 * @author amomin
 *
 */
public class Slowsort 
{

	public static void main(String[] args) {
		int[] arr = {2, 1, 3};
		//int[] arr = {2};
		//int[] arr = {};
		int[] result = slowsort(arr);
		for (int i = 0; i < result.length; i++) {
			System.out.print(result[i] + ", ");
		}
	}

	public static int[] slowsort(int[] arr) {
		int n = arr.length;
		if (n < 2) {
			return arr;
		}
		// Find max element by searching the front and back,
		// and get the array that results by removing that
		// maximum value
		int[] front = slowsort(front(arr));
		int[] back = slowsort(back(arr));
		int maxFront = front[front.length - 1];
		int maxBack = back[back.length - 1];
		int max = 0;
		int[] basecase = new int[n-1];
		if (maxFront > maxBack) {
			basecase = merge(removeFirstOccurrance(front(arr), maxFront)
					, back(arr));
			max = tail(front);
		} else {
			basecase = merge(front(arr), 
					removeFirstOccurrance(back(arr), maxBack));
			max = tail(back);
		}
		// Recursive step
		int[] headresult = slowsort(basecase);
		int[] last = new int[] {max};
		return merge(headresult, last);
	}
	
	public static int[] front(int[] arr) {
		int n = arr.length;
		if (n < 2) {
			return new int[] {};
		}
		int[] front = new int[n/2];
		System.arraycopy(arr, 0, front, 0, n/2);
		return front;
	}
	public static int[] back(int[] arr) {
		int n = arr.length;
		if (n < 1) {
			return new int[] {};
		}
		int[] back = new int[n -(n/2)];
		System.arraycopy(arr, n/2, back, 0, n - n/2);
		return back;
	}
	public static int[] merge(int[] front, int[] back) {
		int[] result = new int[front.length + back.length];
		System.arraycopy(front, 0, result, 0, front.length);
		System.arraycopy(back, 0, result, front.length, back.length);
		return result;
	}

	public static int[] removeFirstOccurrance(int[] arr, int val) {
		if (arr.length < 1) {
			return arr;
		}
		int[] res = new int[arr.length-1];
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == val) {
				System.arraycopy(arr,0,res,0,i);
				System.arraycopy(arr,i+1,res,i,arr.length-i-1);
				return res;
			}
		}
		// Else not found
		return arr;
	}
	public static int[] head(int[] arr) throws
		java.lang.IllegalArgumentException {
		int n = arr.length;
		if (n < 1) {
			throw new java.lang.IllegalArgumentException("parameter cannot be empty");
		}
		int[] result = new int[n-1];
		System.arraycopy(arr, 0, result, 0, n-1);
		return result;
	}
	
	public static int tail (int[] arr) throws
		java.lang.IllegalArgumentException {
		int n = arr.length;
		if (n < 1) {
			throw new java.lang.IllegalArgumentException("parameter cannot be empty");
		}
		return arr[n-1];
	}
}