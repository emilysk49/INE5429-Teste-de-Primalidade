from MillerRabin import *
from Fermat import *

n = 561
composites = [561, 1105, 1729, 2465, 6601, 2047, 1373653, 25326001]
for n in composites:
    if MillerRabin(n):
        print(f"Teste de Primalidade Miller Rabin: {n} é primo")
    else:
        print(f"Teste de Primalidade Miller Rabin: {n} NÃO é primo")

    if Fermat(n):
        print(f"Teste de Primalidade Fermat: {n} é primo")
    else:
        print(f"Teste de Primalidade Fermat: {n} NÃO é primo")