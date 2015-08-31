package orderedCartesianCoordinates;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.TreeMap;

public class OrderedCartesianCoordinates {

	public static void main(String[] args) {
		int n = 10;
		//Coordinate[] coords = solution1(n);
		//Coordinate[] coords = solution2(n);
		Coordinate[] coords = solution3(n);
		for (Coordinate c : coords) {
			System.out.println(c);
		}
	}
	
	/** No-brainer solution, in principle it
	 * is O(n^2 log(n)).  Using a radix/bucket sort
	 * can be made closer to (exactly?) O(n^2)
	 * - have to think about the uneven distribution
	 * of the indices though.
	 * 
	 * In any case it's still the fastest of the solutions
	 * presented here.
	 * 
	 * @param n
	 * @return
	 */
	public static Coordinate[] solution1(int n) {
		Coordinate[] coords = new Coordinate[n*n];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				coords[n*(i-1) + j - 1] = new Coordinate(i, j);
			}
		}
		Arrays.sort(coords); // Presumeably quicksort, but you
		// can use whatever sort algorithm you like here
		// e.g. bucket/radix sort.
		return coords;
	}
	
	/** 
	 * Use a tree-hash-map to store coordinates as they are 
	 * created, and then loop through the keys in 
	 * ascending order.
	 * 
	 * This solution is much slower - it's probably storing 
	 * the keys in a tree to keep the order, which is much 
	 * slower than ordinary hashing.
	 * 
	 * @return Coordinates ordered by product
	 */
	public static Coordinate[] solution2(int n) {
		TreeMap<Integer, ArrayList<Coordinate>> h = new 
			TreeMap<Integer, ArrayList<Coordinate>>();
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (!h.containsKey(i*j)) {
					ArrayList<Coordinate> a = new ArrayList<Coordinate>();
					a.add(new Coordinate(i,j));
					h.put(i*j,a);
				} else {
					ArrayList<Coordinate> a = h.get(i*j);
					a.add(new Coordinate(i,j));
				}
			}
		}
		Coordinate[] coords = new Coordinate[n*n];
		int i = 0;
		for (Integer x : h.navigableKeySet()) {
			ArrayList<Coordinate> a = h.get(x);
			for(Coordinate c : a) {
				coords[i] = c;
				i++;
			}
		}
		return coords;
	}
	
	/** 
	 * Use an array of lists of coordinates indexed 
	 * by the key (product of coordinates).
	 * 
	 * Most lists will be empty but it is manifestly 
	 * sorted.  This will take up a good amount of
	 * extra space but should be certifiably O(n^2).  Can 
	 * be easily parallelized.
	 *
	 * Still, in practice probably not better than the
	 * "no-brainer" solution.
	 * 
	 * EDIT - actually it seems that it is faster than
	 * solution1 up to a point (on my computer about
	 * n=800 to 900) after which solution1 is quite a bit
	 * faster.  Memory use?  But problem persists even
	 * after increasing memory.
	 * 
	 * @return Coordinates ordered by product
	 */
	@SuppressWarnings("unchecked")
	public static Coordinate[] solution3(int n) {
		Object[] list = new Object[n*n+1];
		for (int x = 1; x <= n*n; x++) {
			list[x] = new ArrayList<Coordinate>();
		}
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				int x = i*j;
				ArrayList<Coordinate> a = 
					(ArrayList<Coordinate>) list[x];
				a.add(new Coordinate(i,j));
			}
		}
		Coordinate[] coords = new Coordinate[n*n];
		int i = 0;
		for (int x = 1; x <= n*n; x++) {
			ArrayList<Coordinate> a = (ArrayList<Coordinate>) list[x];
			for(Coordinate c : a) {
				coords[i] = c;
				i++;
			}
		}
		return coords;
	}
}
