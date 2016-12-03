'use strict';

var leftpad = require('./Leftpad')

var tests = [];

tests[0] = function()
{
    var ch = 'c';
    var str = "Hello World";
    var len = 15;
    var res = leftpad(str, len, ch);
    var expected = 'ccccHello World';
    var tstres =  expected == res;
    if (!tstres)
        console.log(res, expected);
    return tstres;
};

// Ignore characters beyond the first
tests[1] = function()
{
    var ch = 'chaha';
    var str = "Hello World";
    var len = 15;
    var res = leftpad(str, len, ch);
    var expected = 'ccccHello World';
    var tstres =  expected == res;
    if (!tstres)
        console.log(res, expected);
    return tstres;
}

// When string is longer than desired length
tests[2] = function()
{
    var ch = 'c';
    var str = "Hello World";
    var len = 10;
    var res = leftpad(str, len, ch);
    var expected = 'Hello World';
    var tstres =  expected == res;
    if (!tstres)
        console.log(res, expected);
    return tstres;
}

// When character is null, undefined, or false - replace with ' '
tests[3] = function()
{
    var ch = null;
    var str = "Hello World";
    var len = 15;
    var res = leftpad(str, len, ch);
    var expected = '    Hello World';
    var tstres =  expected == res;
    if (!tstres)
        console.log(res, expected);
    return tstres;
}
// When character is null, undefined, or false - replace with ' '
tests[4] = function()
{
    var ch = undefined;
    var str = "Hello World";
    var len = 15;
    var res = leftpad(str, len, ch);
    var expected = '    Hello World';
    var tstres =  expected == res;
    if (!tstres)
        console.log(res, expected);
    return tstres;
}

// When character is null, undefined, or false - replace with ' '
tests[5] = function()
{
    var ch = false;
    var str = "Hello World";
    var len = 15;
    var res = leftpad(str, len, ch);
    var expected = '    Hello World';
    var tstres =  expected == res;
    if (!tstres)
        console.log(res, expected);
    return tstres;
}

// Character is null and len  < str.length
tests[6] = function()
{
    var ch = null;
    var str = "Hello World";
    var len = 1;
    var res = leftpad(str, len, ch);
    var expected = 'Hello World';
    var tstres =  expected == res;
    if (!tstres)
        console.log(res, expected);
    return tstres;
}

// Timing
tests[7] = function()
{
    var ch = 'a';
    var str = 'Hello World';
    var elapsed = [];
    var maxpow = 10
    for (var i = 0; i < maxpow; i++)
    {
        var len = Math.pow(2,5 + i)
        var start = process.hrtime();
        for (var j = 0; j < 50000; j++)
        {
            leftpad(str, len, ch);
        }
        var end = process.hrtime(start)[0];
        elapsed[i] =  end;
    }
    var passed = true
    for(i = 1; i < maxpow; i++)
    {
        if ((elapsed[i-1] > 0) && (elapsed[i] > 10*elapsed[i-1]))
        {
            console.log(elapsed[i], elapsed[i-1]);
            passed = false;
        }
    }
    return passed;
}

for(var i = 0; i < tests.length; i++)
{
    if (tests[i]())
        console.log("Test " + i + " passed.");
    else
        console.log("Test " + i + " failed.");
}
