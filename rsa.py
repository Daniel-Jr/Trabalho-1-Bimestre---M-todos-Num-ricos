import os
from rsa_keygen import RSA_keygen

base_path = "./"
def gen_rsa_keys(k: int=512):
  # k is bitlength

  e, n, d = RSA_keygen(k)

  f = open("chave_publica.cpa", "w")
  f.write(str(e) + '\n')
  f.write(str(n) + '\n')
  f.close()

  f = open("chave_privada.csa", "w")
  f.write(str(d) + '\n')
  f.write(str(n) + '\n')
  f.close()


def main():
  if os.path.isfile(base_path + 'chave_publica.cpa') and os.path.isfile(base_path + 'chave_privada.csa'):
    excluir_chaves = input('Você já tem chaves geradas você que recriar? (s ou n): \n')
    if (excluir_chaves == "s"):
      os.remove('chave_publica.cpa')
      os.remove('chave_privada.csa')
      key_bits = input('com quantos bits você que criar as chaves (padrão 512 bits): \n')
      gen_rsa_keys(k=int(key_bits))
      return True
  gerar_chaves = input('Você quer gerar novas chaves públicas e privadas? (s ou n): \n')
  if (gerar_chaves == 's'):
    key_bits = input('com quantos bits você que criar as chaves (padrão 512 bits): \n')
    gen_rsa_keys(k=int(key_bits))

if __name__ == '__main__':
   main()