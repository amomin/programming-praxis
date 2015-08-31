package kthLargestItem;

import java.util.Collections;
import java.util.PriorityQueue;

public class MinStack implements IMinStack {

	PriorityQueue<Integer> pq;
	int size;
	Integer currentMax;

	public MinStack(int size) {
		this.size = size;
		pq = new PriorityQueue<Integer>(size, Collections.reverseOrder());
		currentMax = null;
	}
	
	public int size() {
		return pq.size();
	}
	
	public void insert(int x) {
		if (this.size > pq.size()) {
			pq.add(x);
			currentMax = pq.peek();
		}
		else if (x < currentMax) {
			pq.remove();
			pq.add(x);
			currentMax = pq.peek();
		}
	}
	
	public Integer getValue() {
		if (pq.size() >= this.size) {
			return currentMax;
		} else {
			return null;
		}
	}
}
