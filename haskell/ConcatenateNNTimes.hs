-- Concatenate N N Times
-- May 10, 2016
-- 
-- Your task is to write a program that calculates the number that is
-- concatenated to itself the number of times as the number is
-- (that's hard to say).
-- e.g. 4444
-- e.g. 7777777
-- e.g. 121212121212121212121212
-- 

module ConcatenateNNTimes where

sol1 :: Integer -> String
sol1 m = helper m m ""
    where
        helper :: Integer -> Integer -> String -> String
        helper n k sofar
            | k < 0     = "Error"
            | k < 1     = sofar
            | otherwise =  helper n (k-1) (sofar ++ (show n))
