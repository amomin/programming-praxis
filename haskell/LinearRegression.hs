-- Linear Regression 
-- June 10, 2016  
--
-- https://programmingpraxis.com/2016/06/10/linear-regression/
--
-- Linear regression is a widely-used statistical technique for relating 
-- two sets of variables, traditionally called x and y; the goal is to find 
-- the line-of-best-fit, y = m x + b, that most closely relates the two 
-- sets.  Your task is to write a program that calculates the slope m and 
-- intercept b for two sets of variables x and y.
-- 

-- Input is list of x-coordinates followed by list of y-coordinates
linearRegression1 :: [Float] -> [Float] -> (Float,Float)
linearRegression1 xs ys = (m, b) where
    n = fromIntegral $ length xs
    m = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    b = (sy - m * sx) / n
    sx = sum xs
    sy = sum ys
    sxx = sum $ zipWith (*) xs xs
    sxy = sum $ zipWith (*) xs ys

-- Input is list of points
linearRegression2 :: [(Float,Float)] -> (Float,Float)
linearRegression2 xys = (m, b) where
    xs :: [Float]
    ys :: [Float]
    (xs, ys) = unzip xys 
    n = fromIntegral $ length xs
    m = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    b = (sy - m * sx) / n
    sx = sum xs
    sy = sum ys
    sxx = sum $ zipWith (*) xs xs
    sxy = sum $ zipWith (*) xs ys
