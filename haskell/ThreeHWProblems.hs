module ThreeHomeworkProblems where

sum1 :: [Int] -> Int
sum1 = foldl (+) 0

-- Built-in
rev0 :: [a] -> [a]
rev0 = reverse

-- Cheap code but potentially O(n^2)
rev1 :: [a] -> [a]
rev1 [] = []
rev1 (x:xs) = (rev1 xs) ++ [x]

-- Should be O(n)
rev2 :: [a] -> [a]
rev2 xs = helper [] xs where
    helper hs [] = hs
    helper hs (t:ts) = helper (t:hs) ts

isort :: Ord a => [a] -> [a]
isort xs = helper [] xs where
    helper hs [] = hs
    helper hs (t:ts) = helper (ins t hs) ts where
        ins x [] = [x]
        ins x (xh:xs)
            | x < xh            = (x : xh : xs)
            | otherwise         = (xh : (ins x xs))
