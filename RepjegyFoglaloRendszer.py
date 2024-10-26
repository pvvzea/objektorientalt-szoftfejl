# Ez egy alapvető a repülőjegy foglalási rendszer
from abc import ABC, abstractmethod
from datetime import datetime

# 1. Lépés: Osztályok definiálása
# Absztrakt Járat osztály
# Ez az osztály lesz a szülőosztály, amelyből a belföldi és nemzetközi járatok származnak.
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass

# A járatok két típusúak lehetnek: belföldi és nemzetközi.
# Ezek öröklik a Jarat osztályt, és saját specifikus metódusaik lehetnek.
# Belföldi járat osztály
class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_tipus(self):
        return "Belföldi"

# Nemzetközi járat osztály
class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_tipus(self):
        return "Nemzetközi"

# Légi társaság osztály
# Ez az osztály tartalmazza a különböző járatokat, és kezeli azok listáját.
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def foglalas_hozzaadasa(self, foglalas):
        self.foglalasok.append(foglalas)

    def foglalas_torlese(self, foglalas_id):
        self.foglalasok = [
            f for f in self.foglalasok
                if f.foglalas_id != foglalas_id
        ]

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincs elérhető foglalás.")
        else:
            for foglalas in self.foglalasok:
                print(
                    f"Foglalás ID: {foglalas.foglalas_id}, "
                    f"Járat: {foglalas.jarat.jaratszam}, "
                    f"Célállomás: {foglalas.jarat.celallomas}, "
                    f"Utas: {foglalas.utas_nev}, "
                    f"Ár: {foglalas.jarat.jegyar} Ft"
                )

    def jaratok_listazasa(self):
        if not self.jaratok:
            print("Nincs elérhető járat.")
        else:
            for jarat in self.jaratok:
                print(f"Járatszám: {jarat.jaratszam}, Célállomás: {jarat.celallomas}, "
                      f"Típus: {jarat.jarat_tipus()}, Ár: {jarat.jegyar} Ft")

# Jegy foglalás osztály
#Ez az osztály kezeli a jegyfoglalásokat.
class JegyFoglalas:
    def __init__(self, foglalas_id, jarat, utas_nev, foglalas_datum):
        self.foglalas_id = foglalas_id
        self.jarat = jarat
        self.utas_nev = utas_nev
        self.foglalas_datum = foglalas_datum
# ****** Osztályok definiálásának vége ******

# 2. Lépés: a rendszer betöltése
# Rendszer inicializálása néhány alapértelmezett járattal és foglalással
def rendszer_inditas():
    legi_tarsasag = LegiTarsasag("SkyTravel")

    # Előre létrehozott járatok
    belfoldi_jarat1 = BelfoldiJarat("B001", "Budapest", 5000)
    belfoldi_jarat2 = BelfoldiJarat("B002", "Debrecen", 5000)
    nemzetkozi_jarat = NemzetkoziJarat("N001", "London", 20000)

    legi_tarsasag.jarat_hozzaadasa(belfoldi_jarat1)
    legi_tarsasag.jarat_hozzaadasa(belfoldi_jarat2)
    legi_tarsasag.jarat_hozzaadasa(nemzetkozi_jarat)

    # Előre létrehozott foglalások
    foglalas1 = JegyFoglalas("F001", belfoldi_jarat1, "Kiss Anna", datetime.now())
    foglalas2 = JegyFoglalas("F002", belfoldi_jarat2, "Nagy Béla", datetime.now())
    foglalas3 = JegyFoglalas("F003", nemzetkozi_jarat, "Tóth Csaba", datetime.now())

    legi_tarsasag.foglalas_hozzaadasa(foglalas1)
    legi_tarsasag.foglalas_hozzaadasa(foglalas2)
    legi_tarsasag.foglalas_hozzaadasa(foglalas3)

    return legi_tarsasag
# ****** rendszer betöltés vége ******

# 3. Lépés: funkciók megadása
# Foglalási funkciók
def jegy_foglalasa(legi_tarsasag):
    jaratszam = input("Adja meg a járatszámot: ")
    utas_nev = input("Adja meg az utas nevét: ")
    for jarat in legi_tarsasag.jaratok:
        if jarat.jaratszam == jaratszam:
            foglalas_id = f"F{len(legi_tarsasag.foglalasok) + 1:03}"
            foglalas = JegyFoglalas(foglalas_id, jarat, utas_nev, datetime.now())
            legi_tarsasag.foglalas_hozzaadasa(foglalas)
            print(f"Foglalás sikeres. Ár: {jarat.jegyar} Ft")
            return
    print("Nincs ilyen járat.")

def foglalas_lemondasa(legi_tarsasag):
    foglalas_id = input("Adja meg a foglalás ID-ját: ")
    for foglalas in legi_tarsasag.foglalasok:
        if foglalas.foglalas_id == foglalas_id:
            legi_tarsasag.foglalas_torlese(foglalas_id)
            print("Foglalás lemondva.")
            return
    print("Nincs ilyen foglalás.")

def foglalasok_listazasa(legi_tarsasag):
    legi_tarsasag.foglalasok_listazasa()

def jaratok_listazasa(legi_tarsasag):
    legi_tarsasag.jaratok_listazasa()

# ****** funkciók vége ******

# 4. Lépés: a futó program és menü
# Egyszerű konzolos felhasználói interfészt készíthetünk a jegyfoglalások kezeléséhez.
# Fő program
def main():
    legi_tarsasag = rendszer_inditas()

    while True:
        print("\n1. Jegy foglalása\n2. Foglalás lemondása\n3. Foglalások listázása\n4. Járatok listázása\n5. Kilépés")
        valasztas = input("Válasszon egy opciót: ")

        if valasztas == "1":
            jegy_foglalasa(legi_tarsasag)
        elif valasztas == "2":
            foglalas_lemondasa(legi_tarsasag)
        elif valasztas == "3":
            foglalasok_listazasa(legi_tarsasag)
        elif valasztas == "4":
            jaratok_listazasa(legi_tarsasag)
        elif valasztas == "5":
            print("Kilépés a programból.")
            break
        else:
            print("Érvénytelen opció. Kérem, próbálja újra.")

# ****** futó program és menü vége ******

if __name__ == "__main__":
    main()
