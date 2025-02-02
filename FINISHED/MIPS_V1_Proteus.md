
- [MIPS - Vezbe 1 - Uvod u korišćenje simulatora Proteus](#mips---vezbe-1---uvod-u-korišćenje-simulatora-proteus)
  - [Kreiranje novog projekta](#kreiranje-novog-projekta)
  - [Radna površina Proteusa](#radna-površina-proteusa)
  - [Zaključak](#zaključak)
  - [Povezivanje signala i komponenti](#povezivanje-signala-i-komponenti)
  - [Kreiranje grafika i postavljanje sondi](#kreiranje-grafika-i-postavljanje-sondi)
  - [Simulacija i analiza rezultata](#simulacija-i-analiza-rezultata)
  - [Instanciranje novih komponenti](#instanciranje-novih-komponenti)
  - [Povezivanje logičkih kola i dioda](#povezivanje-logičkih-kola-i-dioda)
  - [Pokretanje simulacije](#pokretanje-simulacije)
  - [Prakticni Primer](#prakticni-primer)

# MIPS - Vezbe 1 - Uvod u korišćenje simulatora Proteus

Zdravo svima! U ovoj lekciji ćemo se upoznati sa osnovnim funkcionalnostima simulatora Proteus. Pokrenućemo Proteus sa administratorskim privilegijama kako bismo mogli da pristupimo njegovoj internoj biblioteci komponenti. Nakon pokretanja, koristićemo čarobnjak (wizard) za kreiranje novog projekta, do kojeg možemo doći prečicom ili putem menija: **File → New Project**.

## Kreiranje novog projekta

1. **Prvi prozor čarobnjaka** nam nudi mogućnost da dodelimo ime projektu i odredimo lokaciju gde će se projekt nalaziti. U ovom primeru, za ime projekta ćemo izabrati reč "Proteus", a za lokaciju ćemo odabrati folder na desktopu sa istim imenom, tj. "Proteus".

2. **Drugi prozor** se tiče izgleda radne površine. Ovde ćemo prihvatiti podrazumevanu opciju, koja nam u potpunosti odgovara.

3. **Treći prozor** se odnosi na nacrte štampanih ploča. Pošto se mi ne bavimo ovom tematikom na ovom predmetu, odabraćemo opciju koja isključuje nacrte štampanih ploča.

4. **Četvrti prozor** se tiče prisustva izvornog koda u Proteus projektu. Pošto ćemo mi izvorni kod čuvati u drugom integrisanom razvojnom okruženju, nećemo dodavati nikakav izvorni kod u okviru Proteusa.

5. **Peti prozor** se takođe tiče izgleda, i ovde ćemo prihvatiti podrazumevanu opciju.

## Radna površina Proteusa

Nakon ovih koraka, nalazimo se na radnoj površini Proteusa, gde možemo instancirati željene uređaje, odnosno komponente, u cilju simulacije njihovog načina rada.

### Prvi primer: Simulacija jednostavnog strujnog kola

Kao prvi primer, poslužićemo se simulacijom jednostavnog strujnog kola koje se sastoji od dugmeta, diode koja emituje svetlost i otpornika.

#### Instanciranje komponenti

Instanciranje komponenti vrši se u okviru moda za komponente, koji se nalazi ovde. Kada smo u modu za komponente, neophodno je izabrati željenu komponentu iz belog prozora sa desne strane. U ovom prozoru se trenutno ne nalazi ni jedna komponenta jer još nismo izabrali ništa iz biblioteke.

Izbor komponenti iz biblioteke vrši se pomoću opcije **Pick from Library**, koja otvara novi prozor za pretragu komponenti. Pretraga se može vršiti po različitim kriterijumima, kao što su kategorija, podkategorija, proizvođač ili ključne reči iz imena komponente. Pretraga prema ključnim rečima je najčešće najjednostavniji način, pa ćemo je i mi sada koristiti.

1. **Dugme**: Ukucaćemo reč "button" kako bismo pronašli komponentu koja predstavlja dugme. U središnjem delu prozora prikazani su rezultati pretrage. Selekcijom bilo kog rezultata, prikazuje se izgled te komponente. Dvoklikom na odgovarajuću komponentu, prebacujemo je u beli prozor sa desne strane.

2. **Dioda**: Na sličan način ćemo pronaći i diodu koja emituje svetlost.

3. **Otpornik**: Pronaći ćemo i otpornik.

Pošto smo pronašli sve potrebne komponente, možemo zatvoriti prozor za izbor komponenti iz biblioteke.

#### Instanciranje komponenti na radnoj površini

Instanciranje komponenti započinje se izborom željene komponente iz belog prozora. Zatim, prvim levim klikom na radnoj površini aktivira se mod za instanciranje, gde biramo poziciju na radnoj površini gde želimo da instanciramo komponentu. Drugim levim klikom komponenta se zaista instancira. Na isti način instanciraćemo i preostale komponente.

#### Dodavanje napajanja i uzemljenja

Da bismo zatvorili naše jednostavno strujno kolo, potrebno je dodati napajanje i uzemljenje. Ovo se radi pomoću moda za terminale, koji se nalazi ovde. U njegovom belom prozoru već postoje predefinisane komponente koje se mogu instancirati. Mi ćemo odabrati **Power** za napajanje i **Ground** za uzemljenje.

#### Povezivanje komponenti

Poslednji korak je povezivanje komponenti. Povezivanje možemo izvršiti na dva načina: direktnim povezivanjem ili povezivanjem po imenu. Mi ćemo se prvo poslužiti direktnim povezivanjem.

1. **Preuređivanje komponenti**: Da bismo lakše izvršili povezivanje, malo ćemo preurediti komponente. Selekcija komponenti se vrši levim klikom na njih, a ukoliko želimo da rotiramo komponentu, prvo je selektujemo, a zatim desnim klikom izaberemo opciju za rotaciju.

2. **Direktno povezivanje**: Direktno povezivanje se može izvršiti iz moda za selekciju. Ako se dovoljno približimo komponentama pomoću skrola, videćemo da se prilikom prelaska preko terminala pojavljuje crveni kvadrat. Levim klikom započinjemo povezivanje, a prilaskom drugom terminalu ponovo ćemo videti crveni kvadrat. Novim levim klikom uspešno smo povezali dve komponente.

3. **Povezivanje dugmeta i diode**: Na sličan način možemo povezati dugme sa terminalom diode. Ako priđemo dugmetu i pritisnemo levi klik, možemo izvršiti povezivanje sa malo drugačijom putanjom. Primetićete da se žica pomera tako da uspostavi najkraći put od početne do krajnje tačke. Ako želimo da uvedemo novu tačku, dovoljno je da ponovo pritisnemo levi klik, čime se pojavljuje "X" kod terminala dugmeta, što označava novu početnu tačku za najkraći put. Na ovaj način možemo razvući žicu na proizvoljan način, sve dok ne dođemo do drugog terminala, gde ćemo levim klikom zatvoriti putanju.

## Zaključak

Na ovaj način smo uspešno povezali sve komponente našeg jednostavnog strujnog kola. U narednim koracima možemo nastaviti sa simulacijom i analizom rada kola.


---

### Korišćenje Proteusa za simulaciju mikroprocesorskih kola

U Proteusu, možemo povezivati različite komponente direktno, koristeći najkraće moguće veze. **Levi klik** započinje proces povezivanja, a drugi **levi klik** ga završava. Nakon što su sve komponente povezane, spremni smo za pokretanje simulacije.

Simulacija u Proteusu se pokreće klikom na dugme **Play** (▶). Kada pritisnemo ovo dugme, simulacija počinje. Tokom simulacije, prikazuje se proteklo vreme. Što je kolo jednostavnije i računar na kojem se simulacija izvršava ima više resursa, to će vreme simulacije više odgovarati realnom protoku vremena.

Tokom simulacije, možete koristiti različite karakteristike komponenti koje ste instancirali. Na primer, kod komponente **dugme** (button), možete je pritisnuti tokom simulacije. Kada se dugme pritisne, stvara se kratak spoj između dva terminala. U ovom slučaju, dioda ne svetli jer je otpornost otpornika prevelika. Da bismo to promenili, moramo prvo zaustaviti simulaciju pritiskom na dugme **Stop** (⏹).

Izmena karakteristika komponente moguća je desnim klikom na komponentu i odabirom opcije **Edit Properties**. Različite komponente imaju različite opcije za izmenu. Na primer, za otpornik možemo promeniti otpornost. U ovom slučaju, smanjićemo otpornost sa **10 kilooma** na **100 oma**.

Ako sada ponovo pokrenemo simulaciju i pritisnemo dugme, videćemo da dioda uspešno svetli dok je dugme pritisnuto.

---

### Korišćenje sondi za merenje napona i struje

Ako nas zanima intenzitet napona u određenoj tački strujnog kola ili intenzitet struje koja protiče kroz njega, možemo koristiti odgovarajuće sonde za merenje napona ili struje. Instanciranje sondi vrši se u modu za sonde, koji se nalazi u alatkama. Možemo instancirati sondu za napon i postaviti je na odgovarajuće mesto u kolu, ili sondu za merenje struje i postaviti je na željenu poziciju.

Sondama možemo dodeliti imena desnim klikom na njih i odabirom opcije **Edit Label**. Na primer, možemo im dodeliti imena **Voltage 1** i **Current 1**. Kada ponovo pokrenemo simulaciju, videćemo vrednosti koje ove sonde mere. Pritiskom na dugme, vrednosti će se promeniti.

---

### Povezivanje komponenti pomoću imena (labela)

Sada ćemo instancirati identično strujno kolo, ali ćemo komponente povezati pomoću imena (labela), umesto direktnim povezivanjem. Prvo ćemo instancirati sve tri komponente: dugme, diodu i otpornik. Zatim ćemo ih preurediti na radnoj površini kako bismo olakšali povezivanje.

Nakon toga, izvući ćemo žice iz terminala svih komponenti, dovoljno dugačke da im možemo dodeliti imena. Žicama možemo dodeliti imena pritiskom na njih desnim klikom i odabirom opcije **Place Wire Label**. Na primer, možemo dodeliti ime **Power** jednoj žici. Ako drugoj žici dodelimo isto ime, Proteus će ih smatrati povezanim.

Možemo se uveriti u to desnim klikom na žicu i odabirom opcije koja označava sve povezane elemente na radnoj površini. Na primer, ako dodelimo ime **Power** žici koja je povezana sa napajanjem, videćemo da su svi elementi sa istim imenom povezani.

---

### Simulacija kompleksnijeg kola

Za simulaciju kompleksnijeg kola, možemo otvoriti novu stranicu na radnoj površini. Trenutno se nalazimo na **Stranici 1**, a možemo otvoriti novu čistu stranicu odabirom opcije **New Root Sheet**. Ako želimo da se vratimo na prethodnu stranicu, možemo to uraditi desnim klikom bilo gde na radnoj površini i odabirom **Sheet 1** ili **Sheet 2**.

U ovom primeru, umesto jednostavnog izvora napona, koristićemo generator složenijeg signala. Instanciraćemo tranzistor i otpornik, povezati ih direktno, a otpornik povezati na uzemljenje. Ako se nalazimo na drugoj stranici, možemo koristiti odgovarajuće alate za dalji razvoj kola.

---

## Povezivanje signala i komponenti

Prvo, potrebno je uzeti signale sa prve stranice. Ovo ćemo povezati na uzemljenje, a anodu naše diode ćemo povezati na jedan generator. Generator instanciramo uz pomoć ovog moda za generatore. Možemo generisati različite oblike signala, tako da možemo imati generatore za jednosmernu struju, sinusoidu, impulse i tako dalje. Na primer, sada možemo instancirati generator za sinusoidu i smestiti ga na našu radnu površinu, kao i svaku drugu komponentu.

Našem generatoru možemo dodeliti ime, na primer, "generator za sinusoidu". Takođe, možemo promeniti njegove karakteristike, na primer, amplitudu postaviti na 5 volti, a frekvenciju na 1 Hz, što odgovara periodu od 10 sekundi.

## Kreiranje grafika i postavljanje sondi

U ovom primeru, bavićemo se i kreiranjem grafika analognih vrednosti signala. Za to će nam biti potrebne sonde koje će meriti te vrednosti. Prva sonda neka bude za napon, a druga za struju. Promenićemo imena ovim sondama: prva neka bude **V3**, a druga **I3**.

Ovde možemo videti da dioda svetli, pa ćemo smanjiti otpornost otpornika na 100 oma. Vrednosti koje sonde beleže tokom vremena biće prikazane na grafiku. Za to koristimo mod za grafike, gde možemo birati različite tipove grafika. Mi ćemo se odlučiti za analogni grafik. Njega postavljamo na radnu površinu tako što ga povlačimo na željeno mesto.

Kreiranje grafika vršimo tako što levim klikom povlačimo oblik koji želimo, a zatim puštamo levi klik. Zatim, ponovnim pritiskom na levi klik, instanciramo drugi grafik. Na jednom grafiku ćemo prikazivati napon, a na drugom struju.

Za ove grafike sada treba odrediti vremenski opseg prikazivanja. Na primer, odabrat ćemo period od 0 do 30 sekundi. To postižemo desnim klikom na svaki od grafika i u **Edit Properties** postavljamo početno vreme na 0, a krajnje vreme na 30 sekundi. Isto ćemo uraditi i za drugi grafik.

Na kraju, svakom od ovih grafika dodajemo vrednosti koje se na njemu prikazuju. Desnim klikom na grafik biramo opciju **Add Traces** i odabiremo sondu koja beleži napon (**V3**), a na drugom grafiku sondu koja beleži struju (**I3**).

## Simulacija i analiza rezultata

Da bismo prikazali grafik, neophodno je izvršiti simulaciju. Nakon pokretanja simulacije, možemo videti izgled napona i struje u određenim tačkama. Tokom simulacije, primećujemo da se dioda ne uključuje odmah, već intenzitet svetla polako raste i opada kako se menja napon.

## Instanciranje novih komponenti

Za potrebe ovog primera, instancirati ćemo neke nove komponente. Preći ćemo na prvu stranicu naše radne površine i dodati jednostavna integrisana kola koja sadrže logička kola, kao što su **AND** i **OR**. Da bismo instancirali ova kola, potrebno je izabrati ih iz biblioteke koristeći mod za komponente i opciju **Pick from Library**.

Da bismo pronašli željena integrisana kola, unosićemo oznaku familije kola, na primer, **74LS**, a zatim ćemo navesti tip logičkog kola, na primer, **AND**. Kao rezultat pretrage, videćemo četiri dvoulazna pozitivna **AND** kola unutar jednog integrisanog kola sa oznakom **74LS08**. Dodati ćemo jedno takvo kolo.

Slično, dodati ćemo i integrisano kolo sa **OR** logičkim kolima, na primer, **74LS32**, koje sadrži četiri dvoulazna pozitivna **OR** kola.

## Povezivanje logičkih kola i dioda

Nakon instanciranja, na radnu površinu postavljamo pojedinačna logička kola, a ne cela integrisana kola. Instancirati ćemo jedno **AND** i jedno **OR** logičko kolo. Na njihove izlaze povezujemo diode, jednu za **OR** i jednu za **AND**.

Na ulaze logičkih kola dovodimo napon preko dva dugmeta, **Dugme 1** i **Dugme 2**. Lako možemo postaviti **Dugme 2**, dok za **Dugme 1** izvodimo novu žicu. Ako želimo da izvedemo novu žicu, koristimo mod za spojeve, pravimo spoj na određenom mestu, a zatim iz tog spoja izvlačimo žicu i dajemo joj naziv, na primer, **Dugme 1**.

## Pokretanje simulacije

Ako pokrenemo simulaciju i pritisnemo neko od dugmadi, videćemo da se dioda na **OR** kolu upali, dok za **AND** kolo neophodno je da oba ulaza budu na logičkoj jedinici.


## Prakticni Primer

Za potrebe ovog praktičnog primera, otvorićemo novu stranicu radne površine. Na ovoj stranici ćemo instancirati jedno složeno integrisano kolo, odnosno mikrokontroler koji ćemo koristiti tokom ovog kursa. Instanciranje ćemo izvršiti na isti način kao i za sve ostale komponente koje smo do sada koristili. Preći ćemo u mod za komponente, pretražiti biblioteku i pronaći mikrokontroler koji ćemo koristiti. U ovom slučaju, to je **STM32F103R6**. Dodajemo ga u beli pravougaonik kako bismo ga kasnije mogli instancirati.

Ovaj mikrokontroler ćemo koristiti tokom našeg kursa. Međutim, ako pokrenemo simulaciju ovog mikrokontrolera u ovom trenutku, pojaviće se problem. Hajde da to probamo. Poruku o grešci možemo videti u simulacionom logu. Da bismo pristupili ovom logu, potrebno je kliknuti na dugme za simulacioni log, nakon čega će se otvoriti odgovarajući prozor.

Poruka o grešci ukazuje na to da ne postoji izvor napajanja za mrežu. U pitanju su skriveni pinovi, odnosno pinovi koji nisu izvučeni iz ovog mikrokontrolera, a neophodni su za njegovo funkcionisanje. Naime, u pitanju su napajanje (**Vdda**) i uzemljenje (**Vssa**). Zbog toga ćemo sada instancirati napajanje i uzemljenje za potrebe ovog mikrokontrolera i dodeliti terminalima imena koja mikrokontroler očekuje, u skladu sa skrivenim pinovima koje smo pomenuli.

Ako sada ponovo pokrenemo simulaciju, nećemo dobiti istu grešku kao malopre, ali ćemo se suočiti sa drugom greškom. Hajde da pokrenemo simulaciju i pogledamo simulacioni log. U njemu ćemo videti poruku da fajl koji predstavlja program koji mikrokontroler treba da izvršava nije naveden. Drugim rečima, trenutno nema sadržaja u memoriji mikrokontrolera na osnovu kojeg bi on izvršavao neki program.

Da bismo to popravili, potrebno je desnim klikom na mikrokontroler otvoriti njegove opcije. Sada imamo mnogo više opcija nego što je to bio slučaj sa otpornicima. Na ovom mestu treba navesti koji program mikrokontroler treba da izvršava. Ovaj programski fajl predstavlja sadržaj koji treba smestiti u memoriju mikrokontrolera na odgovarajuće adrese kako bi on mogao da radi nešto korisno.

Za potrebe ove lekcije, već imamo pripremljen takav fajl, pod nazivom **program.x**. Njegov sadržaj je u suštini niz nula i jedinica, odnosno informacija koje treba smestiti u memoriju. Bez daljeg ulaska u detalje ovog programa, smestićemo ga u naš Proteus projekat i definisati da je upravo ovaj fajl onaj koji mikrokontroler treba da izvršava. Dakle, **program.x** je fajl koji želimo da naš mikrokontroler izvršava.

Takođe, definisaćemo da nas u simulacionom modu ne zanima preterana preciznost simulacije, već performanse, odnosno da se simulacija izvršava što brže i efikasnije moguće, što više odgovara realnom vremenu.

Ako sada pokrenemo simulaciju, ovaj program će se početi izvršavati. Videćemo da se na **nultom pinu porta C** ovog mikrokontrolera periodično menja logička vrednost. Da bismo to vizuelno prikazali, možemo na ovaj pin povezati diodu. Kao i do sada, jedan kraj diode ćemo povezati na napajanje, a drugi kraj na mikrokontroler. Kako ne bismo opterećivali strujni kapacitet pinova mikrokontrolera, učinićemo ovu diodu digitalnom. Ovo je dovoljno da dioda svetli kada se na njenom pinu nalazi logička jedinica, dok će biti ugašena kada je na pinu logička nula.

Nakon što smo definisali da je dioda digitalna, ponovo ćemo pokrenuti simulaciju. Videćemo da mikrokontroler, u skladu sa programom koji smo mu dodelili, periodično uključuje i isključuje diodu.

Ovim je završena prva lekcija. Obradili smo sve osnovne funkcionalnosti Proteus simulatora. Vidimo se na sledećem času!

**Završena prva lekcija.**
