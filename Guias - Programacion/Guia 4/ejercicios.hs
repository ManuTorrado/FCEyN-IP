fibonacci :: Integer->Integer
fibonacci n | n == 0 = 0
	        | n == 1 = 1
			| otherwise = fibonacci(n-1) + fibonacci(n-2) 

parteEntera :: Float -> Integer
parteEntera x | x >= 0 && x < 1 = 0    
	          | otherwise  =  1 + parteEntera(x-1) 

esDivisible :: Integer -> Integer-> Bool
esDivisible x y | x < y = False
				| (x==y) = True
			    | otherwise = esDivisible (x-y) (y)

-- Funcion auxiliar, te devuelve el enesimo impar que le pidas
imparNumero :: Integer -> Integer 
imparNumero x | x == 1 = 1
              | otherwise = 2 + imparNumero(x-1)

sumaImpares :: Integer -> Integer 
sumaImpares x | x == 1 = 1 
	          | otherwise = imparNumero(x) + sumaImpares(x-1)


-- Ejercicio 5
factorial :: Integer -> Integer 
factorial x | x == 0 = 1
			| otherwise = factorial(x-1) * x

medioFact :: Integer -> Integer
medioFact x | x == 0 = 1
			| x == 1 = 1
			| otherwise = x * medioFact(x-2)

-- Ejercicio 6
sumaDigitos :: Integer -> Integer
sumaDigitos x | x < 10 = x
	          | otherwise = x `mod` 10 + sumaDigitos(x `div` 10)
-- Ejercicio 7  

ultimoDigito :: Integer -> Integer
ultimoDigito x = x `mod` 10

primerDigito :: Integer -> Integer
primerDigito x | x < 10 = x 
               | otherwise = primerDigito(x `div` 10)

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x | x < 10 = True
					  | not ((primerDigito x) == (ultimoDigito x)) = False
					  | otherwise = todosDigitosIguales(x `div` 10)


--Ejercicio 8
cantidadDigitos :: Integer -> Integer
cantidadDigitos x | x < 10 = 1
                  | otherwise = 1 + cantidadDigitos(x `div` 10)
	                
sacaUltimoN :: Integer -> Integer
sacaUltimoN x = x `div` 10

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito x y | cantidadDigitos x == y = ultimoDigito x
	             | otherwise = iesimoDigito ( sacaUltimoN x ) y


-- Esto lo escribimos en clase
sumaInterna :: Integer -> Integer -> Integer -> Integer
sumaInterna q n m | n == 0 = 0 
                  | otherwise = q^(n+1) + sumaInterna q n (m-1)

-- Ejercicio 14 revisar
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias x y z | x == 1 = y + z 
	                | y == 1 && z == 1 = x
                    | y == 1 =  x^z + (sumaPotencias x 1 (z-1))
					| z == 1 =  x^y + (sumaPotencias x (y-1) 1)
	                | otherwise = x^(z+y) + (sumaPotencias x (y-1) (z-1))


-- Ejercicio 18

esPar :: Integer -> Bool
esPar x = (x `mod` 2) == 0

integertail  :: Integer -> Integer
integertail x = x `div` 10

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar x  | esPar(x) &&  (x `div` 10) == x = x
	              | esPar(x `mod` 10) && (x `mod` 10) >  mayorDigitoPar(in|tegertail x ) = x
                  | otherwise = mayorDigitoPar( integertail x  )


