package degreesRadians;

public class Angle {

	private long totalseconds;

	/** Make constructor private
	 */
	private Angle() { }
	
	public static Angle fromDegrees(int degrees, int minutes, int seconds) {
		if (degrees < 0 || minutes < 0 || seconds < 0) {
			throw new java.lang.IllegalArgumentException();
		}
		if (minutes > 59 || seconds > 59) {
			throw new java.lang.IllegalArgumentException();
		}
		if (degrees > 359) 
			degrees = (degrees - 360 * (int) (degrees/360));
		
		Angle a = new Angle();
		a.totalseconds = ((long) 60*60*degrees) + ((long) 60 * minutes) + ((long) seconds);
		return a;
	}
	
	public static Angle fromRadians(double radians) {
		double normalized = radians; // Set between 0 and 2PI
		// For simplicity assuming radians > 0
		if (radians < 0) {
			throw new java.lang.IllegalArgumentException();
		}
		if (radians > 2*Math.PI) {
			normalized = radians - 2 * Math.PI * Math.floor(normalized / (2 * Math.PI));
		}
		// First, x is the angle again re-normalized between 0 and 1
		double x = normalized / (2 * Math.PI);
		int degrees = (int) (Math.floor((x * 360.0)));
		// Now x is the fractional part of the angle in 
		// degrees (as a real number)
		x = 360.0 * x - (double) degrees;
		int minutes = (int) Math.floor( x * 60 );
		// Now x is the fractional part of 
		// the angle in minutes (as a real number)
		x = 60 * x - (double) minutes;
		int seconds = (int) Math.round(60.0 * x);
		return Angle.fromDegrees(degrees, minutes, seconds);
	}
	
	public int degrees() {
		return (int) totalseconds/(60*60);
	}
	
	public int minutes() {
		return (int) ((totalseconds/60) % 60);
	}
	
	public int seconds() {
		return (int) (totalseconds % 60);
	}
	
	public double radians() {
		double radians = 2 * Math.PI * (((double) totalseconds) / (360.0 * 3600.0));
		return radians;
	}
}