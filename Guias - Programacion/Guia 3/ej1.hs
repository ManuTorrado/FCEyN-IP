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
