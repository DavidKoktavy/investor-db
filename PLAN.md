# Plán: Spolehlivá databáze investorů

> Zadání A · David Koktavý · stav k 11. 10. 2026
> Toto je výchozí plán. Každou odchylku během pilotu zapisuji do [`docs/decisions.md`](docs/decisions.md) i s důvodem.

## 0. Shrnutí

- Do databáze zařadím jen subjekt, u kterého umím doložit **investici do soukromé firmy za posledních 24 měsíců** (URL + datum). Toto pravidlo odfiltruje většinu „náhodných firem“, které v obecných seznamech nesou nálepku investor.
- Každý údaj (typ, sektory, ticket, kapitál…) má **vlastní zdroj**: URL, datum zveřejnění, datum přístupu a krátkou doslovnou citaci. Neznámá hodnota = `null` s důvodem, nikdy odhad.
- Spolehlivost nestojí na jednom modelu. Postup je: agent sbírá fakta, skript kontroluje citace, nezávislý agent je ověřuje, o zařazení rozhoduje kód podle pravidel a na konci kontroluje člověk.
- **Pilot:** VC správci se sídlem v ČR (odhad 30–50 aktivních z 60–90 kandidátů). Měřím přesnost celého záznamu i jednotlivých polí, s 95% intervalem spolehlivosti.
- **Celý svět:** z veřejných zdrojů realisticky ~16–25 tis. ověřitelných investorů. První běh vyjde řádově na 35–50 tis. EUR včetně práce, z toho výpočet 12–23 tis. USD. Obnova stojí ~10 tis. EUR za půl roku.

---

## 1. Cíl a co znamená „spolehlivá“

Přednost má přesnost před úplností. Chybně zařazený subjekt (poradce, banka, realitní fond) podkope důvěru v celou databázi víc než investor, který chybí.

Cílové hodnoty pro pilot (hypotézy, které pilot ověří):

| Metrika | Cíl |
|---|---|
| Přesnost záznamu (jde o aktivního investora deklarovaného typu) | ≥ 95 % |
| Platnost citací (URL funguje, citace na stránce je a údaj podporuje) | ≥ 95 % |
| Přesnost polí typ, sídlo, sektory | ≥ 90 % |
| Přesnost polí ticket a kapitál (tam, kde jsou vyplněná) | ≥ 80 % |

---

## 2. Kdo v databázi bude a kdo ne

### 2.1 Definice

**Investor** = subjekt, který z vlastních nebo svěřených prostředků opakovaně nabývá podíly (equity nebo equity-like nástroje: konvertibilní úvěr, SAFE) v soukromých, nekótovaných firmách a sám o investici rozhoduje.

**Jednotka záznamu = správce / investiční značka** (např. „Credo Ventures“), ne jednotlivý fond. Fondy jsou uvedené pod záznamem jako seznam. Důvod: tým, investiční teze i kontakt patří správci, kdežto jednotlivé fondy se překrývají a rychle stárnou.

### 2.2 Typy

| Typ | Kód | Poznámka |
|---|---|---|
| VC fond / správce | `vc` | včetně akcelerátorů, které pravidelně berou podíl výměnou za kapitál |
| Korporátní VC | `cvc` | jen samostatná investiční jednotka korporace s vlastní tezí |
| Private equity | `pe` | buyout, growth, menšinové podíly |
| Family office | `family_office` | jen pokud investuje přímo do firem, ne pouze do fondů |
| Angel investor | `angel` | fyzická osoba s veřejným investorským profilem |
| Soukromý investiční holding | `private_holding` | vehikulum jednotlivce nebo rodiny, které investuje do firem, ale neprezentuje se jako FO |

### 2.3 Podmínky zařazení (musí platit všechny)

