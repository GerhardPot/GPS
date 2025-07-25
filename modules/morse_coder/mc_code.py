class MorseCode:
    def __init__(self):
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

        self.inverted_morse_code_dictionary = {v: k for k, v in self.morse_code_dictionary.items()}

        self.decoded_message = ""
        self.encoded_message = ""