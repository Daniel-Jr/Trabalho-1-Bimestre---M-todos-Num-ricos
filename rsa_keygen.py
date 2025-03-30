from math import gcd
from random import randrange
from primes import gen_prime
from euclidean_egcd import xgcd

from typing import Tuple

def RSA_keygen(n: int=512) -> Tuple[int,int,int]:
  # RSA keygen com n -> 512 bits key
  p = gen_prime(n)
  q = gen_prime(n)

  n = p * q

  phi_n = (p - 1) * (q - 1)
  
  while True:
    e = randrange(1, phi_n - 1)
    if gcd(e, phi_n) == 1:
      greatest_common_divsor, s, t = xgcd(phi_n, e)
      if greatest_common_divsor == (s*phi_n + t*e):
        d = t % phi_n
        break
  
  return e, n, d