- **K1 Existence.** Subjekt je identifikovatelný: právnická osoba dohledatelná v rejstříku (IČO, LEI, CRD…), nebo fyzická osoba s veřejným investorským profilem.
- **K2 Aktivita.** Existuje ≥ 1 doložená investice do soukromé firmy s datem oznámení v posledních 24 měsících před datem sběru, nebo první či konečný close nového fondu v posledních 12 měsících. Důkaz = URL + datum.
- **K3 Rozhodování.** Investuje vlastní nebo svěřený kapitál a o investici rozhoduje (není zprostředkovatel).
- **K4 Typ.** Odpovídá jednomu z typů v 2.2. V pilotu jen `vc` a `cvc` s investičním týmem v ČR.

**Proč 24 měsíců.** Menší CEE fondy dělají jen jednotky investic ročně a investiční období fondu trvá několik let. Kratší okno by vyřadilo pomalé, ale živé fondy, delší by propustilo „zombie“ fondy. Subjekt s poslední investicí před 24–36 měsíci dostane stav `dormant` a do hlavní databáze nepatří.

**Sídlo.** Rozhoduje, kde sídlí investiční tým, ne kde je registrované vehikulum (český tým s lucemburským fondem = CZ).

### 2.4 Kdo v databázi nebude

| Kategorie | Důvod | Kód vyřazení |
|---|---|---|
| Poradci, M&A butiky, advokáti, auditoři | neinvestují | `advisor_or_intermediary` |
| Banky, leasing, venture debt, direct lending | poskytují dluh, ne kapitál za podíl | `debt_only` |
| Fondy fondů a LP bez přímých investic (vč. FO, které investují jen do fondů) | neinvestují přímo do firem | `fund_of_funds_or_lp_only` |
| Fondy kótovaných akcií, hedge fondy, podílové fondy | investují na veřejných trzích | `public_markets_only` |
| Realitní fondy a developeři | investují do nemovitostí, ne do firem | `real_estate_only` |
| Crowdfundingové platformy | zprostředkují cizí kapitál | `crowdfunding_platform` |
| Granty, dotační programy, akcelerátory bez podílu | nenabývají podíl | `grant_or_program_only` |
| Korporace s jednorázovou strategickou akvizicí | kupec, ne investor | `out_of_scope_type` |
| Žádná investice za 24 měsíců | neaktivní | `no_recent_investment` |
| Zaniklé nebo nedohledatelné | | `not_found_or_defunct` |
| Mimo segment pilotu (cizí sídlo, PE apod.) | jen pro pilot | `out_of_scope_geography`, `out_of_scope_type` |

**Hraniční případy** (rozhoduje kód podle pravidel, já výsledek kontroluji):

- **Smíšené portfolio** (např. growth equity + venture debt): zařadit, pokud v okně existuje alespoň jedna doložená equity investice. Pole `stages` obsahuje jen equity fáze.
- **Členství v asociaci neurčuje typ.** Mezi řádnými členy CVCA je fond zaměřený hlavně na seniorní dluh a mezaninové financování (CVI). Mezi přidruženými členy jsou naopak subjekty, které investují vlastní kapitál (Pale Fire Capital, JSK Investments), ale i vlastník průmyslových parků (Accolade) [1]. Seznam asociace proto slouží jen jako zdroj kandidátů; o zařazení rozhoduje důkaz.
- **Korporátní fond** (např. Inven Capital ze skupiny ČEZ [1]): typ `cvc`, zařadit.
- **Zápis v registru není důkaz aktivity.** ČNB správce podle § 15 ZISIF jen eviduje a správnost jejich údajů neověřuje [2]. SEC v srpnu 2026 žalovala 38 subjektů, které podaly nepravdivé formuláře ADV jako exempt reporting advisers, aby budily dojem legitimity [8]. Registr tedy dokládá existenci, ne to, že subjekt investuje.

---

## 3. Datový model

Formální schéma je v [`schema/investor.schema.json`](schema/investor.schema.json), ukázkový (smyšlený) záznam v [`schema/example.record.json`](schema/example.record.json). Každé pole má tvar `{value, source}`, nebo `{value: null, null_reason}`.

