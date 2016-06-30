-- Curious Numbers
-- June 28, 2016
--
-- https://programmingpraxis.com/2016/06/28/curious-numbers/
--
-- Some numbers have the curious property that when they are 
-- squared, the number appears in the least-significant digits 
-- of the product.
-- For instance, 625^2 = 390625, and 7106376^2 = 50543227109376.
-- 
-- What is the sum of all numbers less than 1020 that have this curious property?
-- 
-- Compile with
-- $ ghc -main-is CuriousNumbers \
-- $    -o bin/CuriousNumbers. \
-- $    haskell/CuriousNumbers.hs
--
-- Or switch the module name to "Main" to compile without the -main-is flag

module CuriousNumbers where

import Data.List
import Data.Time

-- Return True if a number is curious and false otherwise
isCurious :: Integer -> Bool
isCurious n = n == (mod (n * n) p) where
    powersOfTen = map (\x -> 10^x) [1..]
    p = head $ dropWhile (< n) powersOfTen

-- Return the list of curious numbers of N digits or fewer
--
-- We use the following to build up the set recursively
-- If c is curious a n-digit number, let c = x*(10^(n-1)) + y where
-- * 10^(n-k-1) < y < 10^(n-k), for some k > 0, and
-- * x is in [1..9]
-- Then c = y (mod 10^(n-k)), and
-- c = c*c = y*y = y (mod 10^(n - k))
-- so y is also curious
--
-- So we can build up a list c(n) of curious n-digit number candidates from
-- the list l(n-1) of (n-1) digit numbers fairly easily as:
-- c(n) = [x*(10^(n-1)) + y | x <- [0..9], y <- l(n-1)]
--
-- and then obtain the curious n-digit numbers l(n) by filtering
-- l(n) = filter isCurious c(n)
-- (This may generate repeats so we will need to take
-- unique elements of the list.)
--
-- Since curious numbers are rare, the list of curious numbers at the
-- previous step is small, so this is not terribly expensive - polynomial
-- in the number of digits requested.
curiousUpToNDigits :: Integer -> [Integer]
curiousUpToNDigits n
    | n == 1        = [1,5,6]
    | n > 1         = let l = (curiousUpToNDigits (n-1)) in
        sort . nub $ filter isCurious [x*(10^(n-1)) + y | x <- [0..9], y <- l]
    | otherwise     = []

-- Compute the sum of curious numbers of at most n digits
--
-- sumOfCurious 20 computes the answer to the question asked
sumOfCuriousUpTo :: Integer -> Integer
sumOfCuriousUpTo n = sum $ curiousUpToNDigits n

-- Terminal prompt
prompt x = do
    putStrLn x
    number <- getLine
    return number

main :: IO ()
main = do
    n <- prompt "Enter the number of digits to sum"
    st <- getCurrentTime
    let num = (read n::Integer)
    let l = curiousUpToNDigits num
    let s = sumOfCuriousUpTo num
    print "The sum is:"
    print s
    print "The list of all curious numbers of n digits or fewer is:"
    print l
    end <- getCurrentTime
    print "Time:"
    print (diffUTCTime end st)
