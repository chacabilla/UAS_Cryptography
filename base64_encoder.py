from PIL import Image
import io

bin_to_character_table = {
    "000000": "A", "000001": "B", "000010": "C", "000011": "D",
    "000100": "E", "000101": "F", "000110": "G", "000111": "H",
    "001000": "I", "001001": "J", "001010": "K", "001011": "L",
    "001100": "M", "001101": "N", "001110": "O", "001111": "P",
    "010000": "Q", "010001": "R", "010010": "S", "010011": "T",
    "010100": "U", "010101": "V", "010110": "W", "010111": "X",
    "011000": "Y", "011001": "Z", "011010": "a", "011011": "b",
    "011100": "c", "011101": "d", "011110": "e", "011111": "f",
    "100000": "g", "100001": "h", "100010": "i", "100011": "j",
    "100100": "k", "100101": "l", "100110": "m", "100111": "n",
    "101000": "o", "101001": "p", "101010": "q", "101011": "r",
    "101100": "s", "101101": "t", "101110": "u", "101111": "v",
    "110000": "w", "110001": "x", "110010": "y", "110011": "z",
    "110100": "0", "110101": "1", "110110": "2", "110111": "3",
    "111000": "4", "111001": "5", "111010": "6", "111011": "7",
    "111100": "8", "111101": "9", "111110": "+", "111111": "/",
}

character_to_bin_table = {v: k for k, v in bin_to_character_table.items()}

def binary_sum(array):
    word = ''
    equals = ''
    for string in array:
        binary_string = ''
        for char in string:
            if char == '=':
                equals += '='
            else:
                binary_string += bin(ord(char))[2:].rjust(8, '0')

        for i in range(0, len(binary_string), 6):
            chunk = binary_string[i:i + 6]
            word += bin_to_character_table[chunk.ljust(6, '0')]
        word += equals
    return word

class base64:
    def __init__(self, base_input, input_type):
        self.file_name = base_input
        self.input_type = input_type
        if input_type == 'image':
            self.binary_data = self.read_contents()
        elif input_type == 'string':
            self.binary_data = self.string_to_binary(base_input)
        else:
            print("Invalid input type. Please choose between 'image' or 'string'")
            exit()

    def read_contents(self):
        with open(self.file_name, 'rb') as image:
            content = image.read()

        binary_string = ""
        for byte in content:
            binary_value = bin(byte)[2:].zfill(8)
            binary_string += binary_value

        return binary_string

    def string_to_binary(self, string):
        binary_string = ""
        for char in string:
            binary_string += bin(ord(char))[2:].zfill(8)
        return binary_string

    def encode(self):
        if self.input_type == 'string':
            num_substrings = (len(self.binary_data) + 2) // 3
            s = self.binary_data.ljust(num_substrings * 3 * 8, '0')
            substrings = [s[i:i + 24] for i in range(0, num_substrings * 24, 24)]
            base64_encoded = ''
            for substring in substrings:
                for i in range(0, len(substring), 6):
                    chunk = substring[i:i + 6]
                    base64_encoded += bin_to_character_table[chunk.ljust(6, '0')]
            padding_length = (3 - (len(self.binary_data) // 8) % 3) % 3
            return base64_encoded + "=" * padding_length
        else:
            binary_chunks = [self.binary_data[i:i + 6] for i in range(0, len(self.binary_data), 6)]
            encoded_string = ""
            for binary_string in binary_chunks:
                if len(binary_string) != 6:
                    continue
                else:
                    encoded_string += bin_to_character_table[binary_string]

            return encoded_string

    def decode(self, encoded_string):
        binary_string = ''
        for char in encoded_string:
            if char != '=':
                binary_string += character_to_bin_table[char]

        if self.input_type == 'string':
            word = ''
            for i in range(0, len(binary_string), 8):
                word += chr(int(binary_string[i:i + 8], 2))
            return word

        else:
            byte_data = bytes(int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8))
            image = Image.open(io.BytesIO(byte_data))
            image.show()
            
