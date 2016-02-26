package LargestForwardDifference;

public class Benchmark {
	private int numTests = 5;
	private int[][] lists;
	private boolean isSetup = false;
	
	public static void main(String[] args) {
		Benchmark b = new Benchmark();
		//b.Naive();
		//b.DC();
		b.Praxis();
	}
	public void setup() {
		if (!isSetup) {
			int N = 3200000;
			lists = new int[numTests][];
			for (int ntest = 0; ntest < numTests; ntest++) {
				lists[ntest] = new int[N];
				for (int i = 0; i < N; i++) {
					lists[ntest][i] = (int) (100000 * Math.random());
				}
				N*=2;
			}
		}
	}
	
	public void Naive() {
		setup();
		for (int i = 0; i < lists.length; i++) {
			int[] list = lists[i];
			long t = System.currentTimeMillis();
			LargestForwardDifference.testNaive(list);
			t = System.currentTimeMillis() - t;
			System.out.printf("For length %d, time in ms %d \n", list.length, t);
		}
	}

	public void DC() {
		setup();
		for (int i = 0; i < lists.length; i++) {
			int[] list = lists[i];
			long t = System.currentTimeMillis();
			LargestForwardDifference.testDC(list);
			t = System.currentTimeMillis() - t;
			System.out.printf("For length %d, time in ms %d \n", list.length, t);
		}
	}
	
	public void Praxis() {
		setup();
		for (int i = 0; i < lists.length; i++) {
			int[] list = lists[i];
			long t = System.currentTimeMillis();
			LargestForwardDifference.testPraxis(list);
			t = System.currentTimeMillis() - t;
			System.out.printf("For length %d, time in ms %d \n", list.length, t);
		}
	}
}
