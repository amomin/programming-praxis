package matrixTranspose;

import java.io.IOException;

public class MatrixTransposer {

	MatrixFileReader mfr;
	MatrixFileWriter mfw;
	
	public MatrixTransposer(MatrixFileReader mfr, MatrixFileWriter mfw) {
		this.mfr = mfr;
		this.mfw = mfw;
	}
	
	public void transpose() throws NumberFormatException, IOException {
		mfr.seekStartOfFile();
		mfr.readNextLine();
		int cols = mfr.lineLength();
		int rows = 1;
		while (mfr.readNextLine()) {
			rows++;
		}
		
		mfr.seekStartOfFile();
		for (int j = 0; j < cols; j ++) {
			for (int i = 0; i < rows; i++) {
                mfr.readNextLine();
                int val = mfr.currentLine(j);
                mfw.append(val);
			}
            mfw.newLine();
            mfr.seekStartOfFile();
		}
		mfw.close();
	}
}