| Pole | Obsah | Pravidlo |
|---|---|---|
| `name`, `website` | identifikace | |
| `hq_country` | sídlo investičního týmu | ISO 3166-1 alfa-2 |
| `legal_entities[]` | právnické osoby a registrační čísla | ideálně z rejstříku (úroveň 1) |
| `type` | typ podle 2.2 | o zařazení rozhoduje kód |
| `sectors` | do čeho investuje | pevná taxonomie (20 kategorií) + původní text |
| `stages` | fáze (pre-seed … buyout) | jen equity fáze |
| `ticket` | obvyklá výše první investice, min–max | v původní měně; přepočet na EUR až v kódu (referenční kurz ECB k datu) |
| `capital` | celkový investiční kapitál | s `basis` (`reported_aum` / `sum_of_fund_sizes` / `latest_fund_size`) a `as_of` |
| `funds[]` | jednotlivé fondy, ročník, velikost | volitelné |
| `evidence_of_activity[]` | investice: firma, datum oznámení, role (lead / účast) | ≥ 1 v okně 24 měsíců |
| `status`, `exclusion_reason` | `active` / `dormant` / `excluded` | nastavuje výhradně kód |

**Zdroj (`source`)** = URL, úroveň zdroje (1–3), vydavatel, datum zveřejnění, datum přístupu, doslovná citace (≤ 25 slov) a příznak `self_reported`.

**„Celkový investiční kapitál“** chápu jako upsaný kapitál všech fondů správce, které ještě investují nebo drží portfolio. Kapitál nikdy nezaměňuji s velikostí posledního fondu, proto pole `basis`. Pokud se kapitál skládá z několika fondů, součet počítá kód z jednotlivě doložených velikostí; model nic nesčítá.

---

## 4. Zdroje

### 4.1 Úrovně spolehlivosti

| Úroveň | Typ | Příklady | Co dokládá |
|---|---|---|---|
| 1 | Regulátor / rejstřík | ČNB (JERRS, seznam podle § 15 ZISIF), obchodní rejstřík a sbírka listin (výroční zprávy), ESMA (registry AIFM a EuVECA) [14], SEC IAPD / Form ADV a měsíční soubory ERA [7], EDGAR Form D, FCA, Companies House | existence, právní forma, někdy objem majetku |
| 2 | Primární publikace | web subjektu (portfolio, teze, tým), tisková zpráva fondu nebo portfoliové firmy, zveřejnění LP (EIF, Národní rozvojová banka) | aktivita, ticket, sektory, velikost fondu |
| 3 | Nezávislé sekundární | CzechCrunch, Forbes, HN, E15, Lupa, profily asociací (CVCA, Invest Europe) | potvrzení aktivity, kontext |

Pravidla pro jednotlivá pole:

- **Aktivita:** ≥ 1 zdroj úrovně 2 nebo 3 s datem. Vysoká jistota = dva nezávislé zdroje (např. fond + portfoliová firma nebo média).
- **Kapitál:** přednost má úroveň 1 před 2 a 3, vždy s datem platnosti. Profily členů CVCA nesou datum publikace z ledna 2020 a objem fondů uvádějí bez data platnosti [1]. Používám je jako zdroj kandidátů, ne jako aktuální hodnotu.
- **Ticket:** téměř vždy ho uvádí jen investor sám (úroveň 2), proto má příznak `self_reported`. Kontroluji ho proti velikosti doložených kol a velikosti fondu.

### 4.2 Co nepoužívám

- Placené databáze (PitchBook, Preqin, placený Crunchbase / Dealroom). Zadání připouští jen veřejná data.
- Scraping LinkedInu, protože odporuje podmínkám služby.
- Otevřené stránky agregátorů beru jen jako tip na kandidáta, nikdy jako důkaz.
- Respektuji robots.txt. Snímky stránek ukládám jen lokálně (`data/raw/`, mimo git); v repozitáři je URL, datum a krátká citace.

### 4.3 Andělé a GDPR

Andělé jsou fyzické osoby. Do databáze patří jen ti, kdo se sami veřejně prezentují jako investoři (profil v síti andělů, vlastní web, rozhovor). Právním základem je oprávněný zájem (čl. 6 odst. 1 písm. f) GDPR) s testem proporcionality. Ukládám jen nezbytné údaje (jméno, profesní profil, investiční zaměření), žádné soukromé kontakty. Při použití databáze k oslovení platí informační povinnost podle čl. 14 a právo vznést námitku. Pilot anděly nezahrnuje.

