def get_key_to_letters():
    import string
    possible_letters = string.ascii_lowercase
    possible_keys = string.digits
    key_to_letters = {}
    start_index = 0
    for key in possible_keys:
        if key == "0":
            key_to_letters[key] = " "
        elif key == "1":
            key_to_letters[key] = ""
        else:
            num_letters = 3
            if key in {"7","9"}:
                num_letters = 4
            letters = possible_letters[start_index:start_index + num_letters]
            key_to_letters[key] = letters
            start_index += num_letters
    return key_to_letters

def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    '''
    # loop through mapped letters for number of times the key was pressed
    keys_to_letters = get_key_to_letters()
    result = ""
    count = 0
    prev_key = ""
    for curr_key in keys:
        if curr_key == "1"
            pass
        else:
            if not prev_key:
                prev_key = curr_key
                count = 1
            else:
                curr_key = keys_to_letters[key]
                if prev_key == curr_key:
                    if count == len(curr_key):
                        result += letters[-1]
                        count = 1 
                    else:
                        count += 1
                else:
                    prev_letters = keys_to_letters[prev_key]
                    result += prev_letters[count - 1]
                    prev_key = curr_key
                    count = 1
        
    return result

