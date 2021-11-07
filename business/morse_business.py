from constants.morse_code import MORSE_CODE_DICT


class Morse:

    msg = None

    def __init__(self, msg):
        self.msg = msg

    def to_text(self):
        new_msg = ''
        arr_msg = self.msg.split(' ')
        for item in arr_msg:
            if item.strip():
                new_msg = new_msg + list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(item)]
        return new_msg

    def to_morse(self):
        new_msg = ''
        for char in self.msg:
            new_msg = new_msg + MORSE_CODE_DICT[char]
        return new_msg
