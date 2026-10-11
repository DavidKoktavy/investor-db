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
