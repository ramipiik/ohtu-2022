import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        leipa = Tuote("Leipä", 3)
        self.kori.lisaa_tuote(leipa)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.hinta(),5)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        leipa = Tuote("Leipä", 3)
        self.kori.lisaa_tuote(leipa)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_kaksi_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),2*3)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
 
        # testaa että metodin palauttaman listan pituus 1
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)
        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
    
    #step 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_ostosoliota(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipä", 3)
        self.kori.lisaa_tuote(leipa)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
    
    #step 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    #step 12
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostosolio_jolla_on_sama_nimi_kuin_tuotteella_ja_lukumaara_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)

    #step 13
    def test_jos_korissa_on_kaksi_samaa_tuotetta_ja_toinen_poistetaan_jaa_koriin_yksi_ostos_jossa_on_yksi_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)
    
    #step 14
    def test_jos_koriin_lisataan_tuote_ja_sama_tuote_poistetaan_on_kori_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)
        self.assertEqual(self.kori.hinta(),0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)
        
    #step 15
    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipä", 3)
        self.kori.lisaa_tuote(leipa)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)