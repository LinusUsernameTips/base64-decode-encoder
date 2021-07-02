from base64 import *
import string
def decode_encode():
  print('Decode or Encode? 1|2 ')
  d_e = input('--> ')
  if d_e == "1":
    print('Enter the string to decode')
    string_to_decode = input('--> ')
    decoded_string = b64decode(string_to_decode)
    stripped_decoded = str(decoded_string).strip("b'")
    print(f'Heres your decoded string! "{stripped_decoded}"')
    decode_encode()
  elif d_e == "2":
    print('Enter the string to encode')
    string_to_encode = input('--> ')
    encoded_string = b64encode(string_to_encode.encode("utf-8"))
    stripped_encoded = str(encoded_string).strip("b'")
    print(f'Heres your encoded string! "{stripped_encoded}"')
    decode_encode()
decode_encode()
