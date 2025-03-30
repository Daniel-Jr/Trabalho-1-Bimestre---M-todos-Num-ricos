
from primes import exponentiation_by_squaring

def rsa_decrypt(crypt_message: str = "message.cript" , private_key: str = "chave_privada.csa"):
  
  try:
    fo = open(crypt_message, 'r')

    # check for the possibility that the user tries to encrypt something
    # using a public key that is not found
  except FileNotFoundError:
      print('That file is not found.')
  else:
    main_block = fo.readline()
    fo.close()

  try:
    fo = open(private_key, 'r')

    # check for the possibility that the user tries to encrypt something
    # using a public key that is not found
  except FileNotFoundError:
      print('That file is not found.')
  else:
      d = int(fo.readline())
      n = int(fo.readline())
      fo.close()
  
  decrypted_characters = []
  blocks = []

  for char in main_block.split(','):
    if char != '':
      blocks.append(int(char))

  for i in blocks:
    char_decrypted = exponentiation_by_squaring(i,d, n)
    decrypted_characters.append(char_decrypted)
  
  decrypted_message = "".join([chr(char) for char in decrypted_characters])

  return decrypted_message


def main():
  message_path = input("Digite o caminho do arquivo criptografado: \n")
  private_key_path = input("Digite o caminho do arquivo da chave privada (chave_privada.csa), se estiver no mesma pasta não digitar nada: \n")

  if private_key_path == "":
    decrypted_message = rsa_decrypt(crypt_message=message_path)
  else:
    decrypted_message = rsa_decrypt(crypt_message=message_path, private_key=private_key_path)
  
  print(decrypted_message)


if __name__ == '__main__':
  main()