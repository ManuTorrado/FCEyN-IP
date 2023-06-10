from tester import test, multipleTest
import guia7

test(guia7.raizDe2, 1.4142)
print("-------------------------------------------------------")
test(guia7.factorial_de_2, 2)
print("-------------------------------------------------------")
multipleTest(guia7.factorial_de, [
             1, 1, 2, 6, 24, 120, 720, 5040, 40320], [0, 1, 2, 3, 4, 5, 6, 7, 8])
print("-------------------------------------------------------")
multipleTest(guia7.raiz_cuadrada_de, [
             0.0, 1.0, 2.0, 4.0, 5.0], [0, 1, 4, 16, 25])