---

## 5. Jak ověřím pravost a správné zařazení

### 5.1 Postup

```
zdroje kandidátů ──► candidate-scout ──► data/candidates/cz_vc.csv
                                              │
                                              ▼
                              investor-extractor (1 agent na kandidáta)
                                              │  JSON, u každého údaje zdroj + citace
                                              ▼
                 validate.py (schéma) + check_quotes.py (je citace opravdu na stránce?)
                                              │
                                              ▼
              evidence-verifier (nový kontext, jiný model, bez vyhledávání)
                                              │  verdikt ke každému údaji
                                              ▼
                 decide.py (pravidla K1–K4, nepodložené údaje → null)
                                              │
                                              ▼
              ruční kontrola (100 % pilotu, bez znalosti verdiktů ověřovatele)
```

### 5.2 Principy

1. **O zařazení rozhoduje kód, ne model.** Agent jen sbírá fakta s citacemi. Zařazení (K1–K4, okno 24 měsíců, kódy vyřazení) počítá `decide.py`, takže je opakovatelné a testovatelné.
2. **Citace kontroluje skript.** `check_quotes.py` stáhne stránku a citaci s textem porovná (fuzzy shoda). Důvod: nástroj WebFetch v Claude Code nevrací surovou stránku, ale výstup malého modelu, který může text přeformulovat. „Doslovná“ citace od agenta proto není automaticky doslovná.
3. **Ověřovatel je nezávislý.** Běží v novém kontextu na silnějším modelu, nevidí úvahy extraktoru, jen tvrzení a URL. Nesmí hledat nové zdroje ani opravovat hodnoty, pouze posoudí, zda zdroj tvrzení podporuje. Model, který kontroluje vlastní výstup, má sklon ho potvrdit.
4. **Nepodložený údaj se vynuluje, neopravuje.** Záznam bez podloženého důkazu aktivity vypadne.
5. **Na konci kontroluje člověk.** V pilotu projdu 100 % zařazených záznamů i všechny vyřazené kandidáty. Při škálování stratifikovaný vzorek a vše, co pipeline označí.

### 5.3 Očekávané chyby a jak je zachytím

| Chyba | Kontrola |
|---|---|
| Vymyšlený ticket nebo kapitál | citace musí obsahovat číslo; `check_quotes.py` + ověřovatel |
| Záměna kapitálu a velikosti posledního fondu | pole `basis`, ověřovatel |
| Subjekt je v článku poradce, banka nebo kupec, ne investor | ověřovatel kontroluje roli subjektu |
| Datum článku ≠ datum investice (zpětný přehled) | ověřovatel kontroluje datum oznámení |
| Jmenovec (stejný název, jiná firma) | doména + IČO, ověřovatel |
| Měna a řád (CZK vs EUR, mil. vs mld.) | čísla v jednotkách, přepočet jen v kódu, ověřovatel |
| Zastaralý web (tým odešel, fond už neinvestuje) | okno 24 měsíců, `as_of` |
| Špatný typ (akcelerátor vs VC, poradce vs investor) | pravidla + ruční kontrola |

---

## 6. Odhad rozsahu a spolehlivosti

### 6.1 Proč nestačí převzít „nálepku“

Firemní index DiscoLike vede pod štítkem „Private Equity & VC“ přes 215 tis. firem, z toho 1 282 v Česku [13]. V Česku přitom v roce 2025 proběhlo zhruba sto investic rizikového kapitálu [3] a CVCA má 27 řádných členů, z nichž zhruba 8 jsou VC [1]. Většinu „PE & VC“ firem tvoří SPV, holdingy, poradci a realitní vehikula. Proto je doložená aktivita podmínkou zařazení.

### 6.2 Celý svět

