import os
from rsa import gen_rsa_keys

base_path = "./"

def main() -> None:
  if os.path.isfile(base_path + 'chave_publica.cpa') and os.path.isfile(base_path + 'chave_privada.csa'):
  
    excluir_chaves = input('Você já tem chaves geradas você que recriar? (s ou n)')
    if (excluir_chaves == "s"):  
  
        os.remove('chave_publica.cpa')
        os.remove('chave_privada.csa')
        gen_rsa_keys()

  gerar_chaves = input('Você quer gerar novas chaves públicas e privadas? (s ou n)')
  if (gerar_chaves == 's'):
    gen_rsa_keys()

  


main()