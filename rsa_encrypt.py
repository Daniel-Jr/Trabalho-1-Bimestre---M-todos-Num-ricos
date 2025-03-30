from primes import exponentiation_by_squaring

def rsa_encrypt(message: str, public_key:str = "chave_publica.cpa"):
  try:
      fo = open(public_key, 'r')

    # check for the possibility that the user tries to encrypt something
    # using a public key that is not found
  except FileNotFoundError:
      print('That file is not found.')
  else:
      e = int(fo.readline())
      n = int(fo.readline())
      fo.close()

  characters = []
  encrypted_characters = []

  for char in message:
     characters.append(ord(char))
  
  for char in characters:
     char_encrypted = exponentiation_by_squaring(char, e , n)
     encrypted_characters.append(char_encrypted)
  
  return encrypted_characters

def main():
  message = input("Digite uma mensagem que quer criptografar: \n")
  public_key_path = input("Digite o caminho do arquivo da chave publica (chave_publica.cpa), se estiver no mesma pasta não digitar nada:  \n")

  if public_key_path == "":
    encrypted_message = rsa_encrypt(message=message)
  else:
    encrypted_message = rsa_encrypt(message=message, public_key=public_key_path)
  
  f = open("mensagem.cript", "w")
  for char in encrypted_message: 
    f.write(str(char))
    f.write(',')
  f.close()

if __name__ == '__main__':
   main()