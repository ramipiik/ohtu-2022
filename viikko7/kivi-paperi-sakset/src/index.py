from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tuomari import Tuomari

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
            peli = KPSTekoaly(Tuomari())
        elif vastaus.endswith("c"):
            peli = KPSParempiTekoaly(Tuomari())
        else:
            break
        peli.pelaa()

if __name__ == "__main__":
    main()
