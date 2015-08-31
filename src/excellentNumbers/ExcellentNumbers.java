package excellentNumbers;

import java.math.BigInteger;
import java.util.ArrayList;

public class ExcellentNumbers {

	public static final int EXP = 5;
	public static void main(String[] args) {
		BigInteger answer = solution2();
		System.out.println(answer);
	}
	
	public static BigInteger solution2() {
		ArrayList<BigInteger> sols = new ArrayList<BigInteger>();
		int i = (int) Math.pow(10, EXP-1);
		int j = (int) (Math.sqrt(i) 
			* Math.sqrt(Math.pow(10,EXP) + ((double) i)));
		while (j < Math.pow(10, EXP)) {
			j = (int) (Math.sqrt(i) 
				* Math.sqrt(Math.pow(10,EXP) + ((double) i)));
			for (int jj = 0; jj < 2; jj++) {
				int jjj = j + jj;
				BigInteger a = BigInteger.valueOf(i);
				BigInteger b = BigInteger.valueOf(jjj);
				BigInteger a1 = a.multiply(BigInteger.valueOf((int) Math.pow(10,EXP)));
				BigInteger rhs = b.add(a1);
				BigInteger lhs = (b.multiply(b)).subtract(a.multiply(a));
				if ( lhs.equals(rhs)) {
					sols.add(lhs);
				}
			}
			i++;
		}
		BigInteger sum = BigInteger.ZERO;
		for(BigInteger x : sols) {
			//System.out.println(x);
			sum = sum.add(x);
		}
		return sum;
	}
	
	public static void solution1() {
		ArrayList<BigInteger> sols = new ArrayList<BigInteger>();
		for (int i = (int) Math.pow(10, EXP - 1); 
			i < (int) Math.pow(10, EXP); i++) 
		{
			int j = i + 1;
			BigInteger rhs = BigInteger.valueOf(1);
			BigInteger lhs = BigInteger.valueOf(2);
			while(j < Math.pow(10,EXP) && lhs.compareTo(rhs) <= +1) {
				BigInteger a = BigInteger.valueOf(i);
				BigInteger b = BigInteger.valueOf(j);
				BigInteger a1 = a.multiply(BigInteger.valueOf((int) Math.pow(10,EXP)));
				rhs = b.add(a1);
				lhs = (b.multiply(b)).subtract(a.multiply(a));
				if (rhs.equals(lhs)) {
					sols.add(rhs);
				}
				j ++;
			}
		}
		for(BigInteger b : sols) {
			System.out.println(b);
		}
	}
}
