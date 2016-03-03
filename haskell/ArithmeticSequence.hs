module ArithmeticSequence where

import Data.List

solution1 :: [Int] -> Bool
solution1 xs = (== 1) 
    $ length 
    $ nub 
    $ zipWith (\x y -> x-y) ys (tail ys)
        where ys = (sort xs)
