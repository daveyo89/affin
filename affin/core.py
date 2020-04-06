class Affin:
    def __init__(self):
        self.letters = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyzAÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ" \
                       "+-,?!.:&@#><()=/%\"'’[]$_* "
        self.length = len(self.letters)

    @staticmethod
    def get_valid_numbers() -> tuple:
        af = Affin()
        return tuple((x, y) for x in range(1, 100) for y in range(1, 100) if
                     af.decode((x, y), af.encode((x, y), "lets test if the decoder works properly!"))
                     == "lets test if the decoder works properly!")

    def encode(self, k: (int, int), text: str) -> str:
        return "".join([
            self.letters[((k[0] * self.letters.index(x)) + k[1]) % self.length]
            if x in self.letters else " " for x in text
        ])

    def decode(self, k: (int, int), text: str) -> str:
        return "".join([
            self.letters[((self.letters.index(x) - k[1]) % self.length) * int(k[0] / k[0] ** (-1)) % self.length] for x
            in text
        ])
