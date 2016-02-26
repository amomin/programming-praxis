package fibonacciSearch;

// 0,1,2,3,4,5,6,7 ,8 ,9 ,10,11
// 0,1,1,2,3,5,8,13,21,34,55,89
public class FibonacciSearch {

	public static void main(String[] args) {
		for (int i = 1; i < 15; i++) {
			//System.out.println(i + ", " + indexFloor(i));
			int fib = fibonacci(i);
			System.out.println(i + ", " + fib);
			System.out.println("Index floor fib - 1= " + indexFloor(fib - 1));
			System.out.println("Index floor fib = " + indexFloor(fib));
			System.out.println("Index Ceil fib = " + indexCeil(fib));
			System.out.println("Index Ceil fib + 1 = " + indexCeil(fib + 1));
		}
	}
	
	// Return -1 if not found
	public static int fibSearch(int[] arr, int val) {
		return search(arr, val, 0, arr.length);
	}
	
	private static int search(int[] arr, int val, int min, int max) {
		if (min > max) return -1;
		
		int n = max - min;
		int k = indexCeil(n);
		if (k == 0) return -1;
		
		int pos = fibonacci(k - 1);
		if (arr[min + pos] == val) return min + pos;
        else if (arr[min + pos] < val)
        	return search(arr, val, min + pos + 1, max);
        else //arr[min + pos] > val
        	return search(arr, val, min, min + pos - 1);
	}
	
	// kth fibonnaci number
	public static int fibonacci(int k) {
		double gamma = 1.618033988749895;
		double delta = -1/gamma;
		double num = 
			Math.exp(Math.log(gamma) * k);
		if (k % 1 == 1) 
			num -= Math.exp(Math.log(-delta) * k);
		else
			num += Math.exp(Math.log(-delta) * k);
		return (int) Math.floor(
			num /Math.sqrt(5)
		);
	}
	
	/** Returns the index k of the largest fibonacci 
	 * F_k where F_k <= x
	 * 
	 * @param x
	 * @return index of greatest fibonacci number less than  or
	 * equal to x
	 */
	public static int indexCeil(int x) {
		if (x < 1) return 0;
		double gamma = 1.618033988749895;
		int guess = (int) Math.floor(
			Math.log(x * Math.sqrt(5)) 
			/ Math.log(gamma));
		int fin = fibonacci(guess);
		while (fin < x) {
			guess++;
			fin = fibonacci(guess);
		}
		return guess;
	}
	/** Returns the index k of the largest fibonacci 
	 * F_k where F_k <= x
	 * 
	 * @param x
	 * @return index of greatest fibonacci number less than  or
	 * equal to x
	 */
	public static int indexFloor(int x) {
		double gamma = 1.618033988749895;
		int guess = (int) Math.floor(
			Math.log(x * Math.sqrt(5)) 
			/ Math.log(gamma));
		int fin = fibonacci(guess);
		while (fin <= x) {
			guess++;
			fin = fibonacci(guess);
		}
		return guess - 1;
	}
}
