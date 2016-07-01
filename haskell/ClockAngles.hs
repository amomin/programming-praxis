-- Clock Angles
-- July 01, 2016
--
-- https://programmingpraxis.com/2016/07/01/clock-angles/
--
-- Write a program that, given a time as hours and minutes (using 
-- a 12-hour clock), calculates the angle between the two hands. For
-- instance, at 2:00 the angle is 60 degrees.
-- 
-- Compile with
-- $ ghc -main-is ClockAngles \
-- $    -o bin/ClockAngles. \
-- $    haskell/ClockAngles.hs
--
-- Or switch the module name to "Main" to compile without the -main-is flag

module ClockAngles where

import Text.Printf

data ClockTime = ClockTime Int Int
instance Show ClockTime where
    show (ClockTime x y) = printf "%02d:%02d" x y
-- Not necessary to provide getters here
--hour :: ClockTime -> Int
--hour (ClockTime h _) = h
--minute :: ClockTime -> Int
--minute (ClockTime _ m) = m

angleDifference :: ClockTime -> Int
angleDifference (ClockTime h m) = min_diff where
    pos_diff = if (a1 > a2) then (a1 - a2) else (a2 - a1)
    min_diff = if (pos_diff <= 180) then pos_diff else 360 - pos_diff
    _h = mod h 12
    _m = mod m 60
    a1 = mod (div (60 * _h + _m) 2) 360
    a2 = mod (6 * _m) 360

main :: IO ()
main = do
    print $ ClockTime 1 20
    print $ angleDifference (ClockTime 1 20)

    let output_clocktime_angle_difference = print . (\c -> "At " ++ show c ++ " angle difference is " ++ (show $ angleDifference c))

    let cts_on_the_hour = map (\x -> ClockTime x 0) [0..11]
    let cts_on_the_half = map (\x -> ClockTime x 30) [0..11]
    let cts_quarter_past = map (\x -> ClockTime x 15) [0..11]
    let cts_quarter_to = map (\x -> ClockTime x 45) [0..11]
    let cts_nearest_angles =
            [
            ClockTime 1 5,
            ClockTime 2 11,
            ClockTime 3 16,
            ClockTime 4 22,
            ClockTime 5 27,
            ClockTime 6 33,
            ClockTime 7 38,
            ClockTime 8 43,
            ClockTime 9 49,
            ClockTime 10 54
            ]

    mapM_ output_clocktime_angle_difference cts_on_the_hour
    mapM_ output_clocktime_angle_difference cts_on_the_half
    mapM_ output_clocktime_angle_difference cts_quarter_past
    mapM_ output_clocktime_angle_difference cts_quarter_to
    mapM_ output_clocktime_angle_difference cts_nearest_angles
