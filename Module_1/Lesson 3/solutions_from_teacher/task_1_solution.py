input_str = """Hello! My name is Ілля!
My email is illya.khoroshykh@gmail.com. I have 10$ in my pocket. 
& wut 'bout u?'"""

uppercase_string = ""
lowercase_string = ""
new_line_removed_string = ""

for char in input_str:
    ord_char = ord(char)
    if 65 <= ord_char <= 90:
        uppercase_string += char
        lowercase_string += chr(ord_char + 32)
        new_line_removed_string += char
    elif 97 <= ord_char <= 122:
        uppercase_string += chr(ord_char - 32)
        lowercase_string += char
        new_line_removed_string += char
    elif ord_char == 10:
        uppercase_string += char
        lowercase_string += char
    else:
        uppercase_string += char
        lowercase_string += char
        new_line_removed_string += char

print(lowercase_string)
print(uppercase_string)
print(new_line_removed_string)
