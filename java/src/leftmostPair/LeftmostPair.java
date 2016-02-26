package leftmostPair;

public class LeftmostPair {

	public static DigitPair getPair(int base, int n) {
		return getPair(base, n, 1);
	}
	
	/** Solves the pair problem
	 * 
	 * <p>
	 * The rational behind the "digits" (pos) part can be explained like this.  Say for example we are computing 
	 * getPair(10, 54321);
	 * The recursive calls split the number using larger bases
	 * 1 - 7 6 5 4 3 2 1 (6 segments to discard)
	 * 2 - 7 65 43 21 (3 segments to discad)
	 * 3- 765 4321  (1 segment to discard)
	 * 4- 07654321 < base (0 segments to discard)
	 * The pos counter counts the number of "segments to the right" discarded
	 * by the "current" base.  As we move up, each discarded segment splits into
	 * two, doubling the "pos" count, and we add 1 if the result is larger than the 
	 * current segment size because we are skipping an additional one as in level
	 * 2 of the above calculation.
	 * 
	 * </p>
	 * 
	 * @param base
	 * @param n
	 * @param pos
	 * @return
	 */
	public static DigitPair getPair(int base, int n, int pos) {
		if (n < base)  return new DigitPair(n, 0);
		DigitPair base2Pair = getPair(base*base, n, pos);
		pos = base2Pair.getPlace();
		int lp = base2Pair.getLeftMostDigit();
		if (lp < base)
			return new DigitPair(lp, 2*pos);
		else
			return new DigitPair(lp/base, 2*pos + 1);
	}
		
	public static class DigitPair {
		private int leftMostDigit;
		private int place;
		public DigitPair(int l, int p) {
			leftMostDigit = l;
			place = p;
		}
		public int getLeftMostDigit() { return leftMostDigit; }
		public int getPlace() { return place; }
		public String toString() {
			return String.valueOf(leftMostDigit) + ", " + String.valueOf(place);
		}
	}
	
}
