-- Compile with
-- $ ghc -main-is NutsAndBolts \
-- $    -o bin/NutsAndBolts. \
-- $    haskell/NutsAndBolts.hs
--

module NutsAndBolts where

import Data.List
import Data.Maybe
import Text.Printf

solution1 :: (Ord a) => [a] -> [a] -> Maybe a
solution1 nuts [] = Nothing
solution1 nuts bolts = Just (helper nuts bolts (head bolts))

helper :: (Ord a) => [a] -> [a] -> a -> a
helper _ [] biggest = biggest
helper [] bolts biggest = biggest
helper nuts (b:bs) biggest = let ns = filter (>= b) nuts in
    helper ns bs (if (length ns) < (length nuts) then b else biggest)


maybeHead :: [a] -> Maybe a
maybeHead [] = Nothing
maybeHead x = Just (head x)

maybeFst :: Maybe (a, b) -> Maybe a
maybeFst = fmap fst
--maybeFst Nothing = Nothing
--maybeFst (Just x) = Just (fst x)

solution2 :: (Ord a) => [a] -> [a] -> Maybe a
solution2 nuts bolts = maybeFst 
                     . maybeHead
                     -- [(b,l), with l decreasing]
                     . (sortBy (\x y -> compare (snd x) (snd y)))
                     . (map (\(x,y) -> (x, length y)))
                     -- [(b1,[n11, n12,...]), (b2,[n21,n22,...]),....] where bi <= nij
                     $ map (\x -> (x, filter (>= x) nuts)) bolts

main :: IO ()
main = do
    let test_cases = [
                      [
                       [1], []
                      ],
                      [
                       [], [1]
                      ],
                      [
                       [1], [2]
                      ],
                      [
                       [2], [1]
                      ],
                      [
                       [1,3,4], [2,4,5]
                      ],
                      [
                       [2,4,5], [1,3,4]
                      ],
                      [
                       [7,8,9], [1,3,4]
                      ],
                      [
                       [1,3,4], [7,8,9]
                      ]
                     ] :: [[[Int]]]
    let run_testcase = \test_case -> do
                                print $ "Nuts: " ++ show (test_case!!0)
                                print $ "Bolts: " ++ show (test_case!!1)
                                print $ solution1 (test_case!!0) (test_case!!1)
                                print $ solution2 (test_case!!0) (test_case!!1)
    
    mapM_ run_testcase test_cases
