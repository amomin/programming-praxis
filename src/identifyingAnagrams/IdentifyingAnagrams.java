package identifyingAnagrams;

import java.util.Arrays;
import java.util.HashMap;

public class IdentifyingAnagrams {

	/** Sort characters then compare strings.
	 * 
	 * May assume a and b contain only the characters
	 * a..z
	 * @param a
	 * @param b
	 * @return true if a is an anagram of b
	 */
	public static boolean solution1(String a, String b) {
		char[] aa = a.toCharArray();
		char[] bb = b.toCharArray();
		if (aa.length != bb.length) return false;
		
		Arrays.sort(aa);
		Arrays.sort(bb);
		for (int i = 0; i < aa.length; i++) {
			if (aa[i] != bb[i]) return false;
		}
		return true;
	}
	
	/** Count characters, then compare counts. We'll
	 * use a hash map instead of an array.
	 * 
	 *  May assume a and b contain only the characters
	 * a..z
	 * @param a
	 * @param b
	 * @return true if a is an anagram of b
	 */
	public static boolean solution2(String a, String b) {
		HashMap<String, Integer> hm = new HashMap<String, Integer>();
		
		if (a.length() != b.length())  return false;
		
		for (int i = 0; i < a.length(); i++) {
			String key = String.valueOf(a.charAt(i));
			if (!hm.containsKey(key)) {
				hm.put(key, 1);
			} else {
				// increment counter
				hm.put(key, hm.get(key) + 1);
			}
		}
		for (int i = 0; i < b.length(); i++) {
			String key = String.valueOf(b.charAt(i));
			if (!hm.containsKey(key)) {
				return false;
			} else {
				// decrement counter
				hm.put(key, hm.get(key) - 1);
			}
		}
		
		// all counters should be zero
		for (Integer x : hm.values()) {
			if (x != 0) return false;
		}
		
		return true;
	}
}