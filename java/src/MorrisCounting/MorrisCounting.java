package MorrisCounting;

/** Morris counting problem (Feb 20, 2015)...
 * 
 * Implement a Morris counter.  This class runs a demo 
 * which runs a program that increments a Morris counter
 * some number of times, gets the resulting counter value,
 * repeated for some number of trials and prints the average
 * value of the results of these trials.
 * 
 * @author amomin
 *
 */
public class MorrisCounting {
	
	public static int countTo(int N) {
		MorrisCounter count = new MorrisCounter();
		int i = 0;
		while (i < N) {
			count.increment();
			i++;
		}		
		return count.value();
	}
	
	public static void main(String[] args) {
		int trials = 500000;
		int total = 0;
		int countToInt = 18;
		for (int i = 0; i < trials; i++) {
			total += countTo(countToInt);			
		}
		System.out.printf("Over %d trials, average count is %.2f", trials, ((float) total/(float) trials));
	}
}
