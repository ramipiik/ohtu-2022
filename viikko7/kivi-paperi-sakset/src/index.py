from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus.endswith("a"):
            peli = KPSPelaajaVsPelaaja(Tuomari())
        elif vastaus.endswith("b"):
            peli = KPSTekoaly(Tuomari(), Tekoaly())
        elif vastaus.endswith("c"):
            peli = KPSTekoaly(Tuomari(), TekoalyParannettu(10))
        else:
            break
        peli.pelaa()

if __name__ == "__main__":
    main()
