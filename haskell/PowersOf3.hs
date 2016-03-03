module PowersOf3 where

powerOf3 :: Int -> Bool
powerOf3 1 = True
powerOf3 x
    | x < 1 = False
    | (mod x 3) == 0 = powerOf3 (quot x 3)
    | otherwise = False

powerOf3' :: Int -> Bool
powerOf3' x = helper x 1 where
    helper x n
        | x < 1 = False
        | n > x = False
        | x == n = True
        | otherwise = helper x (3*n)
