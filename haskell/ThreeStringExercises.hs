module ThreeStringExercises where

-- All of these can be done with generic a or at worst Eq a

-- Sorta cheating but really the right answer
solLength1 :: [a] -> Int
solLength1 = length

-- An implementation
solLength2 :: [a] -> Int
solLength2 [] = 0
solLength2 (_:xs) = 1 + solLength2 xs

-- Using foldl
solLength3 :: [a] -> Int
solLength3 = foldl (\acc y -> acc + 1) 0

-- First index starting at index i containing character xc in string xs
solIndexStartingAt1 :: Eq a => Int -> a -> [a] -> Int
solIndexStartingAt1 _ xc [] = -1
solIndexStartingAt1 i xc (x:xs)
    | i < 0     = -1
    | i > 0     = 1 + solIndexStartingAt1 (i-1) xc xs
    | xc == x   = 0
    | xc /= x   = if y > -1 then 1 + y else -1 where y = solIndexStartingAt1 i xc xs

-- Assume starting at index 0
solIndex1 :: Eq a => a -> [a] -> Int
solIndex1 = solIndexStartingAt1 0

-- A little better
solIndexStartingAt2 :: Eq a => Int -> a -> [a] -> Int
solIndexStartingAt2 n ch = (+ n) . (solIndex2 ch) . (drop n)

solIndex2 :: Eq a => a -> [a] -> Int
solIndex2 ch [] = -1
solIndex2 ch (sh:st)
    | ch == sh      = 0
    | ch /= sh      = if y > -1 then 1 + y else -1 where y = solIndex2 ch st

-- More haskelly way
solSubstring2 :: Int -> Int -> [a] -> [a]
solSubstring2 x y = (take (y-x+1)) . (drop x)

-- Cheap direct solution
solSubstring1 :: Int -> Int -> [a] -> [a]
solSubstring1 x y [] = []
solSubstring1 x y (sh:st)
    | x < 0     = []
    | y < x     = []
    | x > 0     = solSubstring1 (x-1) (y-1) st
    -- Now x == 0
    | y >= 0     = sh : (solSubstring1 x (y-1) st)
    -- Now y == 0
    | otherwise  = []
