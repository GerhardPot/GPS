class MorseCodeEncoder:
    def __init__(self, unencoded_message):
        self.unencoded_message = unencoded_message.upper()
        self.encoded_message = []
        self.morse_code_dictionary = {
            # Letters
            'A':'.-',
            'B':'-...',
            'C':'-.-.',
            'D':'-..',
            'E':'.',
            'F':'..-.',
            'G':'--.',
            'H':'....',
            'I':'..',
            'J':'.---',
            'K':'-.-',
            'L':'.-..',
            'M':'--',
            'N':'-.',
            'O':'---',
            'P':'.--.',
            'Q':'--.-',
            'R':'.-.',
            'S':'...',
            'T':'-',
            'U':'..-',
            'V':'...-',
            'W':'.--',
            'X':'-..-',
            'Y':'-.--',
            'Z':'--..',

            # Digits
            '1':'.----',
            '2':'..---',
            '3':'...--',
            '4':'....-',
            '5':'.....',
            '6':'-....',
            '7':'--...',
            '8':'---..',
            '9':'----.',
            '0':'-----'
        }

    def encode(self):
        for character in self.unencoded_message:
            if character == ' ':
                self.encoded_message.append('/')
            elif character in self.morse_code_dictionary:
                self.encoded_message.append(self.morse_code_dictionary[character])
        print("Message encoded successfully.")

    def display(self):
        print("Encoded Message: " + ' '.join(self.encoded_message))