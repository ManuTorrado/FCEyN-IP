prodInt:: (Float,Float) -> (Float,Float) -> Float
prodInt (a,b) (c,d) = a*c + d*b

todoMenor:: (Float, Float) -> (Float,Float) -> Bool
todoMenor (a,b) (c,d) = (a < c && b < d)

distanciaPuntos:: (Float,Float) -> (Float, Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt( (a-b)^2  + (c-d)^2  )

sumaTerna:: (Integer, Integer,Integer) -> Integer
sumaTerna (a,b,c) = a + b + c