| Segment | Odhad aktivního univerza | Z čeho odhad vychází | Doložitelné z veřejných zdrojů | Odhad záznamů | Očekávaná spolehlivost |
|---|---|---|---|---|---|
| VC (vč. CVC a akcelerátorů s podílem) | 7–10 tis. | NVCA: 2 984 amerických VC firem, které za posledních 8 ročníků uzavřely fond; USA tvořily v roce 2025 39 % počtu VC dealů ve světě [5]. Prostý přepočet dává ~7,7 tis., mimo USA je víc menších firem s menším počtem dealů. SEC eviduje přes 2 tis. poradců s výjimkou pro VC fondy [6]. | 70–85 % | 5–7 tis. | záznam ≥ 95 %; ticket vyplněn u 50–70 %, kapitál u 50–70 % |
| PE | 8–12 tis. (nízká jistota) | Preqin v roce 2009 napočítal 4 270 PE firem s vlastními fondy, ~6 tis. včetně ostatních [12]; trh od té doby výrazně vyrostl. | 60–75 % | 5–8 tis. | záznam ≥ 95 %; ticket 40–60 %, kapitál 50–70 % (USA lépe díky Form ADV) |
| Family office | ~9 tis. SFO celkem, přímo do firem investuje menšina | Deloitte: 8 030 single family offices v roce 2024, výhled 9 030 pro 2025, z toho Evropa 2 020 [9] | 15–30 % | 1,5–2,5 tis. | záznam 85–90 %; ticket 10–30 %, kapitál 10–20 % |
| Angel investoři | desítky až stovky tisíc | EBAN: ~47,6 tis. aktivních andělů v sítích v Evropě (2024) [10], 358 sítí a federací v 37 zemích [11] | 3–10 % (jen s veřejným profilem) | 3–6 tis. | záznam 85–90 %; ticket 20–40 %, kapitál n/a |
| Soukromé investiční holdingy | spolehlivý odhad neexistuje | dohledatelné jen přes konkrétní dealy v médiích | nízké | 1–2 tis. | záznam ~90 %; nízká vyplněnost |
| **Celkem** | | | | **~16–25 tis.** | |

Z veřejných zdrojů se **nedá** spolehlivě získat: family office bez webu, andělé bez veřejného profilu, přesný kapitál menších fondů a u velké části PE i obvyklý ticket. U Číny, Japonska a Blízkého východu počítám s nižší vyplněností kvůli jazyku a odlišným rejstříkům.

Všechna čísla v tabulce jsou hypotézy. Pilot změří poměr kandidátů a zařazených záznamů a vyplněnost polí pro české VC; podle toho odhad upravím (README, sekce Náklady).

### 6.3 Česko (pilot)

- **Univerzum:** 30–50 aktivních VC správců s týmem v ČR; seznam kandidátů 60–90.
- **Z čeho odhad vychází:** ~8 VC mezi řádnými členy CVCA [1]; EIF v ČR investoval do 17 VC a PE fondů [4]; ročně ~100 VC investic [3], obvykle s 1–3 investory, z nichž část jsou zahraniční fondy a andělé.
- **Zdroje kandidátů:** CVCA (řádní i přidružení členové), ČNB JERRS (investiční společnosti, fondy kvalifikovaných investorů, seznam podle § 15), portfolio EIF a Národní rozvojové banky / Národního inovačního fondu, zprávy o investicích za posledních 24 měsíců (CzechCrunch, Forbes, Lupa, HN), roční přehledy trhu.

---

## 7. Pilot: VC v ČR

### 7.1 Postup

1. **Kandidáti:** `candidate-scout` projde postupně každý zdroj → `data/candidates/cz_vc.csv`, deduplikace podle domény.
2. **Extrakce:** `investor-extractor` pro každého kandidáta → `data/records/staging/<id>.json`.
3. **Kontrola struktury a citací:** `validate.py` + `check_quotes.py` → `data/quote_checks/<id>.json`.
4. **Ověření:** `evidence-verifier` → `data/verification/<id>.json`.
5. **Rozhodnutí:** `decide.py` → `data/records/cz_vc.jsonl` (zařazení) a `data/candidates/cz_vc_decisions.csv` (vyřazení s kódem).
6. **Ruční kontrola:** `data/manual_review/cz_vc.csv`.
7. **Měření:** `metrics.py` → `results/accuracy.md`.

