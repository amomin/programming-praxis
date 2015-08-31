package invoice;

public class InvoiceLine {

	private int quantity;
	private float price;
	private String name;
	
	public void setQuantity(int value) { quantity = value; }
	public void setPrice(float value) {price = value; }
	public void setName(String value) {name = value; }
	
	public float total() { return quantity*price; }

	public String toString() {
		return String.format("%-20s   %5d    %.2f         %.2f", name, quantity, price, total());
	}
}
