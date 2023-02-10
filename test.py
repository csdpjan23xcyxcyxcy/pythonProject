def shift_hex(hex_values, shift_value):
    shifted_hex = ""
    for char in hex_values:
        char_value = int(char, 16)
        print(char_value)
        print(char)
        shifted_char = hex((char_value + shift_value) % 16)[2:].zfill(1)
        print(shifted_char)
        shifted_hex += shifted_char
        print(shifted_hex)
    return shifted_hex


a, b = input('enter the hex').split()

shift_hex(a, b)
