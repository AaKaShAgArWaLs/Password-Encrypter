
def bin(con_str):
    binary_list = [int(format(ord(char), '08b')) for char in con_str]
    return binary_list

def strin(bina):
    decimal_num = int(bina, 2)
    result_str = chr(decimal_num)
    return result_str