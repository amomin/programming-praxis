package poundsShillingPence;

/**
 * Enter values from left = 0 = simplest denomination (e.g. sec)
 * to right = largest denomination (e.g. hours/days/weeks/...)
 * @author amomin
 *
 */
public class Radix {

	private int[] radix;
	private int[] value;
	
	public Radix(int[] radix)
		throws java.lang.IllegalArgumentException{
		for(int i = 0; i < radix.length; i++) {
			if (radix[i] < 0) {
				throw new java.lang.IllegalArgumentException();
			}
		}
		this.radix = radix;
		this.value = null;
	}

	public boolean setValue(int[] val) 
		throws java.lang.IllegalArgumentException{
		if (val.length != radix.length + 1) {
			throw new java.lang.IllegalArgumentException();
		}
		for (int i = 0; i < radix.length; i++) {
			if (val[i] >= radix[i] || val[i] < 0) {
				throw new java.lang.IllegalArgumentException();
			}
		}
		this.value = new int[val.length];
		for (int i = 0; i < val.length; i++) {
			this.value[i] = val[i];
		}
		return true;
	}

	private int convertToInt() {
		int result = this.value[this.radix.length];
		for (int i = this.radix.length - 1; i >= 0; i--) {
			result = this.radix[i]*result + this.value[i];
		}
		return result;
	}

	private void valueFromInteger(int x) {
		this.value = new int[this.radix.length + 1];
		for (int i = 0; i < radix.length; i++) {
			this.value[i] = x % this.radix[i];
			x /= this.radix[i];
			System.out.println(x + " " + this.radix[i]);
		}
		this.value[this.radix.length] = x;
	}
	public Radix add(Radix r2)
		throws java.lang.IllegalArgumentException{
		if (this.value == null || r2.value == null) {
			throw new java.lang.IllegalArgumentException();
		}
		for (int i = 0; i < this.radix.length; i++) {
			if (this.radix[i] != r2.radix[i]) {
				throw new java.lang.IllegalArgumentException();
			}
		}
		int c1 = this.convertToInt();
		int c2 = r2.convertToInt();
		Radix r = new Radix(this.radix);
		r.valueFromInteger(c1 + c2);
		return r;
	}
	
	public String toString() {
		StringBuilder sb = new StringBuilder("");
		for (int i = 0; i < this.value.length - 1; i++) {
			sb.append(this.value[i] + ", ");
		}
		sb.append(this.value[this.value.length - 1]);
		return sb.toString();
	}
}
