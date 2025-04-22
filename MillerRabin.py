import random
import time
from MWC import MultiplyWithCarry
from Xorshift128plus import Xorshift128Plus

def MillerRabin(n, k=5):
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
    if n==2 or n==3 or n==5 or n==7:
        return True
    
    # fatorando n - 1 em n^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        # dividindo d por 2 (usando shift a direita)
        d = d >> 1
        # conta quantas divisão por 2 vez
        s += 1

    for _ in range(k):
        # 1 < a < n - 1
        a = random.randrange(2, n-1)
        # x = a^d mod n
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(s - 1):
            # x = x^2 mod n
            x = pow(x, 2, n)
            # se x = n - 1, sai desse loop
            if x == n - 1:
                break
        else:
            return False
    return True

def gen_prime(num_bits, algorithm='MWC'):
    # verifica qual gerador de numeros vai usar
    if algorithm == 'MWC':
        generator = MultiplyWithCarry()
    else:
        generator = Xorshift128Plus()

    # contador de quantas tentativas para achar primo
    count = 1
    start = time.time()
    _, num = generator.randBits(num_bits)

    # se o numero gerado for par, troca para impar
    if num & 1 == 0:
        num |= 1

    # enquanto numero não é primo, continua gerando e testando
    while not MillerRabin(num):
        _, num = generator.randBits(num_bits)
        if num & 1 == 0:
            num |= 1
        count += 1
    
    end = time.time()
    gen_time = end - start
    print(f"{algorithm} - ACHOU NUMERO PRIMO COM {num_bits} bits: {num} em {gen_time:.7f} s, com {count} tentativas")


if __name__ == "__main__":
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    for bit in bit_sizes:
        gen_prime(bit)
        gen_prime(bit, algorithm='XORSHIFT')
        print('\n')
