package kthLargestItem;

/** Models an integer list - the point of the problem
 * is that the list may be too large to fit in memory.
 * 
 * @author amomin
 *
 */
public class IntegerList implements IIntegerList {

	int[] list;
	int k;
	
	public IntegerList(int[] i) {
		this.list = i;
		k = 0;
	}

	public boolean rewind() {
		k = 0;
		return true;
	}
	public boolean hasNext() {
		return (k < list.length);
	}
	public Integer getNext() {
		if (hasNext()) {
			this.k++;
			return list[this.k - 1];
		} 
		return null;
	}
}
