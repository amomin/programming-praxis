package utilities;

public class Stopwatch {

	long start;
	long end;
	long duration;
	
	public Stopwatch() {
		restart();
	}
	
	public long stop() {
		end = System.currentTimeMillis();
		duration = end - start;
		return duration;
	}
	
	public long logStop() {
		stop();
		System.out.printf("\nStopwatch stopped after %d ms\n", duration);
		return duration;
	}
	
	public void restart() {
		start = System.currentTimeMillis();
		end = Long.MAX_VALUE;
		duration = Long.MAX_VALUE;		
	}
	
	public long elapsedTime() {
		return duration;
	}
}
