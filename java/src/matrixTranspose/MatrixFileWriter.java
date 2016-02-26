package matrixTranspose;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.RandomAccessFile;

public class MatrixFileWriter {

	private BufferedWriter bw;
	
	public void setFile(String filename) throws IOException {
		FileWriter fw = new FileWriter(filename, false);
		bw = new BufferedWriter(fw);
	}

	public void append(int x) throws IOException {
		bw.write(" " + String.valueOf(x));
	}
	
	public void newLine() throws IOException {
		bw.newLine();
	}
	
	public void close() throws IOException {
		bw.close();
	}
}
