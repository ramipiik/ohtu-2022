from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self, tuomari, tekoaly):
        super().__init__(tuomari)
        self.tekoaly = tekoaly

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto