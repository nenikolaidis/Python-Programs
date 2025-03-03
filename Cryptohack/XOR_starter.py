def xor(input_string):
    result = ""
    for char in input_string:
        result += chr(ord(char) ^ 13)
    return result

input_string = "label"
result_string = xor(input_string)
flag = "crypto{" + result_string + "}"
print(flag)
