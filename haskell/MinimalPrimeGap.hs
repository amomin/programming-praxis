module MinimalPrimeGap where

import Sieve

--primes is from Sieve.primes, the infinite list of primes
--computed by successively filtering out multiples of primes

gaps = zipWith (-) (tail . tail $ primes) (tail primes)

--diffs = zip primes (1:gaps)
diffs = zip (tail primes) gaps

-- If you want the first p where the gap meets or exceeds n:
--minimalPrimeGap n = fst $ head (dropWhile (\x -> snd x < n) diffs)
-- If you want a gap of "exactly" n
minimalPrimeGap n = fst $ head (dropWhile (\x -> snd x /= n) diffs)
