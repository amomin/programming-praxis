package diminishingGapSort;

import java.util.Arrays;
import java.util.Comparator;

/** <h1> <a href="">
 *  Diminishing Gap Sort
 *  </a> </h1>
 * 
 * <p>August 19, 2016 </p>
 * 
 * <p> Given a number set of 5, 12, 14, 15, 80, 121, 134, 144, 256 the
 * descending-by-highest-difference sort would yield: 256, 80, 121, 134,
 * 144, 12, 14, 15, 5
 * So in this case, the top 3 biggest gaps would be
 * between 80, 121, and 256. </p>
 *
 * <p> Your task is to write a program that sorts a set of points in order
 * by the diminishing gaps between them. </p>
 *
 **/
public class DiminishingGapSort {

    public static int[] sort(int[] array) {
        int n = array.length;
        Integer[] indices = new Integer[n];
        int[] result = new int[n];
        for (int i = 0; i < n; i++) indices[i] = i;
        Arrays.sort(indices,
                    Comparator.comparingInt(
                        x->((int)x==0)?array[(int)x]:array[(int)x]-array[(int)x-1]));
        for (int i = 0; i < n; i++) result[i] = array[indices[i]];
        return result; 
    }

    public static void main (String[] args) {
        int[] array = new int[args.length];
        int i = 0;
        for (String s : args) {
            array[i++] = Integer.parseInt(s);
        }
        int[] result = DiminishingGapSort.sort(array);
        for (int j: result) {
            System.out.println(j);
        }
    }
}
