import unittest
from affin import core


class AffinTest(unittest.TestCase):
    def test_encode_decode(self):
        af = core.Affin()
        text = "Hello bello!"
        encoded = af.encode((97, 15), text)
        decoded = af.decode((97, 15), encoded)
        self.assertEqual(text, decoded, msg=f"{text} -> {encoded} -> {decoded}")
        print("Test complete")


if __name__ == '__main__':
    unittest.main()
