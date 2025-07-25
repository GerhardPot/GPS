from .mc_code import MorseCode

class MorseCodeDecoder:
    def __init__(self, morse_code: MorseCode):
        self.morse_code = morse_code

    def decode(self):
        encoded_list = list(self.morse_code.encoded_message.rstrip() + ' ')
        decoded_list = []

        substring = ""
        process_list = []

        while encoded_list:
            if encoded_list[0] in self.morse_code.inverted_morse_code_dictionary:
                substring = substring + encoded_list.pop(0)

            elif encoded_list[0] == ' ':
                if substring:
                    process_list.append(substring)
                    substring = ""
                encoded_list.pop(0)
            
            elif encoded_list[0] == '/':
                process_list.append('/')
                encoded_list.pop(0)

        for character in process_list:
            if character == '/':
                decoded_list.append(' ')
            elif character in self.morse_code.inverted_morse_code_dictionary:
                decoded_list.append(self.morse_code.inverted_morse_code_dictionary[character])
        self.morse_code.decoded_message = ''.join(decoded_list)
        print("Message decoded successfully.")

    def display(self):
        print("Decoded Message: " + self.morse_code.decoded_message)