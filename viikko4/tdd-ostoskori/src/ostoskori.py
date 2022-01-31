from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori=[]

    def tavaroita_korissa(self):
        count=0
        for ostos in self.ostokset():
            count+=ostos.lukumaara()
        return count

    def hinta(self):
        count=0
        for ostos in self.ostokset():
            count+=ostos.hinta()
        return count

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostokset():
            if ostos.tuotteen_nimi()==lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self.kori.append(Ostos(lisattava))
        

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostokset():
            if ostos.tuotteen_nimi()==poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara()==0:
                    self.ostokset().remove(ostos)
                return

    def tyhjenna(self):
        self.ostokset().clear()

    def ostokset(self):
        return self.kori


