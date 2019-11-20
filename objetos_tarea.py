class Corcho:
    bodega = ""


class Botella(Corcho):
    elCorcho = None

    def tapar(self):
        self.elCorcho = self.bodega
        return self.elCorcho

    def destapar(self):
        self.elCorcho = None
        return self.elCorcho


nose = Botella()
nose.bodega = "JAJA"
print(nose.destapar())
