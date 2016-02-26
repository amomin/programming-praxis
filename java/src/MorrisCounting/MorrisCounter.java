package MorrisCounting;

/** Represents a counter that uses a single byte (at the cost of
 * probabilistic counting).  Attributed to Robert Morris by
 * programmingpraxis.com
 * 
 * @author amomin
 *
 */
public class MorrisCounter {

	private byte count;
	
	public MorrisCounter() {
		count = (byte) 0;
	}
	
	public void increment() {
		double rand = Math.random();
		double range = Math.pow((double) 2, -(double) (int) count);
		if (rand < range) {
			count = (byte) (((int) count) + 1);
		}
	}
	
	public int value() {
		return (int) Math.pow(2, (double) (int) count) - 1;
	}
}
