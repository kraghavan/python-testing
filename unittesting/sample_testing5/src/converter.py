
class Converter:
    def str_to_ascii(input_str):
        return [ord(char) for char in input_str]

    def ascii_to_str(ascii_list):
        return ''.join(chr(value) for value in ascii_list)
    

# if __name__ == '__main__':
#     input_str = 'Hello, World!'
#     ascii_list = Converter.str_to_ascii(input_str)
#     print(ascii_list)
#     output_str = Converter.ascii_to_str(ascii_list)
#     print(output_str)