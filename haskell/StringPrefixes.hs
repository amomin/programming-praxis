module StringPrefixes where

prefixPair :: (Eq a) => [a] -> [a] -> [a]
prefixPair [] _ = []
prefixPair _ [] = []
prefixPair (x:xs) (y:ys)
    | x == y    = x:(prefixPair xs ys)
    | otherwise = []

prefix :: (Eq a) => [[a]] -> [a]
prefix xs = foldl prefixPair (head xs) (tail xs)
