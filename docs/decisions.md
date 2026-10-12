# Rozhodnutí

Každé rozhodnutí v bodě, který zadání nechává otevřený. Formát: datum · rozhodnutí · zvažované alternativy · proč.

## D-001 · 2026-10-11 · Jednotka záznamu je správce, ne fond
- Alternativy: jeden záznam na každý fond.
- Proč: tým, teze a kontakt patří správci; fondy se překrývají a rychle stárnou. Fondy jsou pod záznamem jako seznam.

## D-002 · 2026-10-11 · Aktivní = doložená investice za posledních 24 měsíců
- Alternativy: 12 měsíců (vyřadí pomalé CEE fondy), 36 měsíců (propustí neaktivní fondy).
- Proč: viz PLAN §2.3. 24–36 měsíců = `dormant`, mimo hlavní databázi. Nový fond s closem do 12 měsíců se počítá jako aktivita.

## D-003 · 2026-10-11 · Sídlo = kde sedí investiční tým
- Alternativy: sídlo registrovaného vehikula.
- Proč: český tým s lucemburským fondem je pro uživatele český investor.

## D-004 · 2026-10-11 · „Celkový investiční kapitál“ s uvedeným základem
- Alternativy: jedno číslo bez upřesnění.
- Proč: zdroje míchají AUM, velikost posledního fondu a cílovou velikost. Pole `basis` to rozlišuje; součet fondů počítá kód, ne model.

## D-005 · 2026-10-11 · Přesnost před úplností
- Proč: chybně zařazený subjekt podkope důvěru v celou databázi víc než chybějící investor. Nepodložený údaj se vynuluje, neopravuje.

## D-006 · 2026-10-11 · Pilot jen VC + CVC s týmem v ČR, bez andělů
- Proč: zadání navrhuje VC v jedné zemi; andělé jsou fyzické osoby (GDPR, PLAN §4.3) a vyžadují jiný postup.

## D-007 · 2026-10-11 · Datum sběru `AS_OF` = 2026-10-11, pevné pro celý pilot
- Alternativy: datum přístupu u každého záznamu zvlášť; datum odevzdání (16. 10. 2026).
- Proč: všechna okna (24 / 36 / 12 měsíců) se počítají od jednoho data, takže rozhodnutí jsou opakovatelná a mezi záznamy srovnatelná. Okno K2 tedy začíná 2024-10-11, `dormant` sahá do 2023-10-11, nový fond se počítá od 2025-10-11. Hodnota je v `src/config.py`.

## D-008 · 2026-10-11 · Tři scouti paralelně, každý do vlastního souboru, pak deterministické sloučení
- Alternativy: jeden scout postupně přes všechny zdroje do jednoho CSV (pomalé); paralelní zápis do jednoho souboru (kolize).
- Proč: zdroje kandidátů jsou nezávislé (CVCA, zprávy o investicích, veřejné programy), takže běží paralelně. Sloučení dělá kód (`src/merge_candidates.py`): shoda domény, ID nebo normalizovaného názvu plus ručně vedený seznam aliasů s důvodem (`data/candidates/aliases.csv`). Výsledek: 300 řádků → 225 kandidátů.

## D-009 · 2026-10-11 · Triáž před plnou extrakcí
- Alternativy: plná extrakce všech 225 kandidátů (desítky hodin agentů, většina skončí jako zahraniční nebo jiný typ).
- Proč: 82 kandidátů má podle scoutů zahraniční sídlo a desítky jsou zjevně PE, holdingy nebo kluby andělů. Levná triáž (model Haiku, jeden zdroj na kandidáta) odpovídá kroku „triáž“ v nákladovém modelu (PLAN §8). Plnou extrakci dostanou jen kandidáti, kteří podle triáže mohou být VC/CVC s týmem v ČR. Rozhodnutí z triáže dělá kód a jsou označená `decided_by=triage`; jejich chybovost měřím na vzorku v ruční kontrole.

## D-010 · 2026-10-11 · Agenti běží v Claude Code na mém počítači, ne v cloudovém pracovním prostoru
- Alternativy: pokračovat v cloudu po dávkách (každé kolo konverzace má jen 200 vyhledávání pro všechny agenty dohromady a každé stažení stránky mimo výsledky vyhledávání musím ručně schválit; skript na kontrolu citací tam nemá přístup na web).
- Proč: na mém počítači má Claude Code přístup na web, oprávnění pro web a příkazy pipeline jsou nastavená jednou v `.claude/settings.json` a export konverzace (`/export`) je přesně to, co zadání žádá. Postup je v `CLAUDE.md` (Pilot runbook), každý krok jde přerušit a obnovit.

## D-011 · 2026-10-11 · Rozšíření schématu o `exclusion_signals`
- Alternativy: nechat extraktor nastavit typ `null` u poradců, bank apod.
- Proč: kód potřebuje vědět, *proč* subjekt nepatří do databáze (jen dluh, poradce, platforma…), a ten důvod musí mít zdroj jako každý jiný údaj. Agent fakt zapíše, kód rozhodne; smíšené portfolio (dluh + doložená equity investice) zůstává zařazené.

