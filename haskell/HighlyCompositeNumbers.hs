-- Highly Composite Numbers
-- July 12, 2016
--
-- https://programmingpraxis.com/2016/07/12/highly-composite-numbers/
--
-- A highly composite number, also called an anti-prime, is a 
-- number n for which d(m) < d(n) for all m < n, where d(x) is 
-- the divisor function that gives a count of the number of divisors 
-- of x; in other words, it has more divisors than any smaller 
-- number. Thus, a highly composite number, which has many divisors,
-- is the opposite of a prime number, which has only two divisors. The 
-- sequence of highly composite numbers, which begins
-- 1, 2, 4, 6, 12, 24, 36, ... (A002182),
-- has been studied by Ramanujan and Erdos, among others, and is a
-- continuing object of study by number theorists. A famous highly
-- composite number, known to Plato, is 5040.
-- 
-- Your task is to write a program that returns all highly composite 
-- numbers less than a given limit.
-- 
-- Compile with
-- $ ghc -main-is HighlyCompositeNumbers \
-- $    -o bin/HighlyCompositeNumbers \
-- $    haskell/HighlyCompositeNumbers.hs
--
-- Or switch the module name to "Main" to compile without the -main-is flag

module HighlyCompositeNumbers where

import Text.Printf

-- Return the number of times an integer divides another integer
intDivLog :: Integer -> Integer -> Integer
intDivLog k n = dehlp k n 0 where
    dehlp k n e
        | (mod n k) == 0    = dehlp k (div n k) (e+1)
        | otherwise         = e

-- Return a factorization of the input in the form of a list of pairs,
-- consisting of factors and the number of times the factor appears in the
-- in the prime factorization of the input
-- e.g. On input 7 = 7, it returns [(7,1)]
-- e.g. On input 6 = 2*3, it returns [(2,1),(3,1)]
-- e.g. On input 4 = 2*2, it returns [(2,2)]
-- e.g. On input 12 = 2*2*3, it returns [(2,2),(3,1)]
-- e.g. On input 90 = 2*3*3*5, it returns [(2,1),(3,2),(5,1)]
factor :: Integer -> [(Integer,Integer)]
factor n = helper [] 2 n where
    helper sofar k n 
        | n == 1            = sofar
        | k*k > n           = sofar ++ [(n,1)]
        | (mod n k) == 0    = (let e = (intDivLog k n) in helper (sofar ++ [(k,e)]) (k+1) (div n (k^e)))
        | otherwise         = helper sofar (k+1) n

-- Ooops, did not need to define this but leaving for later use if needed
phi :: Integer -> Integer
phi x = product $ map (\(x,y) -> x^y - x^(y-1)) (factor x)

-- Return divisors of input
divisors :: Integer -> Integer
divisors x = product $ map (\(x,y) -> (y+1)) (factor x)

-- Return list of Highly Composite Numbers up to input
hcnUpTo :: Integer -> [Integer]
hcnUpTo n = helper 1 (-1) where
    helper k maxSoFar
        | k > n     = []
        | divisors(k) > maxSoFar = [k] ++ helper (k+1) (divisors k)
        | otherwise              = helper (k+1) maxSoFar 

-- Terminal prompt
prompt :: Read b => String -> IO b
prompt x = do
    putStrLn x
    l <- getLine
    return (read l)

-- Prompt for an integer
intPrompt :: String -> IO Integer
intPrompt = prompt

main :: IO ()
main = do
    print "Highly Composite Numbers client"
    n <- intPrompt "Enter a limit"
    print $ hcnUpTo n
