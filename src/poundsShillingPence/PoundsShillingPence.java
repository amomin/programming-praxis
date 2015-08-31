package poundsShillingPence;

public class PoundsShillingPence {

	public static void main(String[] args) {
		// Example using sec, min, hrs, days, weeks mixed radix
		int[] radix = {60, 60, 24, 7};
		Radix r1 = new Radix(radix);
		Radix r2 = new Radix(radix);
		
		int[] v1 = {55, 14, 22, 3, 3};
		int[] v2 = {15, 17, 10, 5, 2};
		
		r1.setValue(v1);
		r2.setValue(v2);
		
		Radix sum = r1.add(r2);
		System.out.println(r1.toString());
		System.out.println(r2.toString());
		System.out.println(sum.toString());
	}
}
