-- Concatenate N N Times
-- May 10, 2016
-- 
-- https://programmingpraxis.com/2016/05/10/concatenate-n-n-times/
--
-- Your task is to write a program that calculates the number that is
-- concatenated to itself the number of times as the number is
-- (that's hard to say).
-- e.g. 4444
-- e.g. 7777777
-- e.g. 121212121212121212121212
-- 

module ConcatenateNNTimes where

import Data.Bits

sol1 :: Integer -> String
sol1 m = helper m m ""
    where
        helper :: Integer -> Integer -> String -> String
        helper n k sofar
            | k < 0     = "Error"
            | k < 1     = sofar
            | otherwise =  helper n (k-1) (sofar ++ (show n))

-- Using binary rep to build in log many steps
repeatStrNTimes :: String -> Integer -> String
repeatStrNTimes str k
    | k < 0             = "Error"
    | k < 1             = ""
    | (mod k 2) == 1    = prev ++ prev ++ str
    | otherwise         = prev ++ prev
        where
            prev = repeatStrNTimes str (k `shiftR` 1)

-- FWIW a more generic version of the above
repeatShowableNTimes :: (Show a) => a -> Integer -> String
repeatShowableNTimes str k
    | k < 0             = "Error"
    | k < 1             = ""
    | (mod k 2) == 1    = prev ++ prev ++ (show str)
    | otherwise         = prev ++ prev
        where
            prev = repeatShowableNTimes str (k `shiftR` 1)

sol2 :: Integer -> String
sol2 m = repeatStrNTimes (show m) m
