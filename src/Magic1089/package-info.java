/** Magic 1089 from programmingpraxis (Oct 3)
 * @author user
 *
 * If n is 3 digits and "digit descending" (e.g. 952 is ok
 * but 538 is not) then the following process supposedly yeilds 1089
 * every time:
 * 
 * let diff be the difference between the number and it's reversal.
 * return diff plus the reversal of its digits.
 * 
 *  Suppose you start with 100x + 10y + z
 *  Then diff should be
 *  100(x-z-1) + 90 + (z-x+10) 
 *  So the result should be  
 *  100(x-z-1 + 10 + z -x) + 180 + (z-x+10 + x - z - 1)
 *  = 900 + 180 + 9 = 1089
 */
package Magic1089;