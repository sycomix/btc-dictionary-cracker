from bitcoin import *
from hashlib import sha256

def try_word(word):
  print(f'Palabra {word}')
  priv = sha256(word).hexdigest()
  print(f'Private Key:{priv}')
  pub = privtopub(priv)
  print(f'Public Key:{pub}')
  addr = pubtoaddr(pub)
  print(f'Address:{addr}')
  # h = history(addr)
  # print(h)
  h = unspent(addr)
  print(f'Cantidad {len(h)}')
  return len(h) > 0

with open('encontrados.txt', 'w') as output_file:
  with open('smalldict.txt') as f:
    content = f.readlines()
    words = [x.strip() for x in content]
    for word in words:
      output_file.write(word + '\n')
      if try_word(word):
        raise ValueError('Holy shit')
        