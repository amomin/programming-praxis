package degreesRadians;

public class DegreesRadians {

	public static void main(String[] args) {
		
	}
	
	public static double degreesToRadians(int d, int m, int s) {
		Angle a = Angle.fromDegrees(d, m, s);
		return a.radians();
	}
	
	public static int radiansToDegrees(double r) {
		Angle a = Angle.fromRadians(r);
		return a.degrees();
	}

	public static int radiansToMinutes(double r) {
		Angle a = Angle.fromRadians(r);
		return a.minutes();
	}
	
	public static int radiansToSeconds(double r) {
		Angle a = Angle.fromRadians(r);
		return a.seconds();
	}
}
