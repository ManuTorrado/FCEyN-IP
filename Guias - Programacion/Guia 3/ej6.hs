esMultiplo:: Integer -> Integer -> Bool
esMultiplo x y = (x `mod` y == 0)

bisiesto:: Integer -> Bool
bisiesto x =  not (not (esMultiplo x 4) || (esMultiplo x 100) && not (esMultiplo x 400))
        
         
