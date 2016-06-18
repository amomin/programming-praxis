-- Tomohiko Sakamoto's Day-of-the-Week Algorithms
-- June 17, 2016
--
-- https://programmingpraxis.com/2016/06/17/tomohiko-sakamotos-day-of-week-algorithm/
--
-- Here is Sakamoto's algorithm for calculating the day of the week, taken from 
-- the comment that introduces the code:
-- 
-- Jan 1st 1 AD is a Monday in Gregorian calendar.
-- So Jan 0th 1 AD is a Sunday [It does not exist technically].
-- 
-- Every 4 years we have a leap year. But xy00 cannot be a leap unless xy 
-- divides 4 with reminder 0.
-- 
-- y/4 - y/100 + y/400 : this gives the number of leap years from 1 AD to the given
-- year. As each year has 365 days (divdes 7 with reminder 1), unless it 
-- is a leap year or the date is in Jan or Feb, the day of a given date 
-- changes by 1 each year. In other case it incre"""ases by 2.
-- 
-- y -= m So y + y/4 - y/100 + y/400 gives the day of Jan 0th (Dec 31st 
-- of prev year) of the year. (This gives the reminder with 7 of the number 
-- of days passed before the given year began.)
-- 
-- Array t: Number of days passed before the month 'm+1' begins.
-- 
-- So t[m-1]+d is the number of days passed in year 'y' up to the given date.
--
-- (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7
-- is reminder of the number of days from Jan 0 1AD to the given date
-- which will be the day (0=Sunday,6=Saturday).
-- ... Quotes from comments of original code...
--
-- Your task is to write a program that implements the day-of-week 
-- algorithm shown above.
--

module TomohikoSakamotosDayOfTheWeek where

data Weekday = Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday deriving (Show, Eq)
weekdayFromInt :: Int -> Weekday
weekdayFromInt x
    | y == 0    = Sunday
    | y == 1    = Monday
    | y == 2    = Tuesday
    | y == 3    = Wednesday
    | y == 4    = Thursday
    | y == 5    = Friday
    | y == 6    = Saturday
        where y = (mod x 7)

weekdayToInt :: Weekday -> Int
weekdayToInt x
    | x == Sunday       = 0
    | x == Monday       = 1
    | x == Tuesday      = 2
    | x == Wednesday    = 3
    | x == Thursday     = 4
    | x == Friday       = 5
    | x == Saturday     = 6

data DateYMD = DateYMD Int Int Int
day :: DateYMD -> Int
day (DateYMD _ _ d) = d
month :: DateYMD -> Int
month (DateYMD _ m _) = m
year :: DateYMD -> Int
year (DateYMD y _ _) = y

sol :: DateYMD -> Weekday
sol ymd = weekdayFromInt $ mod (y + (div y 4) - (div y 100) + (div y 400) + t + d) 7
    where
        y1 = year ymd
        m = month ymd
        d = day ymd
        y = if m > 2 then y1 else y1-1
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4] !! (m-1)

main :: IO ()
main = do
    putStrLn "Demo client"
    putStrLn ((show . sol $ DateYMD 2016 06 18) ++ " June 18, 2016")
    putStrLn ((show . sol $ DateYMD 2016 06 19) ++ " June 19, 2016")
    putStrLn ((show . sol $ DateYMD 1980 10 7 ) ++ " October 7, 1980")
    putStrLn ((show . sol $ DateYMD 1985 4  8 ) ++ " April 8, 1985")
    putStrLn ((show . sol $ DateYMD 1981 10 28) ++ " October 28, 1981")
    putStrLn ((show . sol $ DateYMD 1944 12 1 ) ++ " December 1, 1944")
    putStrLn ((show . sol $ DateYMD 1941 3  19) ++ " March 19, 1941")
    putStrLn ((show . sol $ DateYMD 1777 07 04) ++ " July 4, 1777")
    putStrLn ((show . sol $ DateYMD 1867 07 01) ++ " July 1, 1867")
    putStrLn ((show . sol $ DateYMD 2016 01 01) ++ " January 1, 2016")
    putStrLn ((show . sol $ DateYMD 2016 02 28) ++ " February 28, 2016")
    putStrLn ((show . sol $ DateYMD 2016 02 29) ++ " February 29, 2016")
