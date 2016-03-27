/** Leftpad
 * March 25, 2016
 *
 * Large portions of the internet failed a few days ago when a program 
 * called leftpad, which pads a string to a given length by adding spaces 
 * or other characters at the left of the string, was suddenly removed from 
 * its repository. The whole episode is sad, and brings nothing but shame 
 * on everyone involved (though everyone involved seems to think they acted 
 * properly throughout), and all of the web sites that broke were created 
 * by fools (you don’t rely on unknown third parties to maintain code critical 
 * to your application at some unknown place on the internet). You can read 
 * more about what happened at these links: good overview of what happened
 * , Azer’s statement, NPM’s statement, and satire. The code that caused 
 * the problem is shown below:
 *
 * Your task is to write a proper version of leftpad; make sure yours operates 
 * in linear time instead of the quadratic time caused by the string concatenation 
 * in Azer’s code. When you are finished, you are welcome to read or run 
 * a suggested solution, or to post your own solution or discuss the exercise 
 * in the comments below.
 **/

module.exports = leftpad;

/**
 * Commenter notes that there are issues with UTF-16
 * string lenghts so this implementation is not totally
 * acceptable.
 * Using Array.join for (I think) better time preformance.
 */
function leftpad(str, len, ch)
{
    var prfx = [];
    if (!ch && ch !== 0) ch = ' ';
    if (ch.length > 1) ch = ch[0];
    targetlen = len - str.length;

    for(i = 0; i < targetlen; i++)
    {
        prfx.push(ch)
    }
    return prfx.join("") + str;
}
