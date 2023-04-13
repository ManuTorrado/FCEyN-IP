absoluto:: Integer -> Integer
absoluto n | n < 0 = -n 
           | n > 0 =  n
           | otherwise = 0 

maximoabsoluto:: Integer -> Integer -> Integer
maximoabsoluto x y | x > y = x
                   | otherwise = y

maximo3::  Integer -> Integer -> Integer -> Integer
maximo3  x y z  | x > y && x > z = x
                | y > x && y > z = y
                | z > y && z > x = z 
                | otherwise = x 


algunoEs0ConPM:: Integer -> Integer -> Bool 
algunoEs0ConPM x y | x == 0  = True
                   | y == 0  = True
                   | otherwise = False

            
                



algunoEs0SinPM:: Integer -> Integer -> Bool 
algunoEs0SinPM x y =  (x == 0 || y == 0) 

ambosSon0SinPm:: Integer -> Integer -> Bool 
ambosSon0SinPm x y =  (x == 0 && y == 0) 


ambosSon0ConPM:: Integer -> Integer -> Bool 
ambosSon0ConPM x y | x == 0 && y == 0 = True
                   | otherwise = False

--mismoIntervalo:: Float -> Float -> Bool
--mismoIntervalo x y = not (x > 3 && y > 3  && x <= 3 && y <= 3)

sumaDistintos:: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x == y = x+z
		    | y == z = z+x
		    | x == z = x+y
		    | otherwise = x + y + z 

esMultiploDe:: Integer -> Integer -> Bool
esMultiploDe x y =  ( x `mod` y == 0 )

digitoUnidades:: Integer -> Integer 
digitoUnidades x = x `mod`10

digitoDecenas:: Integer -> Integer
digitoDecenas x = (x `div` 10) `mod` 10
