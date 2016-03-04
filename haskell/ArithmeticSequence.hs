module ArithmeticSequence where

import Data.List
import Data.IntMap

----------------
-- Easy solution
----------------
-- But the sort is O(nlogn) (the nub too)
-- If the point is to do it fast there are better ways
solution1 :: [Int] -> Bool
solution1 xs = (== 1) 
    $ length 
    $ nub 
    $ zipWith (\x y -> x-y) ys (tail ys)
        where ys = (Data.List.sort xs)

---------------------------
--Similar to above solution
---------------------------
--I thought this could be O(n) but actually it won't be because the
--keys are (nearly) distinct, the word lengh w = log n so the
--O(wn) is really O(nlogn) like a comparison sort.  May as
--well use a comparison sort anyway.
solution2 :: [Int] -> Bool
solution2 = Data.List.null . (Prelude.filter (/= 0)) . diffList . diffList . linSort
    where
        -- Compute differences of a list
        diffList :: [Int] -> [Int]
        diffList xs = zipWith (\x y -> x-y) xs (tail xs)
        -- Even if linSort is a "linear" sort, this method will still
        -- be O(nlogn)
        linSort :: [Int] -> [Int]
        linSort = Data.List.sort

--------------------------------
--Linear solution, use a hashmap
--------------------------------
--The inserts/lookups are (should be) O(1), and each construction is O(n), so
--the total time is (should be) O(n) (space is O(n))
solution3 :: [Int] -> Bool
solution3 xs = let
    minList :: [Int] -> Int
    minList ys = Data.List.foldl min (head ys) (tail ys)    
    shiftIntList :: Int -> [Int] -> [Int]
    shiftIntList y xs = Prelude.map (\x -> (x - y)) xs
    min1 = minList xs
    min2 = minList . (Data.List.filter (/= min1)) $ xs
    diff = min2 - min1
    hashmap = Data.IntMap.fromList ( zip (shiftIntList min1 xs) (repeat True) )
    in
    and $ Prelude.map (\x -> Data.IntMap.member x hashmap) [0,diff..(diff*(length xs - 1))] 
