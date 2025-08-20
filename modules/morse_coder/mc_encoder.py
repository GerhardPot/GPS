from .mc_code import MorseCode

class MorseCodeEncoder:
    def __init__(self, morse_code: MorseCode):
        if morse_code.decoded_message.strip() == "":
            raise ValueError("GWS: There is nothing to encode")
        else:
            self.morse_code = morse_code

    def encode(self):
        unencoded_list = list(self.morse_code.decoded_message.upper())
        encoded_list = []
        for character in unencoded_list:
            if character == ' ':
                encoded_list.append('/')
            elif character in self.morse_code.morse_code_dictionary:
                encoded_list.append(self.morse_code.morse_code_dictionary[character])
        self.morse_code.encoded_message = ' '.join(encoded_list)
        print("Message encoded successfully.")

    def display(self):
        print("Encoded Message: " + self.morse_code.encoded_message)