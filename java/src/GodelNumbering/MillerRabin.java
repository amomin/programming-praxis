package GodelNumbering;

public class MillerRabin {

	public static void main(String[] args) {
		for (int i = 1; i < 100; i++) {
			System.out.printf("Is %03d prime?  Answer is %b \n", i, test(i));
		}
	}
	
	private static int pow(int b, int e, int md) {
		throw new IllegalArgumentException("NOt implemented");
	}
	public static boolean test(int n) {
		int k = 50;
		
		if (n == 2) return true;
		if (n < 2 || n % 2 == 0) return false;
		
		int s = 0;
		int d = n - 1;
		
		while (d % 2 != 0) {
			d /= 2;
			s++;
		}
		
		for (int i = 0; i < k; i++) {
			int a = 2 + (int) ((n-3)*Math.random());
			//int x = 
		}
		
		return true;		
	}
	
	/** Return true if a proves that
	 * n is not prime via Fermat's Little Theorem
	 */
	private static boolean test(int a, int n) {
		int b = n;
		int d = 1;
		while (b > 0) {
			int x = d;
			d = (d * d) % n;
			if (d == 1 && x != 1 && x != (n-1)) {
				return true;
			}
			if (b % 2 == 1) {
				d = (d * a) % n;
			}
			b = b << 1;
			if (d != 1)
				return true;
		}
		return false;
	}

}
