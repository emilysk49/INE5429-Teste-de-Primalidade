# INE5429-Teste de Primalidade
## 1 - Geradores de números pseudo-aleatórios
Sem alterar vai executar por padrão : tempo médio de 100 execução de cada tamanho de bits.
Para gerar apenas um número de específico de bits use : randBit(num_bits).
### Multiply With Carry
```bash
python3 MWC.py
```
### Xorshift128+
```bash
python3 Xorshift128plus.py
```

## 2 - Teste de Primalidade
Por padrão geram os números primos partir de geradores de MWC e Xorshift. 
Se quiser testar se um número é primo ou não, use: MillerRabin(num) ou Fermat(num).
### Miller-Rabin
```bash
python3 MillerRabin.py
```
### Fermat
```bash
python3 Fermat.py
```
