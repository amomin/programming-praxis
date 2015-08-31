This is a simple, slow (but straightforward) algorithm to 
achieve the task.

The idea is to keep a pointer to the input and output files.  We keep
track of the current (output) column starting at 0, and at pass j we
pass through the lines of the input file, take the jth element, and append
it to the current line of the output file.  At the end of each pass we
reset the reader to the top of the file, and start a new line in the 
output file.

The suggested solution is much better - read through the input file,
write as a triplet to a temporary file with each line containing the
row number, column number, and value of that entry.  Then sort the 
temporary file first by column number and then by row number (or vv? in
any case should be via an in-place sort...) and then print the result
to the output file appropriately.

(If you know - or count - the number of rows in advance, you may
store the single number (j-1)*rows + i instead of the pair (i,j) 
and sort by that.)

Yet another way would be to use one file for each row of the output
file, and then append the values encountered to the correct file
as necessary.  In this case one has to take care to allocate the files
appropriately (so they don't potentially overwrite each other as they 
are being built).