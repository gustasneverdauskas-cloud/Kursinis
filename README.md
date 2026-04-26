# AGV Simuliacijos Sistema (OOP Kursinis darbas)

## 1. Įžanga
[cite_start]**Tikslas:** Sukurti automatizuoto valdomo transporto (AGV) simuliatorių, kuris demonstruotų objektinio programavimo (OOP) principus Python aplinkoje[cite: 4, 77].

**Apie programą:** Tai interaktyvi aplikacija, skirta stebėti roboto judėjimą sandėlyje. [cite_start]Robotas reaguoja į vartotojo užsakymus, randa trumpiausią kelią (A* algoritmas) tarp kliūčių ir registruoja visus veiksmus faile.

**Kaip paleisti:**
1. Įsitikinkite, kad turite įdiegtą Python 3.x.
2. Įsidiekite `pygame` biblioteką: `pip install pygame`.
3. Paleiskite pagrindinį failą: `python main.py`.

**Kaip naudotis:**
* Ekrane matysite sandėlį (mėlyni kvadratai), terminalus (žali kvadratai) ir kliūtis (pilki kvadratai).
* Apačioje esantys mygtukai "Panaudoti 1-4" leidžia iškviesti robotą į konkretų terminalą.
* Geltonas kvadratas (AGV) automatiškai nuvažiuos į sandėlį paimti krovinio ir pristatys jį į tikslą.

---

## 2. Analizė (OOP principų įgyvendinimas)

### [cite_start]4 OOP poliai 

1. **Abstrakcija:** Naudojama `MapObject(ABC)` klasė. Ji nustato bendrą struktūrą visiems žemėlapio objektams, bet pati negali būti sukurta.
2. **Paveldėjimas:** Klasė `Station` paveldi visas savybes iš `MapObject`. Tai leidžia pakartotinai naudoti kodą pozicijai valdyti.
3. **Enkapsuliacija:** Koordinačių kintamieji `self._x` ir `self._y` yra paslėpti (naudojant `_` prefiksą), o prieiga prie jų suteikiama tik per saugų `@property` metodą.
4. **Polimorfizmas:** Kiekviena klasė savaip įgyvendina `draw()` metodą. Nors kviečiame tą pačią komandą, stotelė piešiama kaip kvadratas, o robotas - kaip mažesnis judantis objektas.

### [cite_start]Dizaino šablonas (Design Pattern) 
Programoje įdiegtas **Singleton** šablonas (`Logger` klasė). Jis užtikrina, kad visoje sistemoje egzistuotų tik vienas žurnalo objektas, atsakingas už rašymą į `log.txt`. Tai apsaugo nuo failo konfliktų.

### [cite_start]Kompozicija 
`AGV` klasė naudoja kompoziciją: jos konstruktoriuje sukuriamas `Navigator` objektas (`self.nav = Navigator()`). Robotas „turi“ navigaciją, bet jos nepaveldi – tai leidžia lengvai pakeisti navigacijos algoritmą neliečiant roboto logikos.

### [cite_start]Darbas su failais 
* **Rašymas:** `log(msg)` metodas papildo `log.txt` failą kiekvieną kartą, kai robotas gauna užduotį arba ją įvykdo.
* **Skaitymas:** `last()` metodas nuskaito paskutinę failo eilutę ir atvaizduoja ją vartotojo sąsajoje (UI) realiu laiku.

---

## 3. Rezultatai ir išvados

### [cite_start]Rezultatai 
* Sukurta veikianti grafinė simuliacija su kliūčių išvengimo algoritmu.
* Įgyvendinta užduočių eilė (`queue`), leidžianti vartotojui pateikti kelis užsakymus vienu metu.
* **Iššūkiai:** Sudėtingiausia dalis buvo užtikrinti sklandų roboto judėjimą ir A* algoritmo integravimą su Pygame kadrų dažniu.

### Išvados [cite: 78]
Šis projektas parodė, kaip OOP principai padeda struktūrizuoti sudėtingas sistemas. Programa pasiekė visus iškeltus tikslus: objektų valdymą, duomenų išsaugojimą ir vartotojo sąveiką.

**Ateities perspektyvos:**
* Galimybė valdyti kelis AGV robotus vienu metu (vengiant susidūrimų).
* Dinaminis kliūčių pridėjimas pelytės paspaudimu.
* Detalesnė statistika apie pristatymo laiką.


