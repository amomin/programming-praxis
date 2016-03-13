module TwoBoysCanoe where

import Data.List

-- Not optimal, need to sort, and uses extra space
-- But at least still O(n) if you use a radix or bucket sort
-- Using a two-sided linked list and two pointers you could 
-- eliminate much of this waste
sol1 :: [Int] -> [(Int,Maybe Int)]
sol1 xs = helper (length xs) (Data.List.sort xs) (reverse $ Data.List.sort xs) where
    helper :: Int -> [Int] -> [Int] -> [(Int, Maybe Int)]
    helper 0 _ _ = []
    helper 1 _ (x:xs) = [(x, Nothing)]
    -- n > 1
    helper howManyLeft (mn:inc) (mx:dec)
        | mx > 150          = []
        | (mx + mn) > 150   = (mx,Nothing):(helper (howManyLeft-1) (mn:inc) dec)
        -- Can fit two in a boat
        | otherwise         = (mx,Just mn):(helper (howManyLeft-2) inc dec)

howMany1 :: [Int] -> Int
howMany1 = length . sol1
