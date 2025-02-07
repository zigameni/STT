# Paralelni Računarski Sistemi i Konkurentno Programiranje

Na vašoj kartici (grafičkoj ili procesorskoj) postoji posebna sintaksa koja vam omogućava da kažete: "Izvršavaj ovaj deo koda paralelno." To se postiže korišćenjem direktiva koje specificiraju kako se taj paralelni deo koda treba izvršiti. 

## Šta je Paralelni Računarski Sistem?

Paralelni računarski sistem je svaki računarski sistem koji je u stanju da istovremeno izvršava dva ili više delova jednog ili više programa. Ovo nije isto što i **Instruction Level Parallelism (ILP)**, gde se pojedinačne instrukcije izvršavaju paralelno unutar jednog procesa. Paralelni program mora eksplicitno da označi delove koda koji treba da se izvršavaju paralelno.

Hardver nam pruža određene mogućnosti za paralelno izvršavanje, ali mi moramo znati kako to izvršavanje funkcioniše. U ovom kontekstu, postoji nekoliko ključnih termina, kako na srpskom tako i na engleskom jeziku:

- **Tok izvršavanja** (Execution Flow)
- **Programski tok** (Program Flow)
- **Tok instrukcija** (Instruction Flow)
- **Nit kontrole** (Thread of Control)

Ovi termini se u suštini odnose na istu stvar: skup naredbi koje se izvršavaju u određenom sekvencijalnom redosledu. Dakle, imamo svoj **execution flow** – način na koji se naša nit (thread) izvršava i obavlja određeni posao. 

Možemo imati jednu nit ili više programa koji se izvršavaju paralelno. Međutim, šta tačno znači "istovremeno"? Možete pokrenuti konkurentnu aplikaciju čak i ako nemate multiprocesorski sistem. Ovo je nešto što ste već radili na predmetu **Operativni Sistemi**. Koristili ste samo jedno jezgro procesora, a ipak ste uspeli da pokrenete više niti ili više programa "istovremeno". 

### Konkurentnost vs. Paralelizam

Važno je razumeti razliku između **konkurentnosti** i **paralelizma**:
- **Konkurentnost** se odnosi na sposobnost sistema da upravlja više zadataka u isto vreme, čak i ako se oni ne izvršavaju istovremeno (npr. na jednom jezgru).
- **Paralelizam** podrazumeva stvarno istovremeno izvršavanje više zadataka, što zahteva više jezgara ili procesora.

Dakle, konkurentnost ne zahteva hardversku podršku za paralelizam, ali paralelizam je nemoguć bez odgovarajućeg hardvera.

