from modules.dice.d_dice import Dice
from modules.dice.d_roll import roll

dice = Dice(12, 2)
roll(dice)
print(dice.current_face_value)
roll(dice)
print(dice.current_face_value)
roll(dice)
print(dice.current_face_value)
roll(dice)
print(dice.current_face_value)
roll(dice)
print(dice.current_face_value)
roll(dice)
print(dice.current_face_value)


# from modules.morse_coder import MorseCode, MorseCodeEncoder, MorseCodeDecoder

# ec = MorseCode()
# ec.decoded_message = "there once was a great flood that washed.... away the lands and all the people that lived within them..." 
# encoder = MorseCodeEncoder(ec)
# encoder.encode()
# print("Encoded Message: " + ec.encoded_message)

# dc = MorseCode()
# dc.encoded_message = ec.encoded_message
# decoder = MorseCodeDecoder(dc)
# decoder.decode()
# print("Decoded Message: " + dc.decoded_message)
