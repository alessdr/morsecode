from constants.morse_code import MORSE_CODE_DICT
from constants.constants import MSG_ERROR_MORSE, MSG_ERROR_TEXT


class Morse:

    msg = None

    def __init__(self, msg):
        self.msg = msg

    def to_text(self):
        try:
            new_msg = ''
            arr_msg = self.msg.split(' ')
            for item in arr_msg:
                if item != '':
                    new_msg = new_msg + list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(item)]
                else:
                    new_msg = new_msg + ' '
            return new_msg
        except ValueError:
            return MSG_ERROR_MORSE

    def to_morse(self):
        try:
            new_msg = ''
            for char in self.msg:
                if new_msg != '':
                    new_msg = new_msg + ' '
                new_msg = new_msg + MORSE_CODE_DICT[char]
            return new_msg
        except Exception:
            return MSG_ERROR_TEXT
