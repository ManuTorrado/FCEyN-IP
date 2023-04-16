sumaUltimosDosDigitos:: Integer -> Integer
sumaUltimosDosDigitos x  = (x `mod` 10) + ((x `div` 10) `mod` 10)

comparar:: Integer -> Integer -> Integer
comparar x y | sumaUltimosDosDigitos(x) < sumaUltimosDosDigitos(y) = 1
             | sumaUltimosDosDigitos(x) > sumaUltimosDosDigitos(y) = -1
             | sumaUltimosDosDigitos(x) == sumaUltimosDosDigitos(y) = 0
