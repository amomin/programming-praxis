-- Test Scores
-- May 24, 2016
-- 
-- Given a list of student names and test scores, compute the average 
-- of the top five scores for each student. You may assume each 
-- student has as least five scores.

module TestScores where

import Data.List
import System.Random

data TestScore = TestScore String Int deriving (Show)
testScoreName :: TestScore -> String
testScoreName (TestScore x _) = x
testScoreScore :: TestScore -> Int
testScoreScore (TestScore _ y) = y

equalName :: TestScore -> TestScore -> Bool
equalName x y = (testScoreName x) == (testScoreName y)

compareByName :: TestScore -> TestScore -> Ordering
compareByName x y = compare (testScoreName x) (testScoreName y)

compareByScore :: TestScore -> TestScore -> Ordering
-- Increasing
--compareByScore x y = compare (testScoreScore x) (testScoreScore y)
-- But we want to sort in decreasing order
compareByScore x y = compare (testScoreScore y) (testScoreScore x)

sortByName :: [TestScore] -> [TestScore]
sortByName = sortBy compareByName

sortDecByScore :: [TestScore] -> [TestScore]
sortDecByScore = sortBy compareByScore

groupByName :: [TestScore] -> [[TestScore]]
-- groupByName x = map groupBy equalName $ sortByName x
groupByName = (groupBy equalName) . sortByName

averageScores :: [TestScore] -> TestScore
averageScores [] = TestScore "" 0 
averageScores xs = helper xs (testScoreName (head xs)) 0 0 where
    helper :: [TestScore] -> String -> Int -> Int -> TestScore
    helper [] name sm cnt = TestScore name (div sm cnt)
    helper ((TestScore _ x):xs) name sm cnt = helper xs name (sm + x) (cnt + 1)

topFiveAverages :: [TestScore] -> [TestScore]
topFiveAverages = (map (averageScores . (take 5))) . (map sortDecByScore) . groupByName
--topFiveAverages x = map (averageScores . (take 5)) $ groupByName x where 

--- Helper for the demonstration below
--randomlist :: Int -> StdGen -> [Int]
--randomlist n = take n . unfoldr (Just . random)
randomscores :: Int -> Int -> Int -> StdGen -> [Int]
randomscores lo hi n = take n . unfoldr (Just . randomR (lo,hi))

main :: IO ()
main = do
    print "--------------- Example 1: -----------------"
    let as = map (\x -> TestScore "Al" x) [15,20..100]
    let bs = map (\x -> TestScore "Bob" x) [80,82..95]
    let cs = map (\x -> TestScore "Carol" x) [60,62..85]
    let ts = concat [as, bs, cs]
    print "List of scores:"
    print ts
    print "Top five averages:"
    print (topFiveAverages ts)
    print "New List of scores:"
    let ts = concat [as, bs, cs, as, as, bs, as]
    print ts
    print "New Top five averages:"
    print (topFiveAverages ts)
    print "--------------- Example 2: -----------------"
    let nSamples = 30
    let loscore = 20
    let hiscore = 99
    gen <- newStdGen
    let xs = take nSamples $ randomRs ('a','c') gen
    --let nlist = [1..100]
    let nlist = randomscores loscore hiscore nSamples gen
    let zs = zip xs nlist
    let ts = map (\x -> TestScore ([fst x]) (snd x)) zs
    print "Random list of test scores"
    print ts
    print "List grouped and sorted"
    print $ map sortDecByScore $ groupByName ts
    print "Averages:"
    print (topFiveAverages ts)
