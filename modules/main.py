from morse_coder.mc_encoder import MorseCodeEncoder

message = "Hello World My name is Gerald Baron the 3rd"
encoder = MorseCodeEncoder(message)
encoder.encode()
encoder.display()