-- Compile with
-- $ ghc -main-is NutsAndBolts \
-- $    -o bin/NutsAndBolts. \
-- $    haskell/NutsAndBolts.hs
--

module NutsAndBolts where

import Text.Printf

solution1 :: [Int] -> [Int] -> Int
solution1 nuts [] = -1
--solution1 nuts (b:bs) = helper (filter (>= b) nuts) bs b
solution1 nuts bolts = helper nuts bolts (head bolts)

helper :: [Int] -> [Int] -> Int -> Int
helper _ [] biggest = biggest
helper [] bolts biggest = biggest
helper nuts (b:bs) biggest = let ns = filter (>= b) nuts in
    helper ns bs (if (length ns) < (length nuts) then b else biggest)

main :: IO ()
main = do
    let test_cases = [
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
    --test_cases :: [[[Int]]]
    --test_cases = [ [ [1,3,4], [2,4,5] ], [[2,4,5], [1,3,4]] ]

    --let run_testcase = print . (\c -> solution1 (c!!0) (c!!1)) >>= print . (\c -> solution1 (c!!0) (c!!1))
    --let run_testcase = \c -> (print $ solution1 (c!!0) (c!!1)) >>= \c -> (print $ solution1 (c!!0) (c!!1))
    let run_testcase = \test_case -> do
                                print $ "Nuts: " ++ show (test_case!!0)
                                print $ "Bolts: " ++ show (test_case!!1)
                                print $ solution1 (test_case!!0) (test_case!!1)
    
    mapM_ run_testcase test_cases
