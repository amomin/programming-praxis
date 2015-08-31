package matrixTranspose;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MatrixFileReader {

	private String filename;
	private BufferedReader in;
	private int[] currentLine;
	private int lineLength;
	
	public void setFile(String fname) throws IOException {
		lineLength = 0;
		filename = fname;
	    setFile(new BufferedReader(new FileReader(fname)));
	}
	
	protected void setFile(BufferedReader br) {
		in = br;
	}
	
	public void seekStartOfFile() throws IOException {
		in.close();
		in = new BufferedReader(new FileReader(filename));
	}
	
	public boolean readNextLine() throws 
		IOException, NumberFormatException
	{
		String s = in.readLine();
		String[] currentStringLine = {};
		if (s != null) {
			currentStringLine = s.split("\\s+");
		} else {
			return false;
		}
		lineLength = currentStringLine.length;
		currentLine = new int[lineLength];
		int i = 0;
		for (String t : currentStringLine) {
			currentLine[i] = Integer.parseInt(t);
			i++;
		}
		return true;
	}

	public int lineLength() {
		return lineLength;
	}
	
	public int currentLine(int i) throws IllegalArgumentException {
		if (i < 0  || i > currentLine.length) 
			throw new IllegalArgumentException();
		return currentLine[i];
	}
}
