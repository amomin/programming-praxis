package matrixTranspose;

public class MatrixTranspose {

	public static final String PATH = Constants.PATH;
	
	public static void main(String[] args) {
		transpose("in.txt", "out.txt");
	}

	public static void transpose(String infile, String outfile) {
		try {
			MatrixFileReader mfr = new MatrixFileReader();
			mfr.setFile(PATH+infile);
			
			MatrixFileWriter mfw = new MatrixFileWriter();
			mfw.setFile(PATH+outfile);
		
			MatrixTransposer t = new MatrixTransposer(mfr, mfw);
			t.transpose();
		} catch (Exception e) {
			System.out.println("Problem reading file");
			System.out.println(e.getMessage());
		}
	}
}