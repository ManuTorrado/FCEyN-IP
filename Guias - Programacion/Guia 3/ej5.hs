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
