parteEntera:: Float -> Integer
parteEntera x	 |  (0 <= x && x < 1) = 0
							 |  x>= 1 = 1 + parteEntera(x-1)
