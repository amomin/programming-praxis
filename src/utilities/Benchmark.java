package utilities;

import java.util.ArrayList;

public class Benchmark {

	private ArrayList<DataPoint> data;
	
	public Benchmark() {
		data = new ArrayList<DataPoint>();
	}
	
	public void addCase(int time, int size) {
		data.add(new DataPoint(time, size));
	}
	
	public String report() {
		return "";
	}
	
	private static class DataPoint {
		private int time;
		private int size;
		private int memory;
		
		public DataPoint(int t, int s) {
			time = t;
			size = s;
		}
	}
}
