class Irasas:
    def __init__(self, suma):
        self.suma = suma

    def __str__(self):
        return f"{self.suma}"


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

    def __str__(self):
        return f"Pajamos: {self.suma} Eur, siuntėjas - {self.siuntejas}, info - {self.papildoma_informacija}"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __str__(self):
        return f"Išlaidos: {self.suma} Eur, atsiskaitymo būdas - {self.atsiskaitymo_budas}, įsigyta - {self.isigyta_preke_paslauga}"


class Biudzetas:
    def __init__(self):
        self._zurnalas = []

    def prideti_pajamas(self, suma, siuntejas="darbdavys", papildoma_informacija="atlyginimas"):
        irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self._zurnalas.append(irasas)

    def prideti_islaidas(self, suma, atsiskaitymo_budas="kortele", isigyta_preke_paslauga="pirkinys"):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self._zurnalas.append(irasas)

    def balansas(self):
        bendra = 0
        for irasas in self._zurnalas:
            if type(irasas) is PajamuIrasas:
                bendra += irasas.suma
            if type(irasas) is IslaiduIrasas:
                bendra -= irasas.suma
        print(bendra)
        return bendra

    def ataskaita(self):
        print("Ataskaita:")
        for irasas in self._zurnalas:
            print(irasas)
        print("--------------")


biudzetas1 = Biudzetas()
while True:
    veiksmas = int(
        input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - balansas \n4 - ataskaita \n5 - išeiti iš programos"))
    if veiksmas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        biudzetas1.prideti_pajamas(suma)
    if veiksmas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        biudzetas1.prideti_islaidas(suma)
    if veiksmas == 3:
        biudzetas1.balansas()
    if veiksmas == 4:
        biudzetas1.ataskaita()
    if veiksmas == 5:
        print("Viso gero")
        break
