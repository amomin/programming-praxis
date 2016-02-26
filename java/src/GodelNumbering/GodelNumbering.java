package GodelNumbering;

import java.math.BigDecimal;


public class GodelNumbering {

	private int current;
	
	public static void main(String[] args) {
		String input = "thisishowwedoit";
		input = input.toUpperCase();
		BigDecimal encoded = encode(input);
		System.out.printf("Encoded is %s \n", encoded.toString());
		System.out.printf("Test decodeing: %s", decode(encoded));
	}
	
	public static BigDecimal encode(String s) {
		GodelNumbering g = new GodelNumbering();
		BigDecimal gn = new BigDecimal(1);
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			int idx = ((int) c) - 64;
			int p = g.nextPrime();
			BigDecimal exp = new BigDecimal(1);
			for (int j = 0; j < idx; j++) {
				exp = exp.multiply(new BigDecimal(p));
			}
			gn = gn.multiply(exp);
		}
		return gn;		
	}
	
	public static String decode(BigDecimal x) {
		GodelNumbering g= new GodelNumbering();
		String out = "";
		while (x.compareTo(new BigDecimal(1)) > 0) {
			int p = g.nextPrime();
			int idx = 0;			
			while (x.remainder(new BigDecimal(p)).compareTo(new BigDecimal(1)) == -1) {
				idx++;
				x = x.divide(new BigDecimal(p));
				if (idx > 26) throw new IllegalArgumentException();
			}
			out = out + String.valueOf((char)(64 + idx));
		}
		return out;
	}
	private GodelNumbering() {
		current = 1;
	}
	
	private int nextPrime() {
		int x = current + 1;
		while (!prime(x)) {
			x++;
		}
		current = x;
		return x;
	}
	
	/** Simple implementation since the difficulty
	 * is dealing with the large integers
	 */
	private boolean prime(int x) {
		for (int i = 2; i <= Math.sqrt(x); i++) {
			if (x % i == 0) return false;
		}
		return true;
	}
}
