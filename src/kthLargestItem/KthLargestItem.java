package kthLargestItem;

public class KthLargestItem {

	public static void main(String[] args) {
		int[] arrl = {5,2,4,1,8,5,6};
		IIntegerList l = new IntegerList(arrl);
		System.out.println(KthLargestItem.find(l, 2));
	}

	public static Integer find(IIntegerList l, int k) {
		if (k < 1) {
			throw new IllegalArgumentException();
		}
		l.rewind();
		IMinStack ms = new MinStack(k);
		while (l.hasNext()) {
			int x = l.getNext();
			ms.insert(x);
		}
		return ms.getValue();
	}
}
