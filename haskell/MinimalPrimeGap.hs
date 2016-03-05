module MinimalPrimeGap where

import System.Environment
import Text.Printf
import Sieve

--primes is from Sieve.primes, the infinite list of primes
--computed by successively filtering out multiples of primes


-- If you want the first p where the gap meets or exceeds n:
--minimalPrimeGap n = fst $ head (dropWhile (\x -> snd x < n) diffs)

-- If you want a gap of "exactly" n
minimalPrimeGap n = fst $ head (dropWhile (\x -> snd x /= n) diffs) where
    gaps = zipWith (-) (tail . tail $ primes) (tail primes)
    diffs = zip (tail primes) gaps

--prompt :: (Read a) => String -> IO a
--prompt s = putStr s >> getLine >>= return . read
prompt x = do
    putStrLn x
    number <- getLine
    return number

main :: IO ()
main = do
    n <- prompt "Enter a number: "
    let num = 2*(quot (read n :: Integer) 2)
    let gaps = map (\x -> (x, minimalPrimeGap x)) [2,4..num]
    let output = map (\x -> printf "Gap of %10d first occurs at %10d" (fst x) (snd x)) gaps
    mapM_ putStrLn output
