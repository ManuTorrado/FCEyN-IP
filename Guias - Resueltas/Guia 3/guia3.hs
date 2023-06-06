f:: Integer -> Integer
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16
    
g:: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1


h:: Integer -> Integer 
h n = f(g(n))

k:: Integer -> Integer 
k n = g(f(n))

-- Ejercicio 2 
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

-- Ejercicio 3 

estanRelacionados:: Integer -> Integer -> Bool
estanRelacionados a b = (a `mod` b  == 0) 

-- Ejercicio 4


-- a)
prodInt:: (Float,Float) -> (Float,Float) -> Float
prodInt (a,b) (c,d) = a*c + d*b

-- b)
todoMenor:: (Float, Float) -> (Float,Float) -> Bool
todoMenor (a,b) (c,d) = (a < c && b < d)

-- c)
distanciaPuntos:: (Float,Float) -> (Float, Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt( (a-b)^2  + (c-d)^2  )

-- d)
sumaTerna:: (Integer, Integer,Integer) -> Integer
sumaTerna (a,b,c) = a + b + c

-- e)
sumarSoloMultiplos:: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n | (a `mod` n == 0) && (b `mod` n == 0) && (c `mod` n == 0) = a + b + c
                             | (a `mod` n == 0) && (b `mod` n == 0) = a + b 
                             | (a `mod` n == 0) && (c `mod` n == 0) = c + a 
                             | (c `mod`n == 0) && (b `mod` n == 0) = b + c 
                             | a `mod` n == 0 = a   
                             | c `mod` n == 0 = c
                             | b `mod` n == 0 = b
                             | otherwise = 0

-- f)

esPar:: Integer -> Bool
esPar x = (x `mod` 2 == 0)

posPrimerPar:: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z) | esPar(x) = 0
                       | esPar(y) = 1
                       | esPar(z) = 2
                       | otherwise = 4

-- g)
crearPar:: t-> t -> (t,t)
crearPar a b = (a,b)


invertir:: (t,t) -> (t,t)
invertir (a,b) = (b,a)


-- Ejercicio 5

esPar:: Integer -> Bool
esPar n = (n `mod` 2 == 0)

f:: Integer -> Integer
f n | n <= 7 = n^2
    | n > 7 = (2*n) - 1

g:: Integer -> Integer
g n | esPar(n) = n `div` 2 
    | otherwise = (3*n) + 1

todosMenores:: (Integer,Integer,Integer) -> Bool
todosMenores (x,y,z) = (f(x) > g(x) && f(y) > g(y) && f(z) > g(z))

-- Ejercicio 6

esMultiplo:: Integer -> Integer -> Bool
esMultiplo x y = (x `mod` y == 0)

bisiesto:: Integer -> Bool
bisiesto x =  not (not (esMultiplo x 4) || (esMultiplo x 100) && not (esMultiplo x 400))
        
         
-- Ejercicio 7

valorAbsoluto:: Float -> Float
valorAbsoluto x | x > 0 = x
                | x == 0 = 0
                |otherwise = x * (-1)

distanciaManhattan:: (Float,Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (p1, p2, p3) (q1,q2, q3) = valorAbsoluto ((p1 - q1) + (p2 - q2) + (p3 - q3)) 


-- Ejercicio 8 


sumaUltimosDosDigitos:: Integer -> Integer
sumaUltimosDosDigitos x  = (x `mod` 10) + ((x `div` 10) `mod` 10)

comparar:: Integer -> Integer -> Integer
comparar x y | sumaUltimosDosDigitos(x) < sumaUltimosDosDigitos(y) = 1
             | sumaUltimosDosDigitos(x) > sumaUltimosDosDigitos(y) = -1
             | sumaUltimosDosDigitos(x) == sumaUltimosDosDigitos(y) = 0
