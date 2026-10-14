# Výsledky měření přesnosti — pilot VC v ČR

Kandidátů: **224** · zařazeno (active): **34** · plných záznamů (extrakce): 69 · řádků ruční kontroly: 48/48

## Hlavní čísla

| Metrika | Hodnota |
|---|---|
| Přesnost záznamu (aktivní VC/CVC s týmem v ČR) | 75.0 % (9/12; 95% CI 46.8–91.1 %) |
| Správnost vyřazení — pipeline | 90.0 % (9/10; 95% CI 59.6–98.2 %) |
| Správnost vyřazení — triáž (vzorek) | 100.0 % (5/5; 95% CI 56.6–100.0 %) |
| Přesnost údajů ve finální databázi (všechna pole) | 90.0 % (18/20; 95% CI 69.9–97.2 %) |
| Přesnost údajů od extraktoru před ověřením | 90.5 % (19/21; 95% CI 71.1–97.3 %) |
| Platnost citací (citace nalezena na stránce) | 97.9 % (424/433; 95% CI 96.1–98.9 %) |
| Ověřovatel zahodil správný údaj | 0× |
| Ověřovatel propustil chybný údaj | 0× |
| Náklad výpočtu celkem / na zařazený záznam | 18.04 USD / 0.53 USD |
| Ruční kontrola | 10.0 min (0.8 min na záznam) |

## Pole: vyplněnost a přesnost

| Pole | Vyplněnost | Přesnost (finální DB) | Přesnost (extraktor) |
|---|---|---|---|
| type | 100.0 % (34/34; 95% CI 89.8–100.0 %) | – | – |
| hq_country | 100.0 % (34/34; 95% CI 89.8–100.0 %) | – | – |
| sectors | 73.5 % (25/34; 95% CI 56.9–85.4 %) | – | – |
| stages | 76.5 % (26/34; 95% CI 60.0–87.6 %) | – | – |
| ticket | 61.8 % (21/34; 95% CI 45.0–76.1 %) | 85.7 % (6/7; 95% CI 48.7–97.4 %) | 85.7 % (6/7; 95% CI 48.7–97.4 %) |
| capital | 41.2 % (14/34; 95% CI 26.4–57.8 %) | 100.0 % (1/1; 95% CI 20.7–100.0 %) | 100.0 % (2/2; 95% CI 34.2–100.0 %) |
| legal_entities | 100.0 % (34/34; 95% CI 89.8–100.0 %) | – | – |
| evidence_of_activity | 100.0 % (34/34; 95% CI 89.8–100.0 %) | 91.7 % (11/12; 95% CI 64.6–98.5 %) | 91.7 % (11/12; 95% CI 64.6–98.5 %) |

## Ověřovatel vs. ruční kontrola

| verdikt ověřovatele | correct | partially | incorrect | unverifiable |
|---|---|---|---|---|
| none | 1 | 0 | 0 | 0 |
| partially_supported | 2 | 0 | 0 | 0 |
| supported | 16 | 2 | 0 | 0 |

## Trychtýř rozhodnutí

| rozhodl / stav / důvod | počet |
|---|---|
| none:pending: | 88 |
| pipeline:active: | 34 |
| pipeline:dormant: | 2 |
| pipeline:excluded:grant_or_program_only | 2 |
| pipeline:excluded:no_recent_investment | 1 |
| pipeline:excluded:not_found_or_defunct | 4 |
| pipeline:excluded:out_of_scope_geography | 7 |
| pipeline:excluded:out_of_scope_type | 18 |
| pipeline:excluded:real_estate_only | 1 |
| triage:excluded:advisor_or_intermediary | 1 |
| triage:excluded:debt_only | 1 |
| triage:excluded:out_of_scope_geography | 60 |
| triage:excluded:out_of_scope_type | 5 |

## Kontrola citací (skript) a verdikty ověřovatele

- citace: {'found': 424, 'unreachable': 6, 'missing': 3}
- ověřovatel: {'supported': 322, 'partially_supported': 107, 'unverifiable': 6, 'unsupported': 1}

## Náklady podle agenta

| agent | běhů | tokenů | nástrojů | čas (min) | USD (odhad) |
|---|---|---|---|---|---|
| candidate-scout | 3 | 536,034 | 498 | 118 | 1.5 |
| candidate-triage | 23 | 2,109,429 | 982 | 146 | 0.3 |
| evidence-verifier | 81 | 1,417,346 | 680 | 44 | 7.94 |
| investor-extractor | 87 | 2,965,744 | 1452 | 135 | 8.3 |

_Intervaly jsou 95% Wilsonovy. USD je odhad z celkových tokenů (90 % vstup / 10 % výstup, ceník PLAN §8)._
