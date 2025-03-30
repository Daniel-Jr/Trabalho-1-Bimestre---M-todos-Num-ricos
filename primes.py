import random
import math
import re

def exponentiation_by_squaring(x: int, k: int,p: int = None) -> int:
  b = bin(k).lstrip('0b')
  r = 1
  for i in b:
     r = r**2
     if i == '1':
      r = r * x
     if p:
      r %= p
  return r

def whitness(a: int , n: int, n1: int,  r: int, u: int) -> bool: 
  #Retorna: Verdadeiro, se houver uma testemunha de que n não é primo. Falso, quando n pode ser primo
  z  = exponentiation_by_squaring(a, r, n)
  if z == 1:
    return False
  
  for i in range(u):
    z = exponentiation_by_squaring(a, 2**i * r, n)
    if z == n1:
      return False

    return True


def miler_rabin_primality_test(n: int, k: int = 5) -> bool:
  # Implementação do teste de primalidade de Miler-Rabin
  
  if n == 2:
    return True

  if not(n & 1):
     return False
  
  n1, u = n - 1, 0
  r = n1

  while r % 2 == 0:
    r >>= 1
    u += 1

  assert n-1 == 2**u * r

  for _ in range(k):
    a = random.randrange(2, n-2)
    if whitness(a, n, n1, r, u):
      return False
  
  return True

def gen_prime(n: int=512) -> int:

  assert n > 0 and n < 4096

  steps = math.floor(math.log(2**n) / 2)

  x = random.getrandbits(n)


  while True:
    if miler_rabin_primality_test(x, k=7):
      return x
    x = x + 1