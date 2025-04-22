import time 
    
class MultiplyWithCarry():
    def __init__(self, seed=123456789, carry=12345, a=4294957665, b=2**32, r=2):
        """
        - seed: semente inicial
        - carry: valor inicial do carry
        - a: multiplicador 
        - b: módulo 
        - r: tamanho do lag (quanto resultado anterior vai usar)
        - index: index para acessar memória (state)
        """
        self.state = [seed]
        self.carry = carry
        self.a = a
        self.b = b
        self.r = r
        self.index = 0

    def next(self):
        t = self.a * self.state[self.index] + self.carry
        # x = (a * x(n-r) + c(n-1)) mod b
        x = t % self.b
        # c = (a * x(n-r) + c(n-1)) / b
        self.carry = t // self.b

        # até ter memória de tamanho r, faz append
        if len(self.state) < self.r:
            self.state.append(x)
        else:
            # se já tem tamanho r, só altera o valor
            self.state[self.index] = x
        
        # atualiza index garantindo dentro de memória com tamanho r
        self.index = (self.index + 1) % self.r
        return x
        
    def randBits(self, num_bits):
        result = 0
        bits_collected = 0
        count = 0

        start = time.time()
        # enquanto bits coletado < tamanho de bits de saida
        while bits_collected < num_bits:
            n = self.next()
            count += 1
            # desloca os bits do n para esquerda a quantidade de bits coletado até agora
            # depois faz OR com resultado (concatenando)
            result |= n << bits_collected
            bits_collected += n.bit_length()
        
        end = time.time()
        # cria binario com 1 e resto 0 de tamanho num_bits e faz subtração de 1 -> gera bits com todos 1's
        # aplica essa mascara com resultado (anulando os bits mais significativo desnecessário)
        result &= (1 << num_bits) - 1
        result |= (1 << (num_bits - 1))
        gen_time = end - start

        # print(f"Gerou seguinte valor de {num_bits} bits: {result}")
        # print(f"Tempo para gerar: {gen_time* 1000:.5f} ms e fez {count} execuções\n")

        return gen_time, result
    
    def measure_avg(self, num_bits, num_exec=100):
        total_time = 0
        for n in range(num_exec): 
            time, num = self.randBits(num_bits)
            total_time += time
        avg = total_time/num_exec

        print(f"Média de tempo de geração de número com {num_bits} bits: {avg* 1000:.5f} ms\n")

def test_MWC():
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    mwc = MultiplyWithCarry()

    print("==================================== !!Teste com Multiply With Carry!! ====================================")
    for bit in bit_sizes:
        print(f"-------------------- Gerando números com {bit} bits --------------------")
        mwc.measure_avg(bit)


if __name__ == "__main__":
    test_MWC()



        