package matrixTranspose;

import static org.junit.Assert.*;

import java.io.BufferedReader;

import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.junit.Test;

//@RunWith(MockitoJUnitRunner.class)
public class MatrixFileReaderTest {

	@Mock
	BufferedReader br;
	
	@Test
	public void testReadNextLine() {
		MatrixFileWriter mfw = new MatrixFileWriter();
		//mfw.setFile(br);
		fail("Not yet implemented");
	}

	@Test
	public void testLineLength() {
		fail("Not yet implemented");
	}

	@Test
	public void testCurrentLine() {
		fail("Not yet implemented");
	}

}
