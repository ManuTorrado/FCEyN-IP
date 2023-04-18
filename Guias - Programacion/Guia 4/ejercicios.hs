fibonacci:: Integer->Integer
fibonacci n | n == 0 = 0
	          | n == 1 = 1
					  | otherwise = fibonacci(n-1) + fibonacci(n-2) 

parteEntera:: Float -> Integer
parteEntera x | x >= 0 && x < 1 = 0    
	            | otherwise  =  1 + parteEntera(x-1) 

esDivisible:: Integer -> Integer-> Bool
esDivisible x y | x < y = False
	              | (x==y) = True
                | otherwise = esDivisible (x-y) (y)
							  
