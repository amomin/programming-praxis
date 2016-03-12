module CountingPrimesUsingLegendre where

import Text.Printf
import Sieve

ppi :: Integer -> Integer
ppi x 
    -- Slow because using length instead of doing some kind of binary search
    | x < 100       = toInteger $ length (takeWhile (<= (fromIntegral x)) primes)
    | otherwise     = (phi x a) + a - 1
    where
        a = ppi . intSqrt $ x

intSqrt :: Integer -> Integer
intSqrt = floor . sqrt . fromIntegral

phi :: Integer -> Integer -> Integer
phi x a 
    | pa > x        = 1
    | a == 1        = quot (x+1) 2
    | otherwise     = (phi x (a-1)) - (phi (quot x pa) (a-1))
    where
        pa = nthPrime a

nthPrime :: Integer -> Integer
nthPrime n = primes !! ((fromIntegral n) - 1)

prompt x = do
    putStrLn x
    number <- getLine
    return number

main :: IO ()
main = do
    n <- prompt "Enter the number x you wish to compute pi(x) for: "
    let x = (read n::Integer)
    let answer = ppi x
    putStrLn (printf "Answer is %09d" answer)
