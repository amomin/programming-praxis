-- Wave Sorting
-- March 4, 2016
-- 
-- A list of integers is sorted in “wave” order if alternate items are greater 
-- than their immediate neighbors (thus the other alternate items are less 
-- than their immediate neighbors). Thus, the list [4 1 7 5 6 2 3] is in 
-- wave order because 4 > 1, then 1 < 7, then 7 > 5, then 5 < 6, then 6 > 
-- 2, and finally 2 < 3. Note that the two alternate streams [4 7 6 3] and 
-- [1 5 2] need not themselves be sorted. It doesn’t matter if the first 
-- item is the high wave or the low trough between waves, though starting 
-- with a wave is traditional.
-- 
-- Your task is to write a program that takes a list of unique integers and 
-- sorts it into wave order. When you are finished, you are welcome to read 
-- or run a suggested solution, or to post your own solution or discuss the 
-- exercise in the comments below.
--
-- NOTE: We go with the convention that a list is wave sorted allowing
-- equality between neighbors.  Under this stricter defintion not all 
-- lists are wave sortable, and for those that are it is more difficult to 
-- find a solution.

module WaveSorting where

import Data.List

-- Cheat solution - first sort, and then wavify by swapping pairs
wsort1 :: (Ord a) => [a] -> [a]
wsort1 xs = wavify srted
    where
        srted = Data.List.sort xs
        wavify [] = []
        wavify (x:[]) = [x]
        wavify (x:y:xs) = y:x:(wavify xs)

-- Test if wave sorted
isWaveSorted :: (Ord a) => [a] -> Bool
isWaveSorted [] = True
isWaveSorted [x] = True
isWaveSorted [x,y] = True
isWaveSorted (x:y:xs)
    | x > y         = isTroughWaveSorted (y:xs)
    | otherwise     = isCrestWaveSorted (y:xs)
    where
        isTroughWaveSorted :: (Ord a) => [a] -> Bool
        isCrestWaveSorted  :: (Ord a) => [a] -> Bool
        isTroughWaveSorted [] = True
        isTroughWaveSorted [x] = True
        isTroughWaveSorted [x,y] = x <= y
        isTroughWaveSorted (x:y:z:xs) = and [x <= y, z <= y, isTroughWaveSorted (z:xs)]
        isCrestWaveSorted [] = True
        isCrestWaveSorted [x] = True
        isCrestWaveSorted [x,y] = y <= x
        isCrestWaveSorted (x:y:z:xs) = and [y <= x, y <= z, isCrestWaveSorted (z:xs)]

-- Try to write a solution with a litte more dignity
-- This one is linear
wsort2 :: (Ord a) => [a] -> [a]
wsort2 [] = []
wsort2 [x] = [x]
wsort2 [x,y] = [max x y, min x y]
wsort2 (x1:x2:x3:xs) = l3:l1:wsort2(l2:xs)
    where
        [l1,l2,l3] = Data.List.sort([x1,x2,x3])

-- This one is linear and should be idempotent
-- though it is not quite the identity on wave sorted lists
-- because we haven't taken care of the case where the first two entries are equal
wsort3 :: (Ord a) => [a] -> [a]
wsort3 [] = []
wsort3 [x] = [x]
wsort3 [x,y] = [x, y]
wsort3 (x1:x2:x3:xs) 
    | x1 > x2       = wsort3Crested (x1:x2:x3:xs)
    | otherwise     = wsort3Troughed (x1:x2:x3:xs)
-- Linear solution, which is idempotent if the input starts with a crest
wsort3Crested :: (Ord a) => [a] -> [a]
wsort3Crested [] = []
wsort3Crested [x] = [x]
wsort3Crested [x,y] = [max x y, min x y]
wsort3Crested (x1:x2:x3:xs) 
    | and [(x2 < x1), (x2 < x3)]    = x1:x2:(wsort3Crested(x3:xs))
    | otherwise                     = l3:l1:wsort3Crested(l2:xs)
    where
        [l1,l2,l3] = Data.List.sort([x1,x2,x3])
-- Linear solution, which is idempotent if the input starts with a trough
wsort3Troughed :: (Ord a) => [a] -> [a]
wsort3Troughed [] = []
wsort3Troughed [x] = [x]
wsort3Troughed [x,y] = [min x y, max x y]
wsort3Troughed (x1:x2:x3:xs) 
    | and [x1 < x2, x3 < x2]       = x1:x2:(wsort3Troughed(x3:xs))
    | otherwise                     = l1:l3:wsort3Troughed(l2:xs)
    where
        [l1,l2,l3] = Data.List.sort([x1,x2,x3])
