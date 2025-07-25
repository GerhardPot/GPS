from modules.morse_coder import MorseCode, MorseCodeEncoder, MorseCodeDecoder

ec = MorseCode()
ec.decoded_message = "Hello World My name is Gerald Baron the 3rd" 

encoder = MorseCodeEncoder(ec)
encoder.encode()
print("Encoded Message: " + ec.encoded_message)

dc = MorseCode()
dc.encoded_message = ec.encoded_message
decoder = MorseCodeDecoder(dc)
decoder.decode()
print("Decoded Message: " + dc.decoded_message)