### 7.2 Ruční kontrola (ground truth)

U každého zařazeného záznamu otevřu každou citovanou URL a ověřím citaci i údaj. Nezávisle dohledám poslední investici (nejvýš 3 minuty). Každé pole ohodnotím jako `correct` / `partially_correct` / `incorrect` / `unverifiable`. Kontroluji dřív, než uvidím verdikty ověřovatele, abych se jimi nenechal ovlivnit. Projdu i všechny vyřazené kandidáty, protože chybné vyřazení znamená ztracenou úplnost.

### 7.3 Metriky

| Metrika | Výpočet |
|---|---|
| Přesnost záznamu | správně zařazené / zařazené, s 95% Wilsonovým intervalem |
| Přesnost typu | správný typ / zařazené |
| Chybné vyřazení | omylem vyřazené / vyřazené |
| Úplnost vůči referenci | zařazené / aktivní VC správci s týmem v ČR v referenčním seznamu (CVCA + EIF/NRB + můj ruční seznam) |
| Vyplněnost pole | vyplněné / všechny záznamy, pro každé pole |
| Přesnost pole | správné / vyplněné, pro každé pole |
| Platnost citací | nalezené a podporující citace / všechny citace |
| Kvalita ověřovatele | shoda jeho verdiktů s ruční kontrolou (matice záměn) |
| Náklad | tokeny, počet vyhledávání, USD a minuty ruční práce na záznam |

**Malý vzorek = široký interval.** Výsledek 38/40 správně odpovídá 95% intervalu 83,5–98,6 %, výsledek 40/40 intervalu 91,2–100 %. Pilot tedy ukáže, zda pipeline funguje a kde chybuje, ne přesné procento. V README to uvádím otevřeně.

---

## 8. Náklady na rozšíření na celý svět

**Ceny Claude API (říjen 2026)** [15]: Sonnet 5.5 stojí 2 / 10 USD za milion vstupních / výstupních tokenů, Opus 5.5 4 / 20 USD, Haiku 5.5 0,10 / 0,50 USD. Webové vyhledávání stojí 10 USD za 1 000 dotazů, stažení stránky jen tokeny. Batch API dává slevu 50 % na tokeny.

**Vzorec:**
`náklad = N_surových × c_triáž + N_kandidátů × c_extrakce + N_záznamů × c_ověření + N_QA × t_QA × sazba + vývoj`

| Položka | Předpoklad | Náklad |
|---|---|---|
| Triáž surových kandidátů (Haiku 5.5) | 200 tis. kandidátů z registrů a seznamů × ~5 tis. tokenů | ~0,1 tis. USD |
| Extrakce (Sonnet 5.5) | 40 tis. kandidátů × (120 tis. vstupních + 3 tis. výstupních tokenů + 3 vyhledávání) ≈ 0,30 USD | ~12 tis. USD |
| Ověření (Opus 5.5) | 20 tis. záznamů × (60 tis. vstupních + 2 tis. výstupních tokenů) ≈ 0,28 USD | ~5,6 tis. USD |
| Rezerva na opakování a chyby | +30 % | ~5,3 tis. USD |
| **Výpočet celkem** | s Batch API přibližně poloviční | **12–23 tis. USD** |
| Ruční QA | 1 500 náhodných záznamů × 8 min + 2 000 označených × 5 min ≈ 370 h × 40 EUR/h | ~15 tis. EUR |
| Vývoj | konektory na registry (SEC, ESMA, národní), fronta, deduplikace, monitoring: 4–6 týdnů × 40 h × 50 EUR/h | 8–12 tis. EUR |
| **První běh celkem** | | **řádově 35–50 tis. EUR** |
| Obnova každých 6 měsíců | nové ověření aktivity (~40 % výpočtu) + QA vzorku 600 záznamů | ~5–9 tis. USD + ~3 tis. EUR |

