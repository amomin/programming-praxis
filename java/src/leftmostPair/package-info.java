/**
 * @author Al Momin
 *
 * Re: Programming Praxis "Integer Logarithm" post on August 26th
 * http://programmingpraxis.com/2014/08/26/integer-logarithm/ 
 * 
 * The integer logarithm function in the Standard Prelude looks like this:
 * 
 * (define (ilog b n)
 *   (let loop1 ((lo 0) (b^lo 1) (hi 1) (b^hi b))
 *     (if (< b^hi n) (loop1 hi b^hi (* hi 2) (* b^hi b^hi))
 *       (let loop2 ((lo lo) (b^lo b^lo) (hi hi) (b^hi b^hi))
 *        (if (<= (- hi lo) 1) (if (= b^hi n) hi lo)
 *           (let* ((mid (quotient (+ lo hi) 2))
 *                  (b^mid (* b^lo (expt b (- mid lo)))))
 *             (cond ((< n b^mid) (loop2 lo b^lo mid b^mid))
 *                   ((< b^mid n) (loop2 mid b^mid hi b^hi))
 *                   (else mid))))))))
 * 
 * It performs binary search in loop1 until n is bracketed between b^lo and b^hi, doubling at each step, then refines the binayr search in loop2, halving the bracket at each step.
 * 
 * Inspired by that function, Joe Marshall posed this puzzle at his Abstract Heresies web site:
 * 
 * You can get the most significant digit (the leftmost) of a number pretty quickly this way:
 * 
 * (define (leftmost-digit base n)
 *   (if (< n base)
 *       n
 *       (let ((leftmost-pair (leftmost-digit (* base base) n)))
 *         (if (< leftmost-pair base)
 *             leftmost-pair
 *             (quotient leftmost-pair base)))))
 * 
 * The puzzle is to adapt this code to return the position of the leftmost digit.
 */
package leftmostPair;