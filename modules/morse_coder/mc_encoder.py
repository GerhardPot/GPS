from .mc_code import MorseCode

class MorseCodeEncoder:
    def __init__(self, morse_code: MorseCode):
        self.morse_code = morse_code

    def encode(self):
        # Get the unencoded string and make it uppercase for the dictionnary lookup
        unencoded_list = list(self.morse_code.unencoded_message.upper())

        # Create a blank list to hold encoded characters
        encoded_list = []

        # Loop through each character in the unencoded list for the encoding process
        for character in unencoded_list:

            # If the character is a space, make it a slash to indicate a space in Morse Code
            if character == ' ':
                encoded_list.append('/')

            # If the character is a letter or digit, get the value for that character from the dictionary
            elif character in self.morse_code.morse_code_dictionary:
                encoded_list.append(self.morse_code.morse_code_dictionary[character])

        # Join the encoded list into a string with spaces between each character
        self.morse_code.encoded_message = ' '.join(encoded_list)
        print("Message encoded successfully.")

    def display(self):
        print("Encoded Message: " + self.morse_code.encoded_message)