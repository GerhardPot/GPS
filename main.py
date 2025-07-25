from modules.morse_coder import MorseCode, MorseCodeEncoder

mc = MorseCode()
mc.unencoded_message = "Hello World My name is Gerald Baron the 3rd" 
encoder = MorseCodeEncoder(mc)
encoder.encode()
encoder.display()