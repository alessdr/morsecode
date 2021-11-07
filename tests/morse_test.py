import unittest

from business.morse_business import Morse


class TestMorse(unittest.TestCase):
    def test_mouse_to_text(self):
        mci = Morse('... --- ...')
        result = mci.to_text()
        self.assertEqual(result, 'SOS')

    def test_text_to_morse(self):
        mci = Morse('SOS')
        result = mci.to_morse()
        self.assertEqual(result, '... --- ...')


if __name__ == '__main__':
    unittest.main()
