-- Goldbach's Other Conjecture
-- June 07, 2016
-- 
-- https://programmingpraxis.com/2016/06/07/goldbachs-other-conjecture/
--
-- Although it is not as well known, Goldbach made another conjecture 
-- as follows: Every odd number greater than two is the sum of 
-- a prime number and twice a square; for instance, 
--
-- 27 = 19 + 2 * (2 ** 2)
--
-- Your task is to write a program that finds the smallest number 
-- that disproves Goldbach's other conjecture.
--

module GoldbachsOtherConjecture where

import Sieve

pair :: Integer -> (Integer,Integer)
pair x
    | 0 == (mod x 2)    = (0,0)
    | otherwise         = head [(y1,y2) |
        y1 <- (takeWhile (<= x) primes),
        y2 <- takeWhile (<= x-y1) [2*z*z | z <- [0,1..]],
        y1+y2 == x]

passesGoldbachTest :: Integer -> Bool
passesGoldbachTest x = not $ null [y1 + y2 |
    y1 <- (takeWhile (<= x) primes),
    y2 <- takeWhile (<= x-y1) [2*z*z | z <- [0,1..]],
    y1+y2 == x]

failsGoldbachTest :: Integer -> Bool
failsGoldbachTest x = null [y1 + y2 | 
    y1 <- (takeWhile (<= x) primes),
    y2 <- takeWhile (<= x-y1) [2*z*z | z <- [0,1..]],
    y1+y2 == x]

counterExample :: Integer
counterExample = head $ filter failsGoldbachTest [3,5..]
--counterExample = head $ dropWhile passesGoldbachTest [3,5..]
