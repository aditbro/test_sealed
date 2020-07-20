from typing import List


class InvalidStoreException(Exception):
    pass


def store(inp: List[dict]) -> str:
    result = ''

    for data in inp:
        curr_str = ''
        for key, val in data.items():
            curr_str += '{}={}'.format(key, val)
            if(len(curr_str) > 0):
                curr_str += ';'
        if(curr_str and curr_str[-1] == ';'):
            curr_str = curr_str[:-1]
        result += curr_str
        result += '\n'

    return result


def load(inp: str) -> dict:
    if len(inp) == 0:
        return {}
    
    char_idx: int = 0
    inp_len: int = len(inp)
    result: dict = []

    while(char_idx < inp_len):
        curr_char: str = inp[char_idx]
        curr_dict: dict = {}
        result.append(curr_dict)

        current_key: str = ''
        current_val: str = ''
        status: str = 'key'

        if(curr_char == '\n'):
            char_idx += 1
            continue

        while(not curr_char == '\n' and char_idx < inp_len):
            curr_char = inp[char_idx]

            if(status == 'key' and curr_char == '='):
                status = 'val'
            elif(status == 'key' and curr_char in ';\n'):
                raise InvalidStoreException('delimiter in key value')
            elif(status == 'key'):
                current_key += curr_char
            elif(status == 'val' and curr_char in ';\n'):
                curr_dict[current_key] = current_val
                current_key = ''
                current_val = ''
                status = 'key'
            elif(status == 'val'):
                current_val += curr_char

            char_idx += 1

        if current_key and current_val:
            curr_dict[current_key] = current_val
        elif current_key:
            raise InvalidStoreException('no value provided')

    return result



