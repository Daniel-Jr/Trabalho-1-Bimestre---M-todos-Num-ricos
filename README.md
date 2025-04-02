# Trabalho Métodos Numéricos - Chaves RSA

- Trabalho de métodos numéricos com o objetivo de desenvolver, em linguagem Python, uma aplicação modular que implemente o algoritmo RSA de forma “pura” – isto é,
sem o uso de bibliotecas prontas para operações criptográficas, com exceção de uma função para cálculo de fatorial
modular (se necessário). O sistema deve operar com chaves de 128 bits e permitir a criptografia e decriptação de
mensagens em texto, utilizando arquivos para armazenar as chaves e os dados criptografados.


### Geração das chaves "chave_publica.csa" e "chave_privada.cpa"

```console
python3 rsa.py
```

### Encriptação de uma mensagem em texto utilizando a "chave_publica.csa" e salvando em um arquivo chamado "mensagem.cript"

```console
python3 rsa_encrypt.py
```

### Decriptação do aquivo "mensagem.cript" utilzando a chave privada "chave_privada.cpa"

```console
python3 rsa_decrypt.py
```