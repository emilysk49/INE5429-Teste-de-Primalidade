import time

class Xorshift128Plus():
    def __init__(self, seed1=123456789, seed2=987654321):
        if seed1 == 0 and seed2 == 0:
            raise ValueError("Seed não pode ser zero")
        self.state = [seed1 & 0xFFFFFFFFFFFFFFFF, seed2 & 0xFFFFFFFFFFFFFFFF]

    def next(self):
        x = self.state[0]
        s = self.state[1]
        self.state[0] = s

        # x = x XOR (x << 23)
        x ^= (x << 23) & 0xFFFFFFFFFFFFFFFF
        # x = x XOR (x >> 18)
        x ^= (x >> 18) & 0xFFFFFFFFFFFFFFFF
        # x = x XOR (s XOR s >> 5)
        x ^= s ^ ((s >> 5) & 0xFFFFFFFFFFFFFFFF)

        self.state[1] = x
        # operação não-linear -> soma de dois estados x e s
        result = (x + s) & 0xFFFFFFFFFFFFFFFF
        return result
    
    def randBits(self, num_bits):
        result = 0
        bits_collected = 0
        count = 0

        start = time.time()
        while bits_collected < num_bits:
            num = self.next()
            count += 1
            bits_to_add = min(64, num_bits - bits_collected)
            mask = (1 << bits_to_add) - 1
            result |= (num & mask) << bits_collected
            bits_collected += bits_to_add
    
        result |= (1 << (num_bits - 1))
        end = time.time()
        gen_time = end - start

        # print(f"Gerou seguinte valor de {num_bits} bits: {result}")
        # print(f"Tempo para gerar: {gen_time * 1000:.8f} ms")

        return gen_time, result

    
    def measure_avg(self, num_bits, num_exec=100):
        total_time = 0
        for i in range(num_exec):
            gen_time, num = self.randBits(num_bits)
            total_time += gen_time
        avg = total_time / num_exec
        print(f"Média de tempo de geração de número com {num_bits} bits: {avg* 1000:.5f} ms\n")

            
def testXorshift():
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    xorshift = xorshift = Xorshift128Plus()
    
    print("==================================== !!Teste com Xorshift128+!! ====================================")
    for bit in bit_sizes:
        print(f"-------------------- Gerando números com {bit} bits --------------------")
        xorshift.measure_avg(bit)
        
if __name__ == "__main__":
    testXorshift()