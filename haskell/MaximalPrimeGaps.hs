module MinimalPrimeGap where

import Text.Printf
import Sieve

gaps = zipWith (-) (tail $ primes) ( primes)
diffs = zip primes gaps

maximalPrimeGaps :: [(Integer,Integer)]
maximalPrimeGaps = helper 0 where
    helper n = (x,m):(helper (m+1)) where
        (x,m) = head $ dropWhile(\z -> snd z < n) diffs

-- Bascially as above but carry the tail of the diff list along so you don't
-- have to drop through the head of the list each time.
-- Would like to see how this plays out on memory and time.
maximalPrimeGaps' :: [(Integer,Integer)]
maximalPrimeGaps' = helper 0 diffs where
    helper n xs = (y,m):(helper (m+1) (tail ys)) where
        ys = dropWhile(\z -> snd z < n) diffs
        (y,m) = head ys

--prompt :: (Read a) => String -> IO a
--prompt s = putStr s >> getLine >>= return . read
prompt x = do
    putStrLn x
    number <- getLine
    return number

main :: IO ()
main = do
    n <- prompt "Enter the maximal prime gap to search up to: "
    let num = (read n::Integer)
    let answer = takeWhile (\x -> snd x <= num) maximalPrimeGaps
    let output = map (\x -> printf "Gap of %10d first occurs at %10d" (snd x) (fst x)) answer
    mapM_ putStrLn output