Na jeden zařazený záznam to vychází na ~0,6–1,2 USD za výpočet a ~0,75 EUR za ruční kontrolu.

**Největší nejistoty**, které pilot zkalibruje: počet tokenů na kandidáta, poměr kandidátů a zařazených záznamů (globálně předpokládám 2 : 1) a minuty ruční kontroly na záznam. Po pilotu dosadím naměřené hodnoty do vzorce a výsledek uvedu v README.

**Kde ušetřit:** hromadná data z registrů (SEC, ESMA) jsou zdarma a strojově čitelná, takže triáž může být z velké části bez modelu. Jednodušší pole může extrahovat Haiku, pokud to pilot ukáže jako dost přesné. Prompt caching a Batch API snižují cenu tokenů.

---

## 9. Omezení a rizika

- **Andělé a family office:** veřejně je dohledatelná jen menšina, databáze pro ně bude ze své podstaty neúplná.
- **Jazyk a region:** v Asii a na Blízkém východě jsou místní zdroje a jiné rejstříky; počítám s nižší vyplněností.
- **Ticket** je téměř vždy jen to, co investor uvádí sám; kapitál menších fondů často chybí úplně.
- **Stárnutí dat:** weby se nemění, ani když fond přestane investovat. Proto okno 24 měsíců a pravidelná obnova.
- **Rozsah pilotu:** nezahrnuje PE, family office ani anděly. Plán pro ně stojí na stejných pravidlech, ale bez změřené přesnosti.

---

## Zdroje

1. CVCA – Membership (seznam řádných a přidružených členů s profily): https://cvca.cz/en/membership/
2. ČNB – Role ČNB u správců podle § 15 ZISIF: https://www.cnb.cz/cs/dohled-financni-trh/vykon-dohledu/upozorneni-pro-verejnost/Role-CNB-u-spravcu-podle-15-zakona-o-investicnich-spolecnostech-a-investicnich-fondech ; ČNB – Investování do alternativních fondů: https://www.cnb.cz/cs/o_cnb/vlog-cnb/Investovani-do-alternativnich-fondu
3. Forbes CZ – Investoři jsou vybíravější (počet VC investic v ČR v roce 2025): https://forbes.cz/investori-jsou-vybiravejsi-pocet-investic-do-startupu-ubyva-jejich-prumerna-vyse-vsak-roste/
4. BusinessInfo.cz – První VC fond z Národního plánu obnovy bude spravovat Tensor Ventures (investice EIF v ČR): https://www.businessinfo.cz/clanky/prvni-investicni-vc-fond-z-narodniho-planu-obnovy-cr-bude-spravovat-tensor-ventures/
5. NVCA – 2026 Yearbook: https://nvca.org/wp-content/uploads/2026/04/2026-YB-Public-PDF.pdf
6. SEC – Investment Adviser Statistics (data k prosinci 2023): https://www.sec.gov/files/im-investment-adviser-statistics-20240515.pdf
7. SEC – Form ADV data a měsíční soubory exempt reporting advisers: https://www.sec.gov/help/foiadocsinvafoiahtm.html
8. SEC – Litigation Release No. 26622 (27. 8. 2026): https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26622
9. Deloitte Private – Defining the Family Office Landscape 2024: https://www.deloitte.com/global/en/services/deloitte-private/about/defining-the-family-office-landscape.html
10. EBAN – Statistics Compendium 2024: https://www.eban.org/wp-content/uploads/2025/12/Stats-Compendium-2024.pdf
11. EBAN – publikace (Business Angel Networks and Angel Federations in Europe 2023): https://www.eban.org/?p=40706
12. WealthBriefing – Preqin: Private Equity Funds Expand In Number (2009): https://www.wealthbriefing.com/html/printarticle.php?id=26481
13. DiscoLike – Private Equity & VC company stats: https://discolike.com/company-stats/private-equity-vc/
14. ESMA – Databases and Registers (AIFM, EuVECA): https://www.esma.europa.eu/databases-and-registers
15. Anthropic – Claude API Pricing: https://platform.claude.com/docs/en/about-claude/pricing
