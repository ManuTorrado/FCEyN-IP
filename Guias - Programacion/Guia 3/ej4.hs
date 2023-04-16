
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


