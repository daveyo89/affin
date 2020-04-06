import unittest, random
from affin import core


class AffinTest(unittest.TestCase):
    def test_long_encode(self):
        af = core.Affin()
        text = "A Babar 1989-től 2001-ig vetített kanadai–francia televíziós rajzfilmsorozat, " \
               "amely Jean de Brunhoff 1931-ben megjelent könyvéből készült."
        key = random.choice(af.get_valid_numbers(text))
        encoded = af.encode(key, text)
        decoded = af.decode(key, encoded)
        self.assertEqual(text, decoded, msg=f"{text} -> {encoded} -> {decoded}")
        print(encoded)
        print(decoded)
        print("Test jenkins trigger")


if __name__ == '__main__':
    unittest.main()
