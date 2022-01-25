from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.kori=[]

    def tavaroita_korissa(self):
        # pass
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        count=0
        for ostos in self.ostokset():
            count+=ostos.lukumaara()
        return count

    def hinta(self):
        count=0
        for ostos in self.ostokset():
            count+=ostos.hinta()
        return count
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        # pass
        for ostos in self.ostokset():
            if ostos.tuotteen_nimi()==lisattava:
                ostos.muuta_lukumaaraa(1)
                return
        
        self.kori.append(Ostos(lisattava))
        

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self.kori


