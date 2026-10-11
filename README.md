# Spolehlivá databáze investorů — pilot: VC v ČR

Řešení zadání A (Junior AI Developer). Pravidla, zdroje a metodika jsou v [PLAN.md](PLAN.md).

> _Kostra. Sekce označené `TODO` doplním po pilotu z `results/accuracy.md`, `docs/decisions.md` a `docs/ai-errors.md`._

## Výsledek v číslech

| Kandidáti | Zařazeno | Přesnost záznamu (95% CI) | Platnost citací | Náklad na záznam |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

Podrobně: [results/accuracy.md](results/accuracy.md) · data: [data/records/cz_vc.jsonl](data/records/cz_vc.jsonl) · rozhodnutí o každém kandidátovi: [data/candidates/cz_vc_decisions.csv](data/candidates/cz_vc_decisions.csv)

## Co je v repozitáři

| Cesta | Obsah |
|---|---|
| `PLAN.md` | plán: kdo do databáze patří, zdroje, ověřování, odhad rozsahu, náklady |
| `schema/` | schéma záznamu + smyšlený ukázkový záznam |
| `.claude/agents/` | pokyny pro tři agenty (historie změn je v commitech `agents:`) |
| `src/`, `tests/` | kontrola citací, pravidla zařazení, metriky |
| `data/` | kandidáti, záznamy, ověření, ruční kontrola, log běhů |
| `results/` | výsledky měření |
| `docs/` | rozhodnutí a chyby AI |
| `ai-log/` | exporty konverzací s Claude Code |

## Jak spustit

TODO (venv, příkazy pro validate / check_quotes / decide / metrics)

## Jak jsem pracoval s AI

### Rozdělení práce
TODO. Plán a první verzi pokynů pro agenty jsem připravil v konverzaci s Claude na claude.ai (viz `ai-log/00-…`), zbytek v Claude Code.

### Jaké pokyny dostali agenti
TODO: odkaz na `.claude/agents/`, proč tři role, proč ověřovatel bez vyhledávání a na jiném modelu, jak se pokyny měnily.

### Jak jsem kontroloval jejich výstup
TODO: skript na citace, nezávislý ověřovatel, pravidla v kódu, ruční kontrola naslepo; shoda ověřovatele s ruční kontrolou.

### Kde se AI mýlila
TODO: konkrétní příklady z `docs/ai-errors.md` (záznam, pole, co bylo špatně, jak jsem to zachytil, co jsem změnil).

## Rozhodnutí v nejasných bodech zadání

TODO: shrnutí z `docs/decisions.md`.

## Co v řešení chybí

TODO

## Náklady na celý svět

TODO: vzorec z PLAN §8 s hodnotami naměřenými v pilotu.
