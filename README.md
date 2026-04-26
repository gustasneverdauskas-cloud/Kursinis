# AGV maršruto planavimas (Kursinis darbas)
---
## 1. Įžanga
**Tikslas:** Sukurti bepiločio roboto (AGV) simuliatorių, kuris demonstruotų objektinio programavimo (OOP) principus Python kalboje.

**Apie programą:** Tai programėlė, skirta stebėti roboto judėjimą sandėlyje. Robotas reaguoja į naudotojo užsakymus ir atitinkamai randa optimaliausią pristatymo būdą tarp kliūčių ir registruoja visus veiksmus faile.

**Kaip paleisti:**
1. Įsidiekite `Python`.
2. Įsidiekite `pygame` (`pip install pygame`). 
3. Nukopijuokite ir paleiskite kodą: `main.py`.

**Kaip naudotis:**
* Ekrane matysite sandėlius (mėlyni kvadratai); pristatymo vietas (žali kvadratai); kliūtis (pilki kvadratai).
* Apačioje esantys mygtukai "Panaudoti X" ištuštins tam tinkamą terminalą.
* Geltonas kvadratas (AGV) automatiškai nuvažiuos į sandėlį paimti krovinio ir papildyti tuščią terminalą.

---

## 2. Analizė

### 4 OOP elementai

1. **Abstrakcija:** Naudojama `MapObject(ABC)` klasė. Ji nustato bendrą struktūrą visiems žemėlapio objektams, bet pati negali būti sukurta.
2. **Paveldėjimas:** Klasė `Station` paveldi visas savybes iš `MapObject`. Tai leidžia vaikinėms klasėms paveldėti visą tėvinės klasės informaciją.
3. **Enkapsuliacija:** Koordinačių kintamieji `self._x` ir `self._y` yra paslėpti (naudojant `_`), o prieiga prie jų suteikiama tik per saugų `@property` metodą.
4. **Polimorfizmas:** Kiekviena klasė savaip supranta `draw()` metodą. Nors kviečiame tą pačią komandą, stotelės piešiamios kaip 1x1 dydžio kvadratai, o robotas - kaip mažas kvadračiukas.

### Signleton 
Programoje įdiegtas **Singleton** pattern'as (`Logger` klasė). Jis užtikrina, kad visoje sistemoje egzistuotų tik vienas `Log` objektas, atsakingas už rašymą į `log.txt`. Tai yra kaip viena duomenų bazė, kurioje saugoma visa informacija.

### Kompozicija 
`AGV` klasė naudoja kompoziciją: jos konstruktoriuje sukuriamas `Navigator` objektas (`self.nav = Navigator()`). Robotas „turi“ navigaciją, bet jos nepaveldi – tai leidžia lengvai keisti navigacijos parametrus. Bet, jei nebūtų navigacijos, AGV irgi išnyktų.

### Failai
* **Rašymas:** `log(msg)` metodas papildo `log.txt` failą kiekvieną kartą, kai robotas gauna užduotį arba ją įvykdo.
* **Skaitymas:** `last()` metodas nuskaito paskutinę failo eilutę ir atvaizduoja ją UI langelyje (apačioje kairėje).

---

## 3. Rezultatai ir išvados

### Rezultatai 
* Sukurtas veikiantis algoritmas, kuris suras optimaliausią maršrutą nuo taško A iki taško B, net ir esant besikeičiančioms kliūtims.
* Yra eilė (`queue`), leidžianti panaudoti kelis terminalus vienu metu. Robotas paeiliui (nuo seniausios iki naujausios) atlikinės užduotis, kol jų nebeliks ir tada grįš į bazę.
* **Iššūkiai:** Tai buvo vienas didesnių mano programavimo projektų, teko daug ko išmokti. Optimaliausio maršruto funkcijos pats neišgalvojau, teko ją nukopijuoti. Sekantis iššūkis buvo viską grafiškai atvaizduoti. Yra ką veikti. Pamačiau, kiek laiko tenka skirti programėlių ir žaidimų kūrėjams.

### Išvados
Šis projektas parodė, kaip su OOP galima sukurti vos ne bet ką. Mano sukurta programa sugeba: valdyti objektus, saugoti duomenis ir turi UI.

**Ateities perspektyvos:**
* DAUGIAU ROBOTŲŲŲ važinėjančių vienu metu.
* Judančios kliūtys.
* Baterijos integravimas ir pasikrovimo stotys.


