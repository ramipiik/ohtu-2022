from tekoaly_parannettu import TekoalyParannettu
from kps_tekoaly import KPSTekoaly


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self,tuomari):
        super().__init__(tuomari)
        self.tekoaly = TekoalyParannettu(10)