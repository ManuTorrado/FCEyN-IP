-- 1)

longitud :: [t] -> Integer
longitud [] =   0
longitud (_:xs) = 1 + longitud xs  

-- 2) 
ultimo :: [t] -> t
ultimo  [x] = x -- El [x] significa que tiene un solo elemento
ultimo (x:xs)	=  ultimo (xs)

-- 3) 
principio :: [t] -> [t] 
principio [x] = [x]
principio (x:xs) =  [x]

-- 4)
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]

-- Ejercicio 2), 1
pertenece ::  (Eq t) => t -> [t] -> Bool
pertenece x [y]    | (x == y) = True
pertenece x [y]    | not (x == y) = False
pertenece x (y:ys) | y == x = True 
pertenece x (y:ys) | otherwise = pertenece x ys

-- Ejercicio 2), 2
todosIguales :: (Eq t) => [t] -> Bool





