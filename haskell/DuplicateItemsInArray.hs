-- Duplicate Items in Array
-- June 14, 2016
--
-- https://programmingpraxis.com/2016/06/14/duplicate-items-in-an-array/
--
-- First, write a program that, given an array of integers in unsorted 
-- order, finds the single duplicate number in the array. For instance, 
-- given the input [1,2,3,1,4], the correct output is 4.
-- 
-- Second, write a program that, given an array of integers in unsorted order,
-- finds all of the multiple duplicate numbers in the array. For instance,
-- given the input [1,2,3,1,2,4,1], the correct output is [1,2,1].
--

-- Compile with
-- $ ghc -main-is DuplicateItemsInArray \
-- $    -o bin/DuplicateItemsInArray. \
-- $    haskell/DuplicateItemsInArray.hs
--
-- Or switch the module name to "Main" to compile without the -main-is flag
--

--module Main where
module DuplicateItemsInArray where

import qualified Data.Map as Map

-- Simplest solution but O(n^2)
duplicate :: (Eq a) => [a] -> Maybe a
duplicate xs = helper xs [] where
    helper ls mapkeys
        | null ls       = Nothing
        | elem l mapkeys  = Just l
        | otherwise     = helper (tail ls) (l:mapkeys)
            where l = head ls

-- Using a hashtable (Map)
duplicateWithHashTable :: (Ord a, Eq a) => [a] -> Maybe a
duplicateWithHashTable xs = helper xs Map.empty where
    helper :: (Ord b, Eq b) => [b] -> Map.Map b Bool -> Maybe b
    helper xs mapkeys
        | null xs               = Nothing
        | Map.member x mapkeys    = Just x
        | otherwise             = helper (tail xs) m
            where
                x = head xs
                m = Map.insert x True mapkeys

-- Collection of duplicates
-- Using a hashtable (Map)
duplicatesWithHashTable :: (Ord a, Eq a) => [a] -> [a]
duplicatesWithHashTable xs = helper xs Map.empty [] where
    helper :: (Ord b, Eq b) => [b] -> Map.Map b Bool -> [b] -> [b]
    helper xs mapkeys acc
        | null xs               = acc
        | Map.member x mapkeys    = helper (tail xs) m (x:acc)
        | otherwise             = helper (tail xs) m acc
            where
                x = head xs
                m = Map.insert x True mapkeys

main :: IO ()
main = do
    print "Printing first duplicate in [1,2,3,1,4]"
    print $ duplicate [1,2,3,1,4]
    print "Printing first duplicate in [1,2,3,1,4] using Hash Table method"
    print $ duplicateWithHashTable [1,2,3,1,4]
    print "Printing first duplicate in [1,2,3,2,5,1,4]"
    print $ duplicate [1,2,3,2,5,1,4]
    print "Printing first duplicate in [1,2,3,2,5,1,4] using Hash Table method"
    print $ duplicateWithHashTable [1,2,3,2,5,1,4]
    print "Printing duplicates in [1,2,3,1,4,2,1]"
    print $ duplicatesWithHashTable [1,2,3,1,4,2,1]
