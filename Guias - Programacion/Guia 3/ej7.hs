valorAbsoluto:: Float -> Float
valorAbsoluto x | x > 0 = x
                | x == 0 = 0
                |otherwise = x * (-1)

distanciaManhattan:: (Float,Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (p1, p2, p3) (q1,q2, q3) = valorAbsoluto ((p1 - q1) + (p2 - q2) + (p3 - q3)) 
