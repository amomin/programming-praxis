/**
 * @author user
 *
 * Implement Blums Mental Hash, as follows
 * 
 * Inputs: 
 * - a map f from letters a-z to digits 0-9
 * - a permutation g of the digits 0-9
 * 
 * Method:
 * - map the string to hash using to digits using f
 * - For the first digit of the output, use g(first + last % 10)
 * - For the second digit of the output, use g(previously obtained digit + second (of original) % 10)
 * - For the third digit of the output, use g(previously obtained (2nd) digit + third (of original) % 10)
 * continue...
 */
package BlumsMentalHash;