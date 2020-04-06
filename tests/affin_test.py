import unittest
from affin import core


class AffinTest(unittest.TestCase):
    def test_encode_decode(self):
        af = core.Affin()
        text = "Hello bello!"
        encoded = af.encode((97, 15), text)
        decoded = af.decode((97, 15), encoded)
        self.assertEqual(text, decoded, msg=f"{text} -> {encoded} -> {decoded}")

    def test_long_encode(self):
        af = core.Affin()
        text = "A Babar 1989-től 2001-ig vetített kanadai–francia televíziós rajzfilmsorozat, amely Jean de Brunhoff 1931-ben megjelent könyvéből készült. Az animációs játékfilmsorozat rendezői Larry Jacobs, Raymond Jafelice, Laura Shepherd és Dale Schott. A zenéjét Milan Kymlicka szerezte. "
        encoded = af.encode((97, 15), text)
        decoded = af.decode((97, 15), encoded)
        self.assertEqual(text, decoded, msg=f"{text} -> {encoded} -> {decoded}")
        print(encoded)
        print(decoded)


if __name__ == '__main__':
    unittest.main()
