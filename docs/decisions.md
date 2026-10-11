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
