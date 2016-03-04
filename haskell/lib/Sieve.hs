module Sieve where

sieve n = helper  [] [2,3..n] where
    helper ps [] = reverse ps
    helper ps (xh:xs) = helper (xh:ps) (filter (\x -> (mod x xh /= 0)) xs)

--TODO implement an infinite Sieve
