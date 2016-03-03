module ArithmeticSequence where

import Data.List

-- Easy solution, but the sort is potentially O(nlogn) (the nub might be too)
-- Taking the max and using a bucket/radix sort it need not
-- be, but if the point is to do it fast there are better
-- ways
solution1 :: [Int] -> Bool
solution1 xs = (== 1) 
    $ length 
    $ nub 
    $ zipWith (\x y -> x-y) ys (tail ys)
        where ys = (sort xs)

-- Ok, try a little harder
-- Use the fact that a sorted list is arithmetic if and only if
-- the second difference is constant and equal to zero.  Use
-- a linear sort (not implemented but we know it exists)
-- to obtain a sorted list, take the difference twice, filter out
-- all zeros, and see if there is anything left.
-- Since all operations are linear the total time is O(n)
solution2 :: [Int] -> Bool
solution2 = null . (filter (/= 0)) . diffList . diffList . linSort
    where
        -- Compute differences of a list
        diffList :: [Int] -> [Int]
        diffList xs = zipWith (\x y -> x-y) xs (tail xs)
        -- Assume linSort is a linear sort, we will simply use sort instead but we
        -- could implement a linear sort method
        linSort :: [Int] -> [Int]
        linSort = sort
