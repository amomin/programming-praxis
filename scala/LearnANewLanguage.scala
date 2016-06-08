/**
 * Learn a new language
 *
 * https://programmingpraxis.com/2016/05/31/learn-a-new-language-4/
 *
 * Implementing a "quick-like" sort in Scala.
 */

object QuickishSort {
  def sort(arr: Array[Int]): Array[Int] = {
    if (arr.length < 2) {
      return arr;
    }
    var x = arr(0);
    return sort(arr.filter(_ < x)) ++ arr.filter(_ == x) ++ sort(arr.filter(_ > x))
  }
  
  def main(args: Array[String]) {
    var sorted =sort(Array[Int](12,45,65,1,45,23,76,4,36,17,72,14,64));
    for (i <- sorted) {
      println(i);
    }
  }
}
