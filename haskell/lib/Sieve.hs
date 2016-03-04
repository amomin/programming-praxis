module Sieve where

sieve n = helper  [] [2,3..n] where
    helper ps [] = reverse ps
    helper ps (xh:xs) = helper (xh:ps) (filter (\x -> (mod x xh /= 0)) xs)

--An infinite Sieve
primes = helper [2,3..] where
    helper (x:xs) = x : (helper $ filter (\y -> mod y x /= 0) xs)

--First n primes using the infinite primes list
primesFirstN n = take n primes

--Primes up to a bound n
primesUpTo n = takeWhile (< n) primes