## D-012 · 2026-10-11 · Rozsah ruční kontroly
- Alternativy: 100 % všech kandidátů (PLAN §7.2) — u 225 kandidátů by to byly jednotky hodin jen na vyřazené zahraniční fondy.
- Proč: kontroluji všechny zařazené záznamy (pokud jich je víc než 40, náhodný vzorek 40), všechna vyřazení, o kterých rozhodla pipeline, a náhodný vzorek 15 vyřazení z triáže (seed 42). Odchylka od plánu, protože triáž v plánu nebyla.

## D-013 · 2026-10-11 · Ověřovatel na modelu Opus, extraktor na Sonnetu, triáž na Haiku
- Proč: ověřovatel má být nezávislý a přísnější než extraktor; triáž je levný první průchod jako v nákladovém modelu (PLAN §8). Pokud by Opus narazil na limit předplatného, ověřovatel poběží na Sonnetu a zapíšu to sem.

## D-014 · 2026-10-12 · Pravidlo pro opakování triáže: neznámé sídlo u víc než třetiny dávky
- Alternativy: počítat řádky s jakýmkoli `unknown` (sídlo nebo typ); počítat jen typ.
- Proč: runbook říká „víc než třetina dávky je `unknown`“, ale neříká, které pole. Beru `hq_country`, protože právě sídlo vyřazuje nejvíc kandidátů levně (zahraniční fondy). Opakují se tedy dávky s > 8/25 neznámými sídly (01, 04, 05, 07), každá jen jednou. Platí výstup opakovaného běhu, i když je horší (u batch 01 18/25 místo 14/25). První výstupy jsou v `data/candidates/triage/rerun_first/`. Kandidát s neznámým sídlem nebo typem se nevyřazuje, jde do fronty extrakce.

## D-015 · 2026-10-12 · Triáž smí vyřadit podle typu jen se silným důkazem
- Alternativy: vyřadit podle typu vždy (původní pravidlo); nevyřazovat podle typu vůbec (dražší extrakce).
- Proč: po triáži by ~30 kandidátů s týmem v ČR vypadlo jen podle typu od Haiku, často ze snippetu nebo se střední či nízkou jistotou. Mezi nimi jsou subjekty, které do segmentu patřit mohou (Springtide Ventures je VC fond skupiny KKCG, ale triáž ho označila `private_holding`; dále Rockaway Capital, Pale Fire Capital, QQ Capital, TCF Capital). Chybné vyřazení českého kandidáta je přesně ztráta úplnosti, kterou pilot měří. Nové pravidlo v `decide.triage_decision`: vyřazení podle typu jen při `evidence_kind=page` a `confidence=high`, jinak jde kandidát do extrakce. Vyřazení podle zahraničního sídla zůstává beze změny (sídlo se určuje snáz a cizích fondů je ve frontě nejvíc).

## D-016 · 2026-10-12 · Fronta extrakce: 158 kandidátů, zpracováno 70 s nejsilnější nápovědou českého VC
- Alternativy: extrahovat všech 158 (zhruba dvojnásobný čas a tokeny, většina zbytku jsou zahraniční fondy nebo PE); vybrat ručně.
- Proč: runbook (R3) omezuje pilot na 70. Pořadí počítá kód (`src/select_queue.py` → `data/candidates/extract_selected.csv`): skóre = sídlo z triáže (CZ 2, neznámé 1, cizí 0) + typ z triáže (vc/cvc/akcelerátor 2, neznámý/holding/FO 1, jiný 0); při shodě rozhoduje sídlo, pak tip scouta (`hq_guess` CZ > prázdný > cizí), nakonec abecedně. Hranice vyšla uvnitř skupiny 3/1/0 (neznámé sídlo, typ VC, bez tipu scouta), posledních 7 míst v ní je tedy dáno abecedou.
- Nezpracováno (88, v `cz_vc_decisions.csv` zůstanou `pending` s příznakem): abris-capital, accel, accolade, ai-startup-incubator, air-ventures, airbridge, akcelerator-vsem, alfa8, angelinvest, arctern-ventures, arieli-capital, arx-equity-partners, bakala-capital, battery-ventures, bohemia-venture-capital, bolt-accelerator, bond-ventures, brightcap-ventures, crescendo-ventures, czech-business-angels-association, czechinvest, decibel, decibel-vc, electron-capital-partners, esa-bic-czech-republic, european-investment-fund, evolving-europe, experian, fivesquare, ftmo, gain-ventures, garage-angels, genesis-capital, goldman-sachs-alternatives, google-ventures, hartenberg, headline, integral-capital-group, investown, ipm, itaca-business-incubator, ivbf, j-t-arch, jafam-holding, jaro-capital, jet-investment, jinej-fond, keiretsu-forum-prague, kendaxa-group, longevity-fellows, lumus-investment-collective, mam-private-equity, mid-europa-partners, narodni-rozvojova-investicni, nato-diana, new-vision-3, northzone, np-investments, orizon-systems, pale-fire-capital, partech, plug-and-play, point-nine, proxy-finance, qi-investicni-spolecnost, riverside-acceleration-capital, rsj-investments, rtp-global, safar-and-partners, seedtwo-capital, skylimit-investments, stratum-partners, tarpan-partners, tibiq, token-ventures, tomenterprise, triplebee, uk-innovations-prague, unbound, underground-ventures, university2ventures, up21, value4capital, viking-global-investors, vocal-vc, white-star-capital, y-combinator, zero-gravity-capital.
