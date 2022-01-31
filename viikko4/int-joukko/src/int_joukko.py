class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.alkioiden_lkm = 0
        self.lukujono=[]

    def is_part_of(self, n):
        if n in self.lukujono:
            return True
        return False

    def add(self, number_to_add):
        if not self.is_part_of(number_to_add):
            self.lukujono.append(number_to_add)
            self.alkioiden_lkm=len(self.lukujono)

    def remove(self, n):
        if n in self.lukujono:
            self.lukujono.remove(n)
            self.alkioiden_lkm=len(self.lukujono)

    def to_int_list(self):
        return self.lukujono

    def yhdiste(a, b):
        x = IntJoukko()
        x.lukujono=a.lukujono+b.lukujono
        return x

    def leikkaus(a, b):
        y = IntJoukko()
        for item in a.to_int_list():
            if item in b.to_int_list():
                y.add(item)
        return y

    def erotus(a, b):
        z = IntJoukko()
        for item in a.to_int_list():
            if item not in b.to_int_list():
                z.add(item)
        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        output = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            output += str(self.lukujono[i]) + ", "
        output += str(self.lukujono[self.alkioiden_lkm - 1]) + "}"
        return output
